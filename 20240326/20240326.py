url = '''https://tisvcloud.freeway.gov.tw/history/TDCS/M04A/20240325/00/'''

import requests
filename ='''TDCS_M04A_20240325_000000.csv'''
#fliename 最後面的數字是小時 分鐘 與秒 ，例如000000代表00:00:00 、 000500代表00:05:00
#所以我們可以利用迴圈來產生檔名
#如果每五分鐘一筆資料 利用迴圈產生檔名 例如:TDCS_M03A_20240325_00000.CSV、TDCS_M03A_20240325_000500.CSV、TDCS_M03A_20240325_001000.CSV

for i in range(0,1):
    for j in range(0,60,5):
        filename = f'''TDCS_M04A_20240325_{str(i).zfill(2)}{str(j).zfill(2)}00.csv'''
        print(filename)
        url = f'''https://tisvcloud.freeway.gov.tw/history/TDCS/M04A/20240325/{str(i).zfill(2)}/{filename}'''
        print(url)
        response = requests.get(url)
        with open(filename, 'wb') as f:
            f.write(response.content)
            