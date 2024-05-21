#爬蟲https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/
#下載網址內檔案名稱 M05A_2024MMDD.tar.gz 01<=MM<=04 01<=DD<=31
#儲存在/workspaces/cycu_ai2024/20240521/imfotmatiom 資料夾下

import requests
import os
import time
import datetime
import random
import sys
import logging

def download_file(url, filename):
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(filename,
                    'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
    return filename

def download_file_to_folder(url, folder):
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(os.path.join(folder, os.path.basename(url)),
                    'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
    return os.path.join(folder, os.path.basename(url))

def download_file_to_folder_with_filename(url, folder, filename):
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(os.path.join(folder, filename),
                    'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
    return os.path.join(folder, filename)

def download_file_to_folder_with_filename_and_retry(url, folder, filename, retry=3):
    for i in range(retry):
        try:
            return download_file_to_folder_with_filename(url, folder, filename)
        except Exception as e:
            logging.error(f"Error: {e}")
            time.sleep(random.randint(1, 3))
    return None

