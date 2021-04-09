import re
import os
from bs4 import BeautifulSoup

DIRNAME = os.path.dirname(__file__)
JOBPAGE_FOLDER = DIRNAME + "/joblistSite/jobPage"


def scrap_job_page(job_page):
    with open(f"{JOBPAGE_FOLDER}/{job_page}") as job_page:
        soup = BeautifulSoup(job_page, 'html.parser')

    return extract_job_info(soup)


def extract_job_info(soup):
    job_object = {
        "position": soup.find(id="jobPosition").string.strip(),
        "location": soup.find(id="companyLocation").string.strip(),
        "company": soup.find(id="companyName").string.strip(),
        "category": soup.find(id="jobCategory").string.split(":")[1].strip(),
        "requirement": []
    }

    # Special Treatment for Job Description and Contact
    li_list = soup.find_all(name="li")
    for li_element in li_list:
        content = li_element.string.strip()
        content = re.sub(r"\s+", " ", content)

        # Detect whether the list object is email or phone number
        if(re.search("Email : ", content)):
            job_object["email"] = content.split(": ")[1]
            continue

        if(re.search("Phone Number :", content)):
            job_object["phone"] = content.split(": ")[1]
            continue

        job_object["requirement"].append(content)

    return job_object
