print('Hello World')

#https://news.pts.org.tw/xml/newsfeed.xml
import requests
import feedparser

# RSS 網址
url = "https://news.pts.org.tw/xml/newsfeed.xml"

# 發送 GET 請求
response = requests.get(url)

# 解析 RSS feed
feed = feedparser.parse(response.content)

# 找到所有的標題並列印
for entry in feed.entries:
    print(entry.title)
    #印出 Summary
    print(entry.summary)

    #印出區隔線
    print("="*50)
    #檢查檔案是否有匈牙利，有的話則儲存成Excel檔 可讀取的格式
    #放在使用者的桌面
    #檔案名稱為news.csv
    #檔案內容為標題、摘要、連結
    #檔案格式為utf-8
    #檔案內容以逗號分隔
    if "匈牙利" in entry.title:
        import os
        import csv
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        with open(desktop + "\\news.csv", "w", newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["標題", "摘要", "連結"])
            writer.writerow([entry.title, entry.summary, entry.link])
        print("已儲存成 news.csv 檔案")
        



