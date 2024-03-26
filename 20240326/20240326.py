url = '''https://tisvcloud.freeway.gov.tw/history/TDCS/M04A/20240325/00/'''
#爬蟲網址路徑最後面的 /00/代表的是00點到01點的資料 /01/代表的是01點到02點的資料 以此類推
#所以我們可以利用迴圈來產生網址 例如:https://tisvcloud.freeway.gov.tw/history/TDCS/M03A/20240325/00/、https://tisvcloud.freeway.gov.tw/history/TDCS/M03A/20240325/01/、https://tisvcloud.freeway.gov.tw/history/TDCS/M03A/20240325/02/
#如果要爬取2024年03月25日00點到2024年03月25日23點的資料 可以利用迴圈來產生網址 例如:https://tisvcloud.freeway.gov.tw/history/TDCS/M03A/20240325/00/、https://tisvcloud.freeway.gov.tw/history/TDCS/M03A/20240325/01/、https://tisvcloud.freeway.gov.tw/history/TDCS/M03A/20240325/02/、https://tisvcloud.freeway.gov.tw/history/TDCS/M03A/20240325/03/....https://tisvcloud.freeway.gov.tw/history/TDCS/M03A/20240325/23/
import requests
filename ='''TDCS_M04A_20240325_000000.csv'''
#fliename 最後面的數字是小時 分鐘 與秒 ，例如000000代表00:00:00 、 000500代表00:05:00
#所以我們可以利用迴圈來產生檔名
#如果每五分鐘一筆資料 利用迴圈產生檔名 例如:TDCS_M03A_20240325_00000.CSV、TDCS_M03A_20240325_000500.CSV、TDCS_M03A_20240325_001000.CSV
import time
for i in range(24):
    for j in range(0,60,5):
        url = '''https://tisvcloud.freeway.gov.tw/history/TDCS/M04A/20240325/%02d/%02d/'''%(i,j)
        filename ='''TDCS_M04A_20240325_%02d%02d00.csv'''%(i,j)
        res = requests.get(url)
        with open(filename, 'w') as f:
            f.write(res.text)
        time.sleep(5)
        print(url)
        print(filename)
        print('=====================')
        