#CSV檔案合併方法為接續下一列
#將/workspaces/cycu_ai2024/20240430內有包涵M03A的CSV檔案合併成一個CSV檔案

import pandas as pd
import os

path = "/workspaces/cycu_ai2024/20240430"
files = os.listdir(path)
dfs = []
for file in files:
    if "M03A" in file:
        df = pd.read_csv(f"{path}/{file}")
        df.columns = ["時間", "地點", "方向", "車種", "交通量"]
        df["方向"] = df["方向"].replace({"N": 1, "S": 0})
        df = df.pivot_table(index=["時間", "地點", "方向", "車種", "交通量"])
        dfs.append(df)
df = pd.concat(dfs)
df.to_csv(f"{path}/TDCS_M03A.csv")
print(df)

