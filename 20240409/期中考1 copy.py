#csv其解碼為UTF-8
#csv讀取欄位在資料夾的第二列 
import pandas as pd
import requests
from datetime import datetime

#爬蟲https://scweb.cwa.gov.tw/zh-tw/earthquake/data/#
# 下載CSV檔案
url = "https://scweb.cwa.gov.tw/zh-tw/earthquake/data/"
response = requests.get(url)
with open('/workspaces/cycu_ai2024/20240409/地震活動彙整_638482848123192524.csv', 'wb') as f:
   f.write(response.content)

 #讀取CSV檔案
df = pd.read_csv('/workspaces/cycu_ai2024/20240409/地震活動彙整_638482848123192524.csv', encoding='utf-8', header=1, error_bad_lines=False)

#篩選出地震時間2024/04/03到2024/04/09之間的資料
df['地震時間'] = pd.to_datetime(df['地震時間'])
df = df[(df['地震時間'] > '2024-04-03') & (df['地震時間'] <= '2024-04-09')]


# 將資料存成earthquake.csv放在資料夾中
df.to_csv('earthquake.csv', index=False)
import pandas as pd
import folium
from folium.plugins import TimestampedGeoJson
#讀取欄位為地震時間 經度 緯度 規模 位置之資料並顯示出來
df = pd.read_csv('/workspaces/cycu_ai2024/20240409/地震活動彙整_638482848123192524.csv', encoding='Big5', header=1)
df = df[['地震時間', '經度', '緯度', '規模', '位置']]

# 將 DataFrame 按照地震時間排序
df = df.sort_values('地震時間')

m = folium.Map(location=[23.5, 121], zoom_start=7)

features = []
for i in range(len(df)):
    feature = {
        'type': 'Feature',
        'geometry': {
            'type': 'Point',
            'coordinates': [df.iloc[i]['經度'], df.iloc[i]['緯度']]
        },
        'properties': {
            'time': df.iloc[i]['地震時間'].isoformat(),
            'popup': f"{df.iloc[i]['地震時間']} {df.iloc[i]['規模']}"
        }
    }
    features.append(feature)

TimestampedGeoJson({
    'type': 'FeatureCollection',
    'features': features
}).add_to(m)

m.save('/workspaces/cycu_ai2024/20240409/earthquake.html')