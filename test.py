import requests
import re
from lxml import etree
import pymysql

# connect = pymysql.Connect(
#     host='localhost',
#     port=3306,
#     user="root",
#     passwd="774841525",
#     db="learn",
#     charset="utf8"
# )
# cursor = connect.cursor()
# sql = "INSERT INTO learn.car_articles(articles_title,articles_marks,articles_content) VALUES(%s,%s,%s)"
# url = "https://www.autohome.com.cn/news/201810/923676.html#pvareaid=102624"
# response = requests.get(url).content.decode("gb2312",errors="ignore")
# tree = etree.HTML(response)
# try:
#     ArticleTitle = ','.join(tree.xpath("//div[@class='article-details']/h1/text()")[0].split())
# except IndexError:
#     print('indexError')
# else:
#     ArticleMarks = "|".join(tree.xpath("//div[@class='marks']/a/text()"))
#     sss = "".join(tree.xpath("//div[@class='details']/p[not(@align='center')]/text() | //div[@class='details']/p/a/text() | //div[@class='details']/p/strong/span/text()"))
#     ArticleContent = ''.join(sss.split())
#     cursor.execute(sql,(ArticleTitle,ArticleMarks,ArticleContent))
#     connect.commit()
#     # print(ArticleTitle)
#     # print(ArticleMarks)
#     # print(ArticleContent)
# # sss = re.sub(r'\s','',ArticleContent)
# # for molecule in tree.xpath("//li[@data-artidanchor]"):
# #     url = "https:" + molecule.xpath("a/@href")[0]
# #     title = molecule.xpath("a/h3/text()")
# #     print(url)
# #     print(title)
# #     count = count + 1
# cursor.close()
# connect.close()
# print("down")

url = "https://www.autohome.com.cn/news/"

response = requests.get(url)
response.encoding = "gb2312"
response1 = response.text()
print(response1)
