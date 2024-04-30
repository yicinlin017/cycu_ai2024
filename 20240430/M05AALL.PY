#CSV檔案合併方法為接續下一列
#將/workspaces/cycu_ai2024/20240430內有包涵M05A的CSV檔案合併成一個CSV檔案
#欄位為時間、地點1、地點2、車種、單一車輛計算車速、交通量

import pandas as pd
import os

path = "/workspaces/cycu_ai2024/20240430"
files = os.listdir(path)
dfs = []
for file in files:
    if "M05A" in file:
        df = pd.read_csv(f"{path}/{file}")
        df.columns = ["時間", "地點1", "地點2", "車種", "單一車輛計算車速", "交通量"]
        dfs.append(df)
df = pd.concat(dfs)
df.to_csv(f"{path}/TDCS_M05A.csv")
print(df)
