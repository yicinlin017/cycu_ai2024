import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 讀取/workspaces/cycu_ai2024/20240507/RESETLASTM05A.csv
import pandas as pd
data = pd.read_csv('/workspaces/cycu_ai2024/20240507/RESETLASTM05A.csv')

# 只取用時間、地點1、小客車交通量、小客車車速
data = data[['時間','地點1','小客車交通量','小客車車速']]

# 打印
print(data)

# 繪製3D圖 X軸為時間 Y軸為地點1 Z軸為小客車交通量
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_trisurf(data['時間'], data['地點1'], data['小客車交通量'])

# 在圖表中加入標題 11272006林意芹
plt.title('11272006林意芹')

# 儲存/workspaces/cycu_ai2024/20240514/3D.png
plt.savefig('/workspaces/cycu_ai2024/20240514/3D.png')