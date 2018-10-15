# -*- coding: utf-8 -*-
import requests
import re
from lxml import etree

class CatchArticles:
    def __init__(self):
        self.base_url = "https://www.autohome.com.cn/news/"
        self.Attributions_dict={}

    def selectAttributions(self):
        response = requests.get(self.base_url).content.decode("gb2312",errors="ignore")
        tree = etree.HTML(response)
        for element in tree.xpath("//li[@class='nav-item ' or @class='nav-item current']"):
            AttributionName = element.xpath("a/text()")[0]
            AttributionURL = "https:" + element.xpath("a/@href")[0]
            self.Attributions_dict[AttributionName]=AttributionURL
        print(self.Attributions_dict)
    
    def selectArticles(self):
        response = requests.get(self.base_url).content.decode("gb2312",errors="ignore")
        tree = etree.HTML(response)
        page = int(tree.xpath("//div[@id='channelPage']/a[last()-1]/text()")[0])
        currentPage = 1
        while(currentPage < 2):
            response = requests.get(self.base_url+str(currentPage)+"/#liststart").content.decode("gb2312",errors="ignore")
            tree = etree.HTML(response)
            for element in tree.xpath("//li[@data-artidanchor]"):
                ArticleURL = "https:" + element.xpath("a/@href")[0]
                response = requests.get(ArticleURL).content.decode("gb2312",errors="ignore")
                tree = etree.HTML(response)
                try:
                    ArticleTitle = ",".join(tree.xpath("//div[@class='article-details']/h1/text()")[0].split())
                except IndexError:
                    continue
                else:
                    ArticleMarks = tree.xpath("//div[@class='marks']/a/text()")
                    Temp = "".join(tree.xpath("//div[@class='details']/p[not(@align='center')]/text() | //div[@class='details']/p/a/text() | //div[@class='details']/p/strong/span/text()"))
                    ArticleContent = "".join(Temp.split())
            currentPage = currentPage + 1


                    

if __name__=="__main__":
    demo = CatchArticles()
    #demo.selectAttributions()
    demo.selectArticles()
