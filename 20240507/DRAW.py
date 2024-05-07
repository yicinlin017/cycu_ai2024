#讀取/workspaces/cycu_ai2024/20240507/RESETLASTM05A.csv
#將資料畫成4維圖 X為時間 Y為地點1 Z為小客車交通量 
#第四維度將小客車車速用顏色表示 0為白色 1~20為紫色 21~40為紅色 41~60為橘色 61~80為黃色 81以上為綠色
#將圖片輸出成PNG檔案

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors

data = pd.read_csv('/workspaces/cycu_ai2024/20240507/RESETLASTM05A.csv')
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = data['時間']
y = data['地點1']
z = data['小客車交通量']
c = data['小客車車速']
norm = mcolors.Normalize(vmin=0, vmax=100)
cmap = plt.cm.get_cmap('viridis')
sc = ax.scatter(x, y, z, c=c, cmap=cmap, norm=norm)
plt.colorbar(sc)
plt.savefig('/workspaces/cycu_ai2024/20240507/DRAW.png')

