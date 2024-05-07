#讀取/workspaces/cycu_ai2024/20240430/TDCS_M05ARESET.csv
#將欄位取名稱  第一欄位為時間 第二欄位為地點1 第三欄位為地點2 第四欄位為車種 第五欄位為車速 第六欄位為交通量
#車種內 31為小客車、32為小貨車、41為大客車、42為大貨車、5為聯結車
#欄位顯示改為時間、地點1、地點2、小客車交通量、小貨車交通量、大客車交通量、大貨車交通量、聯結車交通量、小客車車速、小貨車車速、大客車車速、大貨車車速、聯結車車速


import pandas as pd
data = pd.read_csv('/workspaces/cycu_ai2024/20240430/TDCS_M05ARESET.csv')
data = data.rename(columns={'時間':'時間','地點1':'地點1','地點2':'地點2','車種':'車種','單一車輛計算車速':'車速','交通量':'交通量'})
data['小客車交通量'] = data['交通量'][data['車種']==31]
data['小貨車交通量'] = data['交通量'][data['車種']==32]
data['大客車交通量'] = data['交通量'][data['車種']==41]
data['大貨車交通量'] = data['交通量'][data['車種']==42]
data['聯結車交通量'] = data['交通量'][data['車種']==5]
data['小客車車速'] = data['車速'][data['車種']==31]
data['小貨車車速'] = data['車速'][data['車種']==32]
data['大客車車速'] = data['車速'][data['車種']==41]
data['大貨車車速'] = data['車速'][data['車種']==42]
data['聯結車車速'] = data['車速'][data['車種']==5]
data = data[['時間','地點1','地點2','小客車交通量','小貨車交通量','大客車交通量','大貨車交通量','聯結車交通量','小客車車速','小貨車車速','大客車車速','大貨車車速','聯結車車速']]


#再將時間欄位及地點欄位相同的資料合併
data = data.groupby(['時間','地點1','地點2']).sum()

#將時間欄位以每五分鐘為單位 改為順序編號 
#例如 2024/04/29 00:00 改為1 2024/04/29 00:05 改為2 2024/04/29 00:10 改為3 以回歸分析的方式處理
data = data.reset_index()
data['時間'] = pd.to_datetime(data['時間'])
data['時間'] = data['時間'].rank(method='dense')
data['時間'] = data['時間'].astype(int)
print(data)

#去除地點2欄位
data = data.drop(columns=['地點2'])
print(data)
#地點一欄位只保留第一個字元+第二個字元為01的資料 其他資料不要 
#將地點1資料改為第4個字元~第7個字元
#data['地點1'] = data['地點1'].str[3:7]
#data = data[data['地點1']=='01']
#print(data)
#將資料輸出成CSV檔案
data.to_csv('/workspaces/cycu_ai2024/20240507/RESETLASTM05A.csv',index=False)



