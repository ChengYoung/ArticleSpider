# -*- coding: utf-8 -*-
import os
import requests
import re
import time
from lxml import etree
import pymysql
import smtplib
from email.mime.text import MIMEText
from email.header import Header

class CatchArticles:
    def __init__(self):
        self.base_url = "https://www.autohome.com.cn/news/"
        self.Attributions_dict={}
        self.connect = pymysql.Connect(
            host='localhost',
            port=3306,
            user="root",
            passwd="774841525",
            db="learn",
            charset="utf8"
        )
        self.cursor = self.connect.cursor()
        self.sql = "INSERT INTO learn.car_articles(articles_title,articles_marks,articles_content) VALUES(%s,%s,%s)"
        self.mail_host= "smtp.163.com"
        self.mail_user= os.environ.get("MAIL_USERNAME")
        self.mail_pass= os.environ.get("MAIL_PASSWORD")
        self.sender = os.environ.get("MAIL_USERNAME")
        self.receivers = ['774841525@qq.com']

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
        print(page)
        while(currentPage < page):
            try:
                response = requests.get(self.base_url+str(currentPage)+"/#liststart").content.decode("gb2312",errors="ignore")
            except:
                times = 1
                while(times<10 and response.status_code!=200):
                    time.sleep(3)
                    print("正在重新连接")
                    response = requests.get(self.base_url+str(currentPage)+"/#liststart").content.decode("gb2312",errors="ignore")
                    times = times + 1
                if response.status_code!=200:
                    continue
            tree = etree.HTML(response)
            for element in tree.xpath("//ul[@class='article']/li[not(@style)]"):
                ArticleURL = "https:" + element.xpath("a/@href")[0]
                try:
                    response = requests.get(ArticleURL).content.decode("gb2312",errors="ignore")
                except:
                    times = 1
                    while(times<10 and response.status_code!=200):
                        time.sleep(3)
                        print("正在重新连接")
                        response = requests.get(ArticleURL).content.decode("gb2312",errors="ignore")
                        times = times + 1
                    if response.status_code!=200:
                        continue
                tree = etree.HTML(response)
                try:
                    ArticleTitle = ",".join(tree.xpath("//div[@class='article-details']/h1/text()")[0].split())
                except:
                    continue
                else:
                    ArticleMarks = "".join(tree.xpath("//div[@class='marks']/a/text()"))
                    Temp = "".join(tree.xpath("//div[@class='details']/p[not(@align='center')]/text() | //div[@class='details']/p/a/text() | //div[@class='details']/p/strong/span/text()"))
                    ArticleContent = "".join(Temp.split())
                    self.cursor.execute(self.sql,[ArticleTitle,ArticleMarks,ArticleContent])
                    self.connect.commit()
            currentPage = currentPage + 1
            print("now,we are catching the " + str(currentPage) + " page")
            if currentPage % 50 == 0:
                time.sleep(1)
                print("sleep one second") 
        print("the job is over")
        self.cursor.close()
        self.connect.close()
        message = MIMEText('爬虫任务已经完成,请您查看数据库信息', 'plain', 'utf-8')
        message['From'] = os.environ.get("MAIL_USERNAME")
        message['To'] =  "774841525@qq.com"
        subject = '您的任务已经完成'
        message['Subject'] = Header(subject, 'utf-8')
        try:
            smtpObj = smtplib.SMTP_SSL() 
            smtpObj.connect(self.mail_host, 465)
            smtpObj.login(self.mail_user,self.mail_pass) 
            smtpObj.sendmail(self.sender, self.receivers, message.as_string())
            print ("邮件发送成功")
        except smtplib.SMTPException as e:
            print ("Error: 无法发送邮件",e)

if __name__=="__main__":
    demo = CatchArticles()
    #demo.selectAttributions()
    demo.selectArticles()
