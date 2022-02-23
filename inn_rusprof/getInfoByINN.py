import requests
from bs4 import BeautifulSoup
import re
import json
from decouple import config

HEADERS = {
    'user-agent': config('user-agent'),
    'accept': config('accept'),
    'cookie': config('cookie')
}


def get_html(url, params=None):
    # r = requests.get(url, headers=HEADERS, params=params)
    print(url)
    print(HEADERS)
    r = requests.get(url=url, headers=HEADERS)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    phones = soup.find_all('a', href=re.compile('tel:'))
    sites = soup.find_all('a', href=re.compile('http://'))
    emails = soup.find_all('a', href=re.compile('mailto:'))

    company_contacts = {}

    company_phones = []
    for phone in phones:
        company_phones.append(phone.get('href').replace('tel:', ''))

    company_sites = []
    for site in sites:
        company_sites.append(
            site.get('href')
        )

    company_emails = []
    for email in emails:
        company_emails.append(email.get('href').replace('mailto:', ''))

    company_contacts["telephones"] = company_phones
    company_contacts["sites"] = company_sites
    company_contacts["emails"] = company_emails

    return company_contacts


def parse():
    url = config('URL')
    html = get_html(url)
    if html.status_code == 200:
        company_contacts = get_content(html.text)
    else:
        print('Something wrong')
    # print(company_telephones)
    return company_contacts


def get_contacts():
    companies_contacts = []
    # company = {'INN': '10717383'}
    company_info = {'company_info': {'INN': '2310031475'}}
    companies_contacts.append(company_info)
    companies_contacts.append({
        'company_contacts': parse()
    })
    print(companies_contacts)
    json_data = json.dumps(companies_contacts, indent=4, ensure_ascii=False)
    with open(config('file_legal_w_contacts'), 'w') as file:
        file.write(json_data)
    file.close()


if __name__ == '__main__':
    get_contacts()
