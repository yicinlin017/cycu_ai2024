#讀取/workspaces/cycu_ai2024/file/runline.csv
#將欄位名稱設定為第一行
#只留下日期、水位欄位

import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

df = pd.read_csv('/workspaces/cycu_ai2024/file/runline.csv')
lag = 2
df['水位_lag'] = df['水位'].shift(lag)

fig, ax = plt.subplots()

line, = ax.plot([], [], 'o')

def init():
    ax.set_xlim(df['水位'].min(), df['水位'].max())
    ax.set_ylim(df['水位_lag'].min(), df['水位_lag'].max())
    return line,

def update(i):
    line.set_data(df['水位'].iloc[:i], df['水位_lag'].iloc[:i])
    return line,

ani = animation.FuncAnimation(fig, update, frames=range(len(df)), init_func=init, blit=True)

plt.show()

#儲存成gif
ani.save('/workspaces/cycu_ai2024/file/20240515TEAT.gif', writer='pillow', fps=1)