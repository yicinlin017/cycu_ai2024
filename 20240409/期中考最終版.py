#爬蟲https://scweb.cwa.gov.tw/zh-tw/earthquake/data/#
#找出網頁中csv檔案並下載
#將csv存成地震活動彙整_638493320733748879.csv放在資料夾中
#讀取/workspaces/cycu_ai2024/20240409/地震活動彙整_638493320733748879.csv
import pandas as pd
import chardet

# 檢測檔案的編碼
with open('/workspaces/cycu_ai2024/20240409/地震活動彙整_638493320733748879.csv', 'rb') as f:
    result = chardet.detect(f.read())

# 使用檢測到的編碼來讀取檔案
df = pd.read_csv('/workspaces/cycu_ai2024/20240409/地震活動彙整_638493320733748879.csv', encoding=result['encoding'])

print(df)

df.columns = df.iloc[0]
df = df[2:]

print(df.columns)

#篩選欄位名稱為地震時間 介於2024/4/3 00:00:00~2024/4/9 23:59:59的資料 並顯示出來
df['地震時間'] = pd.to_datetime(df['地震時間'])
df = df[(df['地震時間'] >= '2024-04-03 00:00:00') & (df['地震時間'] <= '2024-04-09 23:59:59')]
print(df)

#將篩選後的資料存成earthquake.csv
df.to_csv('earthquake.csv', index=False)

#讀取earthquake.csv並顯示出來
df = pd.read_csv('earthquake.csv')
print(df)
# 將 DataFrame 按照地震時間排序
df = df.sort_values('地震時間')
print(df)

#將資料顯示在地圖上 隨著時間變化
import folium
from folium.plugins import TimestampedGeoJson

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
            'time': df.iloc[i]['地震時間'],
        'popup': f"{df.iloc[i]['地震時間']} {df.iloc[i]['規模']} {df.iloc[i]['位置']} {df.iloc[i]['深度']}"
        }
    }
    features.append(feature)

TimestampedGeoJson({
    'type': 'FeatureCollection',
    'features': features
}).add_to(m)

m.save('earthquake.html')