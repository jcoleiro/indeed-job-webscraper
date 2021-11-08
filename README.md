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
    
#### Output ####

All filed out output to the folder `/output` in csv and json format.
    
Support
--

Raise a github [issue](https://github.com/jcoleiro/indeed-job-webscraper/issues), or contact me at joshuacoleiro@gmail.com.

    
