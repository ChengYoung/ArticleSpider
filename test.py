import requests
import re
from lxml import etree

url = "https://www.autohome.com.cn/news/201810/923676.html#pvareaid=102624"
response = requests.get(url).content.decode("gb2312",errors="ignore")
tree = etree.HTML(response)
try:
    ArticleTitle = ','.join(tree.xpath("//div[@class='article-details']/h1/text()")[0].split())
except IndexError:
    print('indexError')
else:
    ArticleMarks = tree.xpath("//div[@class='marks']/a/text()")
    ArticleContent = "".join(tree.xpath("//div[@class='details']/p[not(@align='center')]/text() | //div[@class='details']/p/a/text() | //div[@class='details']/p/strong/span/text()"))
    sss = ''.join(ArticleContent.split())
    print(ArticleTitle)
    print(ArticleMarks)
    print(ArticleContent)
    print(sss)
# sss = re.sub(r'\s','',ArticleContent)
# for molecule in tree.xpath("//li[@data-artidanchor]"):
#     url = "https:" + molecule.xpath("a/@href")[0]
#     title = molecule.xpath("a/h3/text()")
#     print(url)
#     print(title)
#     count = count + 1

