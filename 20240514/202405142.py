#讀取/workspaces/cycu_ai2024/20240514/0429180000.csv
#x軸為里程欄位，y軸為小客車交通量欄位 加入擬合線
#打印
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

df = pd.read_csv("20240514/0429180000.csv")

# 將 x 和 y 的值組合成一個 DataFrame，並刪除重複的行
data = pd.DataFrame({'x': df["里程"], 'y': df["小客車交通量"]}).drop_duplicates(subset='x', keep='first')

# 再次將 x 和 y 的值分別提取出來
x = data['x'].values
y = data['y'].values

# 創建插值函數
f = interp1d(x, y, kind='cubic')

# 生成新的 x 值
xnew = np.linspace(min(x), max(x), num=1000, endpoint=True)

# 使用插值函數計算對應的 y 值
ynew = f(xnew)

plt.scatter(x, y)
plt.plot(xnew, ynew, color="red")

# 儲存圖形
plt.savefig("20240514/0429180000.png")

# 顯示圖形
plt.show()

