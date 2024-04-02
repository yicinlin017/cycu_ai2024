#https://www.cwa.gov.tw/V8/C/S/eservice/rss.html

import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

# 網頁的URL
url = 'https://www.cwa.gov.tw/V8/C/S/eservice/rss.html'

# 獲取網頁的HTML內容
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# 找到所有的XML連結
links = soup.find_all('a', href=True)
xml_links = [urljoin(url, link['href']) for link in links if link['href'].endswith('.xml')]

# 打印xml_links
print(xml_links)

# 下載每個XML檔案
for xml_link in xml_links:
    xml_response = requests.get(xml_link)
    file_name = os.path.basename(xml_link)
    
    # 將下載的內容寫入到本地檔案
    with open(file_name, 'wb') as file:
        file.write(xml_response.content)