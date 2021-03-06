from os import link
import os
from bs4 import BeautifulSoup
from .scrap_job_page import scrap_job_page


"""
Job Object Structure
    position
    location
    company --> company name
    category
    requirement --> list of job requirements (string)
    email
    phone number
"""

DIRNAME = os.path.dirname(__file__)
JOBPAGE_FOLDER = DIRNAME + "/joblistSite/index.html"


def get_job_list():
    with open(JOBPAGE_FOLDER) as main_page:
        soup = BeautifulSoup(main_page, 'html.parser')

    anchor_list = soup.find_all('a')
    job_page_object_list = []

    for anchor_element in anchor_list:
        link_path = anchor_element["href"].split("/")[1]
        job_page_object_list.append(scrap_job_page(link_path))

    return job_page_object_list


x = get_job_list()
print((x[0])['position'])
