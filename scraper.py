"""
    Indeed.com job web scraper.
    Configure the following inputs using config.json.
    args:
        search (str): Job title, keywords, or company search.
        location (str): City and/or state of job is located.
        country (str): Country where job is located. Refer to domains.json list for country options.
        max_pages (int): Maximum page limit to scrape. There are 15 jobs per page.
        output_file_name (str): Output file name NOT including file type extension.
        params (List[Dict[str, Any]]): Search query parameters: Date Posted, Experience Level and Location (Optional)
        fields (List[Dict[str, Any]]): Fields to scrape and parse into formatted types.
"""
import csv
import json
import re
from typing import (
    Any,
    AnyStr,
    Dict,
    List,
    Match,
    Optional,
    Union
)

import requests
from bs4 import BeautifulSoup
from bs4.element import NavigableString, Tag

with open('config.json') as json_file:
    config: Dict[str, Any] = json.load(json_file)

with open('domains.json') as json_file:
    domains: Dict[str, str] = json.load(json_file)

domain: str = domains.get(config['country'], 'https://www.indeed.com')

def main():
    """Main function to scrape indeed jobs."""
    data: List[Dict[str, Optional[Union[str, int, float]]]] = []
    for page in range(config['max_pages']):
        print(f'Scraping page {page+1} of max {config["max_pages"]} for {config["search"]} in {config["location"]}')
        params: Dict[str, Union[str, int]] = {
            'q': config['search'],
            'l': config['location'],
            'start': page*10,
            **{param['key']: param['value'] for param in config['params'] if param['value']}
        }
        response: requests.Response = requests.get(
            f'{domain}/jobs',
            params=params,
        )

        results_soup: BeautifulSoup = BeautifulSoup(response.text, 'html.parser')
        result_header: Optional[Union[Tag, NavigableString]] = results_soup.find('h1')
        if result_header and 'did not match any jobs' in result_header.text:
            print(result_header.text)
            break

        results: List[str] = [
            result['href']
            for result
            in results_soup.find_all('a', attrs={'class': 'result'})
        ]

        for index, result in enumerate(results):
            url: str = f'{domain}{result}'
            row: Dict[str, Optional[Union[str, int, float]]] = {}
            response: requests.Response = requests.get(url)
            job_soup: BeautifulSoup = BeautifulSoup(response.text, 'html.parser')
            header: str = job_soup.find('h1').text if job_soup.find('h1') else ''
            print(f'Result {(page * 10) + index + 1}: {header}')

            for field in config['fields']:
                element: Optional[Union[Tag, NavigableString]] = job_soup.find(**{
                    key: value if key != 'text' else re.compile(value)
                    for key, value
                    in field.items()
                    if value
                    and key in ['name', 'text', 'attrs']
                })
                if element is None:
                    row[field['key']] = None
                    continue

                attribute: str = field['attribute']
                value: Optional[str] = element.text.strip()\
                    if attribute == 'text'\
                    else element.get(attribute)

                if value is None:
                    row[field['key']] = None
                    continue

                for operator in field['post_processing']:
                    if operator['type'] == 'regex_match':
                        search: Optional[Match[AnyStr]] = re.search(operator['value'], value)
                        value: Optional[str] = search.group() if search else None
                        if value is None:
                            break
                    if operator['type'] == 'regex_remove':
                        value: str = re.sub(operator['value'], '', value)

                if field['type'] == 'integer':
                    value: Optional[int] = int(value) if isinstance(value, str) and value.isnumeric() else None
                elif field['type'] == 'float':
                    value: Optional[float] = float(value) if re.match(r'\d+\.*\d*', value) else None

                row[field['key']] = value

            data.append({
                **row,
                'url': url,
                'page': page + 1,
            })

        if results_soup.find('a', attrs={'aria-label': 'Next'}) is None:
            print('No more results')
            break
    print(f'Total jobs scraped: {len(data)}')

    with open(f'{config["output_file_name"]}.csv', 'w') as csv_file:
        fieldnames: List[str] = list(data[0].keys() if data else [])
        dict_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        dict_writer.writeheader()
        dict_writer.writerows(data)

    with open(f'{config["output_file_name"]}.json', 'w') as json_file:
        json.dump(data, json_file)

if __name__ == "__main__":
    main()
