import time
from datetime import timedelta
from decouple import config
import load_inns
import getInfoByINN as gc
import json
import random
import numpy as np


def save_result(companies_contacts, err=False):
    if not err:
        file_result = config('file_legal_w_contacts')
        json_data = json.dumps(companies_contacts, indent=4, ensure_ascii=False)
        with open(file_result, 'w') as file:
            file.write(json_data)
        file.close()
    else:
        file_result = config('file_err_inn')
        np.savetxt(file_result, companies_contacts, delimitier=',')


if __name__ == '__main__':
    start_time = time.time()
    file_legal = config('file_legal', default='')
    inns = load_inns.load_inn(file_legal)['SRC_INN']
    companies_contacts = []
    inn_err = []
    count = 0
    for index, inn in inns.items():
        count += 1
        try:
            if gc.get_contacts(str(inn)) is not None:
                companies_contacts.append(gc.get_contacts(str(inn)))
                save_result(companies_contacts)
                time.sleep(random.randint(20, 60))
            else:
                inn_err.append(inn)
                save_result(inn_err, err=True)
                time.sleep(120)
            print(f'---- Row number {count} ---')
            print(' elapsed time: ', str(timedelta(seconds=time.time() - start_time)))
            print(companies_contacts[-1:])

        except Exception as e:
            print(e)
            inn_err.append(inn)
            # save_result(inn_err, err=True)
            time.sleep(120)

        print(' elapsed time: ', str(timedelta(seconds=time.time() - start_time)))
