#!/usr/bin/env python 
import urllib
from bs4 import BeautifulSoup

url_1 = urllib.urlopen("http://shop73453528.taobao.com/?q=&searcy_type=item&s_from=newHeader&source=&ssid=s5-e&search=y&initiative_id=itemz_20130602")
url_2 = urllib.urlopen("http://xiaofeiniu.taobao.com/index.htm?spm=2013.1.w5002-900001746.2.l6TT0G")
content_1 = url_1.read()
content_2 = url_2.read()
soup_1 = BeautifulSoup(content_1)

for title in soup_1.find_all("dd"):
    print title.get_text()

#file_1 = open('xvtaitai', 'w') 
#file_2 = open('xiaofeiyang', 'w')
#file_1.write(content_1)
#file_2.write(content_2) 

