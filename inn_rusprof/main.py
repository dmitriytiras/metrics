import os
import time
from datetime import timedelta
from decouple import config
import load_inns
import getInfoByINN as gc
import json


def save_result(companies_contacts):
    json_data = json.dumps(companies_contacts, indent=4, ensure_ascii=False)
    with open(config('file_legal_w_contacts'), 'w') as file:
        file.write(json_data)
    file.close()


if __name__ == '__main__':
    start_time = time.time()
    file_legal = config('file_legal', default='')
    inns = load_inns.load_inn(file_legal)['SRC_INN']
    companies_contacts = []
    for index, inn in inns.items():
        companies_contacts.append(gc.get_contacts(str(inn)))
        save_result(companies_contacts)
        time.sleep(2)
        print(companies_contacts[-1:])
    print(' elapsed time: ', str(timedelta(seconds=time.time()-start_time)))