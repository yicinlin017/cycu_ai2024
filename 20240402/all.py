##################################################
##################################################
#尋找台灣的區界地圖 shape file/ geojson file
#read 20240402/tract_20140313.json as geopanas
import geopandas as gpd
import pandas as pd

#read shape file
df_taiwan=gpd.read_file('/workspaces/cycu_ai2024/20240402/mapdata202301070205/COUNTY_MOI_1090820.shp')

##################################################
##################################################
# crawler from rss of central weather agency

import requests
import feedparser

county_list = []
for num in range(1, 23):
    #string format with prefix 0 if num < 10
    url = 'https://www.cwa.gov.tw/rss/forecast/36_' + str(num).zfill(2) + '.xml'
    print(url)
    #get xml from url
    response = requests.get(url)
    #parse rss feed
    feed = feedparser.parse(response.content)

    tempdict = {}

    for entry in feed.entries:
        # entry.title includes '溫度'
        if '溫度' in entry.title:
        # 資料的格式 如下:
        # 金門縣04/02 今晚明晨 晴時多雲 溫度: 22 ~ 24 降雨機率: 10% (04/02 17:00發布)
            print(entry.title)
        #取出縣市名稱(前三個字)
            tempdict['county'] = entry.title[:3]

        #取出溫度的部分 使用空格切割後 取出 -7 與 -5 的部分
            tempdict['min'] = entry.title.split(' ')[-7]
            tempdict['max'] = entry.title.split(' ')[-5]
            print(tempdict['county'], tempdict['min'], tempdict['max'])
    
            county_list.append(tempdict)
        print("=======================================")

df_weather = pd.DataFrame(county_list)

##################################################
##################################################
#plot taiwan using matplotlib
import matplotlib.pyplot as plt

#merge df_taiwan and df_weather on df_taiwan.COUNTYNAME = df_weather.county 
df_taiwan = df_taiwan.merge(df_weather, left_on = 'COUNTYNAME', right_on = 'county')

#plot
fig, ax = plt.subplots(1, 1, figsize=(10, 10))
df_taiwan.boundary.plot(ax=ax)
df_taiwan.plot(column='max', ax=ax, legend=True)

plt.show()
##################################################

