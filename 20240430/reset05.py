#讀取/workspaces/cycu_ai2024/20240430/TDCS_M05A.csv
#將第一欄位完全刪除 只留下時間,地點1,地點2,車種,單一車輛計算車速,交通量欄位
#將每列資料依照時間欄位照時間排序
#重新儲存在/workspaces/cycu_ai2024/20240430/TDCS_M05ARESET.csv
#打印

import pandas as pd
data = pd.read_csv('/workspaces/cycu_ai2024/20240430/TDCS_M05A.csv')
data = data.drop(columns=['Unnamed: 0'])
data = data[['時間','地點1','地點2','車種','單一車輛計算車速','交通量']]
data = data.sort_values(by='時間')
data.to_csv('/workspaces/cycu_ai2024/20240430/TDCS_M05ARESET.csv',index=False)
print(data)
