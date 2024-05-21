#打印文字 https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/2024MMDD/hh
#2024MMDD 為年份月份日期 MM只採用01~04 DD只採用01~31 hh為00~23 
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
#若網址存在則將網頁內的所有.CSV檔下載 儲存在C:\Users\User\Desktop\cycu_ai2024\20240521\IMFORMATION
#檔名為2024MMDDhh.csv

import requests
import os
from bs4 import BeautifulSoup
import csv

#建立資料夾
if not os.path.exists("C:/Users/User/Desktop/cycu_ai2024/20240521/IMFORMATION"):
    os.makedirs("C:/Users/User/Desktop/cycu_ai2024/20240521/IMFORMATION")

#爬蟲
for month in range(1, 5):  # MM: 01~04
    for day in range(1, 32):  # DD: 01~31
        for hour in range(24):  # hh: 00~23
            url = base_url.format(month, day, hour)
            res = requests.get(url)
            if res.status_code == 200:
                soup = BeautifulSoup(res.text, "html.parser")
                links = soup.find_all("a")
                for link in links:
                    href = link.get("href")
                    if href.endswith(".csv"):
                        res_csv = requests.get(href)
                        filename = f"2024{month:02d}{day:02d}{hour:02d}.csv"
                        with open(f"C:/Users/User/Desktop/cycu_ai2024/20240521/IMFORMATION/{filename}", "wb") as f:
                            f.write(res_csv.content)
                            print(f"Downloaded {filename}")
            else:
                print(f"{url} does not exist")
                