# coding:utf-8
import smtplib
from email.mime.text import MIMEText

# 参数配置
smtpserver = "smtp.qq.com"
port = 465
sender = "3437871062@qq.com"
psw = ""  # QQ授权码
receiver = "1039020476@qq.com"

# 写信模板
body = '<pre><h1>测试报告，请查收`</h1></pre>'

msg = MIMEText(body, 'html', "utf-8")
msg['from'] = sender
msg['to'] = receiver
msg['subject'] = "这是自动化测试报告"

# 写信流程
smtp = smtplib.SMTP_SSL(smtpserver, port)
smtp.login(sender, psw)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()
