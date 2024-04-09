#爬蟲https://scweb.cwa.gov.tw/zh-tw/earthquake/data/#
#下載此網頁的CSV檔案 到/workspaces/cycu_ai2024/20240409/地震活動彙整_638482848123192524.csv
#讀取/workspaces/cycu_ai2024/20240409/地震活動彙整_638482848123192524.csv
#其解碼為big5
#讀取欄位在資料夾的第二列
#讀取欄位為地震時間 經度 緯度 規模 位置之資料並顯示出來
#並將資料存成earthquake.csv放在資料夾中


import pandas as pd
import folium
from folium.plugins import TimestampedGeoJson

df = pd.read_csv('/workspaces/cycu_ai2024/20240409/地震活動彙整_638482848123192524.csv', encoding='Big5', header=1)
df = df[['地震時間', '經度', '緯度', '規模']]

df['地震時間'] = pd.to_datetime(df['地震時間'])
df = df[df['地震時間'] > '2024-04-03']

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