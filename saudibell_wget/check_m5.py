import hashlib
from decouple import config
import os
import pandas as pd


def md5(fname):
    hash_md5 = hashlib.md5()
    hash_md5.update(open(fname, 'rb').read())
    return hash_md5.hexdigest()


if __name__ == '__main__':
    out_dir = config('OUT_PATH')
    m5 = config('M5')

    df = pd.read_csv(m5, sep='  ', engine='python')
    # print(df.head(10))
    # print(df.loc[df['filename'].str.strip() == 'tiles_16.zip.001']['hash'].values[0])

    for file in os.listdir(out_dir):
        hash_file = md5(out_dir + '/' + file)
        if df.loc[df['filename'] == file]['hash'].values[0] == hash_file:
            print(f'{file} True')
        else:
            print(f'----- for {file} hash {hash_file} does not match:')
            print(df.loc[df['filename'] == file]['filename'].values[0])
            print(df.loc[df['filename'] == file]['hash'].values[0])
