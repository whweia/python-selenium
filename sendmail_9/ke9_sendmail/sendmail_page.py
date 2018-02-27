# coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
# 发送邮件函数


def send_mail(smtpserver, port, sender, psw, receiver):
    msg = MIMEMultipart()
    msg['Subject'] = "ssp项目自动化测试报告"
    msg['From'] = sender
    msg['to'] = receiver
# 通过os获取文件路径
    current_path = os.path.realpath(__file__)
    current_file_path = os.path.dirname(current_path)
    file_path = os.path.join(current_file_path, "result.html")

    b = open(file_path, "r", encoding="utf-8")
    mail_body = b.read()
    b.close

    current_path = os.path.realpath(__file__)
    current_file_path = os.path.dirname(current_path)
    file_path1 = os.path.join(current_file_path, "text.html")

    z = open(file_path1, "r", encoding="utf-8")
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

if __name__ == "__main__":

    send_mail("smtp.qq.com", 465, "3437871062@qq.com", "tdcejfnutrascjee", "1039020476@qq.com")
