import requests
import re
from lxml import etree

url = "https://www.autohome.com.cn/news/201809/923007.html#pvareaid=102624"
response = requests.get(url).content.decode("gb2312")
tree = etree.HTML(response)
#ArticleTitle = re.findall(r'[\u4e00-\u9fa5]+',tree.xpath("//div[@class='article-details']/h1/text()")[0])
ArticleTitle = tree.xpath("//div[@class='article-details']/h1/text()")[0].strip()
ArticleMarks = tree.xpath("//div[@class='marks']/a/text()")
# for molecule in tree.xpath("//li[@data-artidanchor]"):
#     url = "https:" + molecule.xpath("a/@href")[0]
#     title = molecule.xpath("a/h3/text()")
#     print(url)
#     print(title)
#     count = count + 1
print(ArticleTitle)
print(ArticleMarks)
