# https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/
#爬蟲網址https://tisvcloud.freeway.gov.tw/history/TDCS/M04A/20240416/00/ 到 https://tisvcloud.freeway.gov.tw/history/TDCS/M04A/20240423/23/   所有CSV的資料
#下載TDCS_M04A_YYYYMMDD_hhmmss.csv YYYY為2024 MM為月份 DD為日期 hh為小時  mm為分鐘 ss為秒 MMDD取0416到0423 hh取00到23 mm取00到55 ss取00
#下載後存入資料夾/workspaces/cycu_ai2024/20240423
#下載後存成CSV檔案
#檔名範例 TDCS_M05A_20240423_203500.csv TDCS_M05A_20240423_203000.csv TDCS_M05A_20240423_202500.csv
#檔案內容範例
#車道,方向,位置,車種,日期,時間,當量
#1,0,0,31,20240423,00,0
#1,0,0,32,20240423,00,0
#1,0,0,51,20240423,00,0


import requests
import os
import pandas as pd
from datetime import datetime
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import matplotlib
start_date = 16
end_date = 23

# 生成日期範圍
dates = [f"202404{i:02d}" for i in range(start_date, end_date + 1)]

# 爬蟲
for date in dates:
    for i in range(24):
        url = f"https://tisvcloud.freeway.gov.tw/history/TDCS/M04A/{date}/{i:02d}/"
        response = requests.get(url)
        if response.status_code == 200:
            if not os.path.exists(date):
                os.mkdir(date)
            with open(f"{date}/{date}_{i:02d}.csv", "wb") as f:
                f.write(response.content)
                print(f"下載 {url} 成功")
        else:
            print(f"下載 {url} 失敗")
