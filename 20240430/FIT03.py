#讀取/workspaces/cycu_ai2024/20240430/TDCS_M03A_20240429_000000.csv
#將欄位取名稱 第一欄位為時間 第二欄位為地點 第三欄位為方向 第四欄位為車種 第五欄位為交通量
#將第三欄位顯示為N的改為數字1 S的改為數字0

import pandas as pd

#車種內 31為小客車、32為小貨車、41為大客車、42為大貨車、5為聯結車
#欄位顯示改為時間、地點、方向、小客車、小貨車、大客車、大貨車、聯結車 ，其中小客車、小貨車、大客車、大貨車、聯結車的資料為對應之交通量
#將每五項資料存成一個資料 
#打印
df = pd.read_csv("/workspaces/cycu_ai2024/20240430/TDCS_M03A_20240429_000000.csv")
df.columns = ["時間", "地點", "方向", "車種", "交通量"]
df["方向"] = df["方向"].replace({"N": 1, "S": 0})
df = df.pivot_table(index=["時間", "地點", "方向"], columns="車種", values="交通量", aggfunc="sum")

print(df)
#儲存成/workspaces/cycu_ai2024/20240430/TDCS_M03A_20240429_0000001.csv
df.to_csv("/workspaces/cycu_ai2024/20240430/TDCS_M03A_20240429_0000001.csv")
