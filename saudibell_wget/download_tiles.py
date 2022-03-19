import os.path
import urllib.error

from decouple import config
import wget
import time
from datetime import timedelta


def getFullFtpPath():
    ftp_server = config('FTP_SERVER')
    ftp_user = config('FTP_USER')
    ftp_pass = config('FTP_PASS')
    ftp_dir = config('FTP_DIR')
    return 'ftp://' + ftp_user + ':' + ftp_pass + '@' + ftp_server + '/' + ftp_dir + '/'


if __name__ == '__main__':
    first_start_time = time.time()
    out_path = config('OUT_PATH')
    tile_number = input('Tiles number see XX tiles_XX.zip.0YY:')
    tile_part = input('Tile part see YY tiles_XX.zip.0YY:')
    tile_end = input('Tiles End file:')
    print(f'tiles_{tile_number}.zip.0{tile_part}')
    try:
        int(tile_number)
        int(tile_part)
        int(tile_end)
    except ValueError as err:
        print("No.. input is not a number. ", err)
        exit(1)

    for i in range(int(tile_part), int(tile_end)+1):
        start_time = time.time()
        file = f'tiles_{tile_number}.zip.0{i}'
        try:
            if os.path.isdir(out_path):
                print(f'-------------------- downloading {file} to {out_path} -----------')
                wget.download(getFullFtpPath() + file, out=out_path)
                print(f' elapsed time download {file}: ', str(timedelta(seconds=time.time() - start_time)))
                print(f' general elapsed time download {file}: ',
                      str(timedelta(seconds=time.time() - first_start_time)))
            else:
                print(f'the folder {out_path} does not exist')
        except urllib.error.ContentTooShortError as err:
            print(f'!!!!!!!ERROR while downloading {file} - urllib.error.ContentTooShortError', err)
            pass
