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

    for i in range(14, 49):
        start_time = time.time()
        file = f'tiles_16.zip.0{i}'
        print(f'-------------------- {file} -----------')
        wget.download(getFullFtpPath() + file, out=out_path)
        print(f' elapsed time download {file}: ', str(timedelta(seconds=time.time() - start_time)))
        print(f' general elapsed time download {file}: ', str(timedelta(seconds=time.time() - first_start_time)))
