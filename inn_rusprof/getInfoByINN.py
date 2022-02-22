import requests
from bs4 import BeautifulSoup
import re
import json

# URL = 'https://www.rusprofile.ru/id/3836792'
URL = 'https://www.rusprofile.ru/id/10717383'  # "Магнит"

HEADERS = {
    'authority': 'www.rusprofile.ru',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'ru-RU,ru;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6',
    'cookie': '_ym_uid=1620917797648814167; _ym_d=1638602191; user_return_url=https%3A%2F%2Fwww.rusprofile.ru%2Fid%2F10717383; sessid=bc81541404253e852fb8695f7e107a57; _ym_isad=1'
}


def get_html(url, params=None):
    # r = requests.get(url, headers=HEADERS, params=params)
    r = requests.get(url=url, headers=HEADERS)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    phones = soup.find_all('a', href=re.compile('tel:'))
    sites = soup.find_all('a', href=re.compile('http://'))
    emails = soup.find_all('a', href=re.compile('mailto:'))

    company_phones = []
    for phone in phones:
        company_phones.append({
            'telephone': phone.get('href').replace('tel:', '')
        })

    company_sites = []
    for site in sites:
        company_sites.append({
            'site': site.get('href')
        })

    company_emails = []
    for email in emails:
        company_emails.append({
            'email': email.get('href').replace('mailto:', '')
        })
    return company_phones, company_sites, company_emails


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        company_telephones, company_sites, company_mails = get_content(html.text)
    else:
        print('Something wrong')
    # print(company_telephones)
    return company_telephones, company_sites, company_mails


if __name__ == '__main__':
    companies_contacts = []
    company = '10717383'
    companies_contacts.append({
        company: parse()
    })
    print(companies_contacts)
    json_data = json.dumps(companies_contacts, indent=4, ensure_ascii=False)
    with open("rusprofile_contacts.json", 'w') as file:
        file.write(json_data)
    file.close()
