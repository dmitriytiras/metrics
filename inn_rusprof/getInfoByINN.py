import requests
from bs4 import BeautifulSoup
import re
from decouple import config

HEADERS = {
    'user-agent': config('user-agent'),
    'accept': config('accept'),
    'cookie': config('cookie')
}


def get_link(inn):
    url_search = config('URL_SEARCH') + inn + config('URL_SEARCH_ACTION')
    r = requests.get(url_search, headers=HEADERS)
    link = r.json().get('ul')[0].get('link')
    return link


def get_html(url, params=None):
    r = requests.get(url=url, headers=HEADERS)
    return r


def get_company_contacts(html):
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


def parse(url):
    html = get_html(url)
    if html.status_code == 200:
        company_contacts = get_company_contacts(html.text)
    else:
        company_contacts = ''
        print('Something wrong')
    return company_contacts


def get_contacts(inn):
    company_info = {'company_info': {'INN': inn,
                                     'link': config('URL') + get_link(inn),
                                     'company_contacts': parse(config('URL') + get_link(inn))}}
    return company_info
