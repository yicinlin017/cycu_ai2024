
# https://vipmbr.cpc.com.tw/mbwebs/ShowHistoryPrice_oil.aspx

import requests
from bs4 import BeautifulSoup
import pandas as pd

# 發送HTTP請求
url = "https://vipmbr.cpc.com.tw/mbwebs/ShowHistoryPrice_oil.aspx"
response = requests.get(url)

# 解析HTML內容
soup = BeautifulSoup(response.text, 'html.parser')

# 找到所有的table元素
tables = soup.find_all('table')

# 將每個table轉換為一個dataframe
dataframes = [pd.read_html(str(table))[0] for table in tables]

# 打印出所有的dataframe
df1, df2 = dataframes
print("DataFrame 1:")
print(df1)
print("\nDataFrame 2:")
print(df2)

# 將每個dataframe保存到CSV文件中
df1.to_csv('dataframe_1.csv', index=False)
df2.to_csv('dataframe_2.csv', index=False)

# 只保留前兩個欄位
df2 = df2.iloc[:, :2]

# 去除第二欄值是NaN的資料
df2 = df2.dropna(subset=[df2.columns[1]])

# 將第一欄的資料型態轉換為datetime
df2[df2.columns[0]] = pd.to_datetime(df2[df2.columns[0]])

print(df2)

import matplotlib.pyplot as plt

# 假設你的日期欄位是第一欄，油價欄位是第二欄
plt.plot(df2[df2.columns[0]], df2[df2.columns[1]])

plt.xlabel('Date')
plt.ylabel('Oil Price')
plt.title('Oil Price Over Time')

plt.show()