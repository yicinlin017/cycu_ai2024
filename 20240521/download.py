#打印文字 https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/2024MMDD/hh
#MM只採用01~04 DD只採用01~31 hh為00~23 
#使用迴圈產生
#範例https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/20240101/00  https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/20240102/01
base_url = "https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/2024{:02d}{:02d}/{:02d}"

for month in range(1, 5):  # MM: 01~04
    for day in range(1, 32):  # DD: 01~31
        for hour in range(24):  # hh: 00~23
            url = base_url.format(month, day, hour)
            print(url)

#爬蟲打印出來的網址 
#若網址不存在則跳過
#若網址存在則將網頁內的所有.CSV檔下載 儲存在/workspaces/cycu_ai2024/20240521/imfotmatiom
import requests
import os
import csv
from bs4 import BeautifulSoup

#建立目錄
os.makedirs("/workspaces/cycu_ai2024/20240521/imfotmatiom", exist_ok=True)

for month in range(1, 5):  # MM: 01~04
    for day in range(1, 32):  # DD: 01~31
        for hour in range(24):  # hh: 00~23
            url = base_url.format(month, day, hour)
            response = requests.get(url)
            if response.status_code == 404:
                continue

            soup = BeautifulSoup(response.text, "lxml")
            for a in soup.find_all("a", href=True):
                if a["href"].endswith(".csv"):
                    file_url = url + a["href"]
                    file_name = file_url.split("/")[-1]
                    response = requests.get(file_url)
                    with open(f"/workspaces/cycu_ai2024/20240521/imfotmatiom/{file_name}", "wb") as f:
                        f.write(response.content)
                    print(file_url)
                    