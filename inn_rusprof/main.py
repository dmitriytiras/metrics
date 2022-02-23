import os
import time
from datetime import timedelta
from decouple import config
import load_inns

if __name__ == '__main__':
    start_time = time.time()
    file_ind = config('file_inn_ind', default='')
    file_leagal = config('file_inn_legal', default='')

    df_ind = load_inns.load_inn(file_ind)

    print(' elapsed time: ', str(timedelta(seconds=time.time()-start_time)))