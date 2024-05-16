#讀取/workspaces/cycu_ai2024/file/runline.csv
#將欄位名稱設定為第一行
#只留下日期、水位欄位

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.ticker as ticker

df = pd.read_csv('/workspaces/cycu_ai2024/file/runline.csv')
lag = 2
df['水位_lag'] = df['水位'].shift(lag)

fig, ax = plt.subplots()

line, = ax.plot([], [], 'r-')

def init():
    ax.set_xlim(df['水位'].min(), df['水位'].max())
    ax.set_ylim(df['水位_lag'].min(), df['水位_lag'].max())
    ax.set_aspect('equal')  # 設定寬度和高度相等
    ax.grid(True)  # 添加格線
    ax.xaxis.set_major_locator(ticker.MultipleLocator(0.1))  # 設定 x 軸格線的間距為 0.1
    ax.yaxis.set_major_locator(ticker.MultipleLocator(0.1))  # 設定 y 軸格線的間距為 0.1
    return line,

def update(i):
    line.set_data(df['水位_lag'].iloc[:i], df['水位'].iloc[:i])
    return line,

ani = animation.FuncAnimation(fig, update, frames=range(len(df)), init_func=init, blit=True)

# 將動畫轉換為 HTML 字串
ani_html = ani.to_jshtml()

# 將 HTML 字串寫入到一個 HTML 文件中
with open('/workspaces/cycu_ai2024/file/20240515.html', 'w') as f:
    f.write(ani_html)


