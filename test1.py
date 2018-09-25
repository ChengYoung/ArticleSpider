import requests
from lxml import etree

url="https://bj.lianjia.com/ershoufang/"
response = requests.get(url)
#sss = etree.HTML(response)
#message = sss.xpath("//*[@id='leftContent']/ul/li[1]/div/div[1]/a/text()")[0]
print(response)