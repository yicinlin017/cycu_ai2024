#讀取/workspaces/cycu_ai2024/20240409/地震活動彙整_638482848123192524.csv
#其解碼為big5
#讀取欄位在資料夾的第二列
#讀取欄位為地震時間 經度 緯度 規模 之資料並顯示出來
#並將資料存成earthquake.csv放在資料夾中
import pandas as pd
df = pd.read_csv('/workspaces/cycu_ai2024/20240409/地震活動彙整_638482848123192524.csv', encoding='Big5', header=1)
df = df[['地震時間', '經度', '緯度', '規模']]
df.to_csv('/workspaces/cycu_ai2024/20240409/earthquake.csv', index=False)
#將地震時間欄位資料只取用2024/4/3以後的資料 並顯示出來
df['地震時間'] = pd.to_datetime(df['地震時間'])
df = df[df['地震時間'] > '2024-04-03']
print(df)
#使用folium 根據資料內的經度緯度座標將其標示在地圖上 下載到本機桌面上
import folium
m = folium.Map(location=[23.5, 121], zoom_start=7)
for i in range(len(df)):
    folium.Marker([df.iloc[i]['緯度'], df.iloc[i]['經度']]).add_to(m)
m.save('/workspaces/cycu_ai2024/20240409/map.html')
