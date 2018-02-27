# coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 参数配置
smtpserver = "smtp.qq.com"
port = 465
sender = "3437871062@qq.com"
psw = "tdcejfnutrascjee"
receiver = "1039020476@qq.com"

# ---添加附件内容---
# 定义一个容器
msg = MIMEMultipart()
msg['Subject'] = "ssp项目自动化测试报告"
msg['From'] = sender
msg['to'] = receiver

b = open("result.html", "r", encoding="utf-8")
mail_body = b.read()
b.close

z = open("text.html", "r", encoding="utf-8")
zhengwen_body = z.read()
z.close
# 添加正文内容到容器
body = MIMEText(zhengwen_body, 'html', 'utf-8')
msg.attach(body)
# 添加附件到容器
att = MIMEText(mail_body, "base64", "utf-8")
att["Content-Type"] = "application/octet-sream"
att["Content-Disposition"] = 'attachment;filename="ssp_test_report.html"'
msg.attach(att)

# 连接发送邮件
smtp = smtplib.SMTP_SSL(smtpserver, port)
smtp.login(sender, psw)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()
