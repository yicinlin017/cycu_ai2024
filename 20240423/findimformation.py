#爬蟲網址https://tisvcloud.freeway.gov.tw/history/TDCS/M04A/20240416/00/ 到 https://tisvcloud.freeway.gov.tw/history/TDCS/M04A/20240423/23/   
#爬蟲網址使用回圈生成 格式https://tisvcloud.freeway.gov.tw/history/TDCS/M04A/YYYYMMDD/HH/ YYYY為2024 MM為月份 DD為日期 HH為小時
#印出迴圈產生之網址

#下載各網址所有CSV的資料
#下載後存入資料夾/workspaces/cycu_ai2024/middlework
import requests
import os
import time
import datetime
import pandas as pd
from datetime import datetime
from datetime import timedelta
import csv
import re

#生成日期清單
daystart = datetime.strptime("20240416", "%Y%m%d")
dayend = datetime.strptime("20240423", "%Y%m%d")
daygenerated = [daystart + timedelta(days=x) for x in range(0, (dayend-daystart).days + 1)]

#生成小時清單
hourgenerated = []
for i in range(0,24):
    hourgenerated.append(str(i).zfill(2))

#生成分鐘清單
mingenerated = []
for i in range(0,60,5):
    mingenerated.append(str(i).zfill(2))

#生成網址清單
url_list = []
for day in daygenerated:
    for hour in hourgenerated:
        for minute in mingenerated:
            url = "https://tisvcloud.freeway.gov.tw/history/TDCS/M04A/"+day.strftime("%Y%m%d")+"/"+hour+"/"+minute+"/"
            url_list.append(url)

#下載檔案

for url in url_list:
    try:
        response = requests.get(url)
        response.raise_for_status()
        print("下載成功")
    except requests.exceptions.RequestException as e:
        print("下載失敗")
        continue
    #取得檔案名稱
    filename = re.search(r'(?<=M04A/)\d{8}/\d{2}/\d{2}', url).group(0)
    filename = filename.replace("/", "")
    filename = filename.replace("/", "")
    filename = filename + ".csv"
    #存檔
    with open("/workspaces/cycu_ai2024/middlework/"+filename, "wb") as f:
        f.write(response.content)
    time.sleep(1)
print("下載結束")
