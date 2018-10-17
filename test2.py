import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
# 第三方 SMTP 服务
mail_host= "smtp.163.com"  #设置服务器
mail_user= os.environ.get("MAIL_USERNAME")    #用户名
mail_pass= os.environ.get("MAIL_PASSWORD")   #口令 
 
 
sender = os.environ.get("MAIL_USERNAME")
receivers = ['774841525@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 
message = MIMEText('爬虫任务已经完成', 'plain', 'utf-8')
message['From'] = os.environ.get("MAIL_USERNAME")
message['To'] =  '774841525@qq.com'
 
subject = '请您查收任务消息'
message['Subject'] = Header(subject, 'utf-8')
 
 
try:
    smtpObj = smtplib.SMTP_SSL() 
    smtpObj.connect(mail_host, 465)
    smtpObj.login(mail_user,mail_pass) 
    smtpObj.sendmail(sender, receivers, message.as_string())
    print ("邮件发送成功")
except smtplib.SMTPException as e:
    print ("Error: 无法发送邮件",e)
