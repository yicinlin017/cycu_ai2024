#讀取目錄內的XML 將文字結構<title>的內容中找出其所屬縣市 例如:基隆市 臺北市 新北市 桃園市 新竹市 新竹縣 苗栗縣 台中市 南投縣 彰化縣 雲林縣 嘉義縣 嘉義市 臺南市 高雄市 屏東縣 
#然後再將文字結構<descripion>內容的 04/02 晚上溫度為多少 例如:04/02 晚上 溫度:22 ~ 27
#將這些資訊打印出來

import os
from xml.etree import ElementTree

# 讀取目錄內的XML檔案
for file_name in os.listdir():
    if file_name.endswith('.xml'):
        # 解析XML檔案
        tree = ElementTree.parse(file_name)
        root = tree.getroot()
        
        # 找到所有的item
        for item in root.findall('.//item'):
            # 找到title和description
            title = item.find('title').text
            description = item.find('description').text
            
            # 打印縣市和溫度
            print(title, description)
