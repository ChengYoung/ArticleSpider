# -*- coding: utf-8 -*-
import requests
import re
from lxml import etree

class CatchArticles:
    def __init__(self):
        self.base_url = "https://www.autohome.com.cn/all"
        self.Attributions_dict={}

    def selectAttributions(self):
        response = requests.get(self.base_url).text
        tree = etree.HTML(response)
        message = tree.xpath("//div[@id='ulNav']/ul/li[2]/a/text()")
        print(message)

if __name__=="__main__":
    demo = CatchArticles()
    demo.selectAttributions()
