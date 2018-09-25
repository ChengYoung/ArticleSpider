import requests
import re
from lxml import etree

url = "https://www.autohome.com.cn/all"
response = requests.get(url).content.decode("gb2312")
tree = etree.HTML(response)
message = tree.xpath("//div[@id='ulNav']/ul/li[2]/a/text()")[0]
print(message)