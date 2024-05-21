#爬蟲https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/ 
#下載名稱為M05A_2024MMDD.tar.gz的檔案 
#MM只採用01 02 03 04 DD只採用01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31
#存儲在/workspaces/cycu_ai2024/20240521/imfotmatiom 資料夾下
import requests
import os
import time
import calendar

url = "https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/"
path = "/workspaces/cycu_ai2024/20240521/imfotmatiom"
for i in range(1, 5):
    _, days_in_month = calendar.monthrange(2024, i)
    for j in range(1, days_in_month + 1):
        if i < 10:
            month = "0" + str(i)
        else:
            month = str(i)
        if j < 10:
            day = "0" + str(j)
        else:
            day = str(j)
        file_name = "M05A_2024" + month + day + ".tar.gz"
        print(file_name)
        response = requests.get(url + month + day + ".tar.gz", timeout=60)
        print(response.status_code)
        with open(os.path.join(path, file_name), "wb") as f:
            f.write(response.content)
        time.sleep(1)
print("Download finish")