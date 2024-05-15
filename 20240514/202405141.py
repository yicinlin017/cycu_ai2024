#下載https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/20240429/18/ 中的 TDCS_M05A_20240429_180000.csv

import requests
import os

url = "https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/20240429/18/TDCS_M05A_20240429_180000.csv"
filename = url.split("/")[-1]
path = os.path.join("20240514", filename)

response = requests.get(url)
with open(path, "wb") as f:
    f.write(response.content)
print(path)

#讀取/workspaces/cycu_ai2024/20240514/TDCS_M05A_20240429_180000.csv
#將欄位插入一列欄位名稱  第一欄位為時間 第二欄位為地點1 第三欄位為地點2 第四欄位為車種 第五欄位為車速 第六欄位為交通量
#打印出來
import pandas as pd
df = pd.read_csv(path, header=None)
df.columns = ["時間", "地點1", "地點2", "車種", "車速", "交通量"]

#車種欄位內 31為小客車、32為小貨車、41為大客車、42為大貨車、5為聯結車
#將欄位改成  第一欄位為地點1  第二欄位為小客車車速 第三欄位為小客車交通量
#打印
df = df[df["車種"].isin([31])]
df = df[["地點1", "車速", "交通量"]]
df.columns = ["地點1", "小客車車速", "小客車交通量"]
print(df)
#篩選掉地點一最後一個字元不是s的資料
df = df[df["地點1"].str[-1] == "S"]
#篩選掉地點一第二個字元不是1的資料
#打印
df = df[df["地點1"].str[1] == "1"]

#將地點1欄位改成里程欄位 資料只取用第四個字元到第七個字元
#打印
df["里程"] = df["地點1"].str[3:7]
df = df[["里程", "小客車車速", "小客車交通量"]]
print(df)
#儲存在/workspaces/cycu_ai2024/20240514/0429180000.csv
df.to_csv("20240514/0429180000.csv", index=False)

