#爬蟲網址https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/20240429/00/
#將爬蟲網址使用迴圈產生
#爬蟲網址https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/20240429/HH/ HH為00~23 共24個網址
#下載網址內所有csv檔案 儲存在/workspaces/cycu_ai2024/20240430

import os
import requests
from bs4 import BeautifulSoup

# 儲存路徑
save_path = "/workspaces/cycu_ai2024/20240430"

# 檢查儲存路徑是否存在
if not os.path.exists(save_path):
    os.makedirs(save_path)

# 爬蟲網址的基礎部分
base_url = "https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/20240429/"

# 對每個小時進行爬蟲
for hour in range(24):
    # 生成爬蟲網址
    url = base_url + f"{hour:02d}/"

    # 下載網址內所有csv檔案
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    for a in soup.find_all("a", href=True):
        if a["href"].endswith(".csv"):
            file_url = url + a["href"]
            file_name = os.path.basename(file_url)
            file_path = os.path.join(save_path, file_name)
            with open(file_path, "wb") as f:
                f.write(requests.get(file_url).content)
