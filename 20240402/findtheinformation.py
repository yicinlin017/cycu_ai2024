#讀取目錄內的XML 將文字結構<title>的內容中找出其縣市 例如:基隆市 臺北市 新北市 桃園市 新竹市 新竹縣 苗栗縣 台中市 南投縣 彰化縣 雲林縣 嘉義縣 嘉義市 臺南市 高雄市 屏東縣 設定為縣市欄位
#然後再找出文字結構<descripion>內容需有 04/02 晚上溫度 字樣的內容找出 例如:04/02 晚上 溫度:22 ~ 27 設定為溫度欄位
#將縣市欄位及溫度欄位的內容打印出來
import os
import re
from xml.etree import ElementTree

# 讀取目錄內的XML檔案
for file_name in os.listdir():
    if file_name.endswith('.xml'):
        # 解析XML檔案
        tree = ElementTree.parse(file_name)
        root = tree.getroot()
        
        # 找到所有的<item>元素
        for item in root.findall('channel/item'):
            title = item.find('title').text
            description = item.find('description').text
            
            # 檢查是否為04/02晚上的描述
            if '04/02 晚上 溫度' in description:
                # 使用正則表達式找到溫度
                match = re.search(r'04/02 晚上 溫度 (\d+)', description)
                if match:
                    temperature = match.group(1)
                    # 打印縣市和溫度
                    print('縣市:', title)
                    print('04/02 晚上溫度:', temperature)
                    print()