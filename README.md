# indeed-job-webscraper

About the project
--
Webscrape the following fields from https://www.indeed.com jobs:

- `job_title`: Job title.
- `job_type`: Job type: Full-time, Part-time, Contract, Temporary or Internship.
- `company_name`: Company listing job.
- `location`: Job location.
- `company_rating`: Company rating out of five (5).
- `company_reviews`: Number of company reviews.
- `description`: Job description.
- `salary_low`:  Salary low, parsed from `description`.
- `salary_high`: Salary high, parsed from `description`.
- `experience`: Years of experience, parsed from `description`.
- `job_posted`: Days since job was posted.
- `url`: Job listing url.
- `page`: Search result page number.


<img width="713" alt="Screen Shot 2021-11-09 at 8 43 18 am" src="https://user-images.githubusercontent.com/61095925/140824583-d20fc240-3c0d-442c-abc5-86df7ea0e766.png">

Installation
--

#### Install python 3.8 ####
    https://www.python.org/downloads/release/python-387/

#### Clone repo ####

    git clone https://github.com/jcoleiro/indeed-job-webscraper.git

#### Create virtual environment (Recommended) ####

macOS

    $ python3 -m venv venv

Windows

    $ c:\>c:\Python35\python -m venv venv

#### Start virtual environment (Recommended) ####

macOS

    $ source venv/bin/activate

Windows

    $ source venv/Scripts/activate

#### Install python requirements ####

    $ pip install -r requirements.txt

Usage
--

#### Configure config.json ####

Configure the following inputs using `config.json`:
- `search`: Job title, keywords, or company search.
- `location`: City and/or state of job is located.
- `country`: Country the job is located. Refer to `domains.json` for correct available options.
- `max_pages`:  Maximum page limit to scrape. There are 15 jobs results per page.
- `output_file_name`: Output file name to be output in csv and json format to folder `/output`.
- `params`: Search query parameters (Optional): Date Posted, Experience Level and Location.
- `fields`: Fields to scrape and parse into formatted types.

#### Execute scraper.py ####

    $ python scraper.py

![Screen Shot 2021-11-09 at 9 50 30 am](https://user-images.githubusercontent.com/61095925/140830889-78eb6b8f-1c9c-4bb3-a513-76bc2d08971b.png)

#### Output ####

All filed out output to the folder `/output` in csv and json format.

<img width="870" alt="Screen Shot 2021-11-09 at 8 46 16 am" src="https://user-images.githubusercontent.com/61095925/140830357-c3bc2a7a-3b00-4b33-ae6c-e977d6d2ea4a.png">

![Screen Shot 2021-11-09 at 8 55 28 am](https://user-images.githubusercontent.com/61095925/140830410-b672c090-71c0-4d50-b4c7-86bc98e9bffb.png)

Support
--

[![GitHub Issues](https://img.shields.io/github/issues/harismuneer/Ultimate-Facebook-Scraper.svg?style=flat&label=Issues&maxAge=2592000)](https://github.com/jcoleiro/indeed-job-webscraper/issues)

If you face any issue, you can create a new issue in the Issues Tab and I will be glad to help you out.

Alternatively, you can contact me at joshuacoleiro@gmail.com.

Licence
--
[![MIT](https://img.shields.io/cocoapods/l/AFNetworking.svg?style=style&label=License&maxAge=2592000)](LICENSE)

Copyright (c) 2021-present, jcoleiro, Joshua Coleiro

