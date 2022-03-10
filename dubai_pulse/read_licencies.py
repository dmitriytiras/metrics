import os
import pandas as pd
from decouple import config
import time
from datetime import timedelta

def load_licencies(file):
    if os.path.exists(file):
        df = pd.read_csv(file)
        print(df.head())
    else:
        print(f'file {file} does not exist')
        df = False
    return df


if __name__ == '__main__':
    df = load_licencies(config('file_license_master'))
    df.head()