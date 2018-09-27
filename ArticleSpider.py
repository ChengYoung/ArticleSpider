# -*- coding: utf-8 -*-
import requests
import re
from lxml import etree

class CatchArticles:
    def __init__(self):
        self.base_url = "https://www.autohome.com.cn/all"
        self.Attributions_dict={}

    def selectAttributions(self):
        response = requests.get(self.base_url).content.decode("gb2312")
        tree = etree.HTML(response)
        for element in tree.xpath("//li[@class='nav-item ' or @class='nav-item current']"):
            AttributionName = element.xpath("a/text()")[0]
            AttributionURL = "https:" + element.xpath("a/@href")[0]
            self.Attributions_dict[AttributionName]=AttributionURL
        print(self.Attributions_dict)
    
    def selectArticles(self):
        response = requests.get(self.base_url).content.decode("gb2312")
        tree = etree.HTML(response)
        page = int(tree.xpath("//div[@id='channelPage']/a[last()-1]/text()")[0])
        CurrentPage = 1
        while(CurrentPage < page):
            response = requests.get(self.base_url+"/CurrentPage/#liststart").content.decode("gb2312")
            tree = etree.HTML(response)
            for element in tree.xpath("//li[@data-artidanchor]"):
                ArticleURL = "https:" + element.xpath("a/@href")[0]
                response = requests.get(ArticleURL).content.decode("gb2312")
                tree = etree.HTML(response)
                ArticleTitle = tree.xpath("//div[@class='article-details']/h1/text()")[0]
                ArticleMarks = tree.xpath("//div[@class='marks']/a/text()")



                    

if __name__=="__main__":
    demo = CatchArticles()
    demo.selectAttributions()
    demo.selectArticles()
