#讀取/workspaces/cycu_ai2024/file/runline.csv

import pandas as pd
df = pd.read_csv('/workspaces/cycu_ai2024/file/runline.csv')
#第一行是欄位名稱
#去除 順序、日期和水位欄位
df = df.drop(['順序','日期','水位'], axis=1)

#將資料繪畫成動畫xy圖 
#根據資料順序排序 
#欄位i=1的為x座標 y座標為x座標欄位的下一個欄位

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.ticker as ticker

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'r-')
texts = []

def init():
    ax.set_xlim(530.9, 531.6)
    ax.set_ylim(530.9, 531.6)
    ax.set_aspect('equal')  # 設定寬度和高度相等
    ax.grid(True)  # 添加格線
    ax.xaxis.set_major_locator(ticker.MultipleLocator(0.1))  # 設定 x 軸格線的間距為 0.1
    ax.yaxis.set_major_locator(ticker.MultipleLocator(0.1))  # 設定 y 軸格線的間距為 0.1
    return ln,

def update(frame):
    xdata.append(df.iloc[frame,0])
    ydata.append(df.iloc[frame,1])
    ln.set_data(xdata, ydata)
    return ln,

def onclick(event):
    ix, iy = event.xdata, event.ydata
    for i in range(len(xdata)):
        if abs(xdata[i]-ix) < 0.05 and abs(ydata[i]-iy) < 0.05:  # 如果點擊位置與資料點的距離小於一個閾值
            texts.append(ax.text(xdata[i], ydata[i], f'({xdata[i]}, {ydata[i]})', fontsize=8))
    plt.draw()

cid = fig.canvas.mpl_connect('button_press_event', onclick)

ani = animation.FuncAnimation(fig, update, frames=range(0, len(df)), init_func=init, blit=True)
# 將動畫轉換為 HTML 字串
ani_html = ani.to_jshtml()

# 將 HTML 字串寫入到一個 HTML 文件中
with open('/workspaces/cycu_ai2024/file/20240515.html', 'w') as f:
    f.write(ani_html)