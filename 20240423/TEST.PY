#爬蟲網址https://tisvcloud.freeway.gov.tw/history/TDCS/M04A/20240416/00/
#下載網址內所有csv檔案 儲存在/workspaces/cycu_ai2024/20240423
import os
import requests
from bs4 import BeautifulSoup

# 爬蟲網址
url = "https://tisvcloud.freeway.gov.tw/history/TDCS/M04A/20240416/00/"

# 儲存目錄
save_dir = "/workspaces/cycu_ai2024/20240423"

# 創建儲存目錄
os.makedirs(save_dir, exist_ok=True)

# 獲取網頁內容
response = requests.get(url)
response.raise_for_status()  # 如果請求失敗，這將引發一個異常

# 解析網頁內容
soup = BeautifulSoup(response.content, "html.parser")

# 找到所有的 CSV 檔案鏈接
for link in soup.find_all("a"):
    if link.get("href").endswith(".csv"):
        csv_url = url + link.get("href")

        # 下載 CSV 檔案
        csv_response = requests.get(csv_url)
        csv_response.raise_for_status()  # 如果請求失敗，這將引發一個異常

        # 儲存 CSV 檔案
        with open(os.path.join(save_dir, link.get("href")), "wb") as f:
            f.write(csv_response.content)