import os
import pandas as pd


def load_inn(file):
    if os.path.exists(file):
        df = pd.read_csv(file)
        print(df.head())
    else:
        print(f'file {file} does not exist')
        df = False
    return df
