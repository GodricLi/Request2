# _*_ coding=utf-8 _*_

import requests


import requests
from lxml import etree

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
}
res = requests.get('http://news.baidu.com/tech', headers=headers)
html = etree.HTML(res.text)
data = html.xpath("//ul[@class='ulist mix-ulist']/li/a/text()")
data_store = {}
for i in data:
    data_store[data.index(i)]=i

print(data_store)