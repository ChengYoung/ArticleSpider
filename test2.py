import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
# 第三方 SMTP 服务
mail_host= "smtp.163.com"  #设置服务器
mail_user= os.environ.get("MAIL_USERNAME")    #用户名
mail_pass= os.environ.get("MAIL_PASSWORD")   #口令 
 
 
sender = os.environ.get("MAIL_USERNAME")
receivers = ['qiancheng123456@live.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 
message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = os.environ.get("MAIL_USERNAME")
message['To'] =  'qiancheng123456@live.com'
 
subject = '任务已经完成'
message['Subject'] = Header(subject, 'utf-8')
 
 
try:
    smtpObj = smtplib.SMTP() 
    smtpObj.connect(mail_host, 25)
    smtpObj.login(mail_user,mail_pass) 
    smtpObj.sendmail(sender, receivers, message.as_string())
    print ("邮件发送成功")
except smtplib.SMTPException as e:
    print ("Error: 无法发送邮件",e)
