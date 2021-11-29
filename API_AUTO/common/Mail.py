# coding: utf-8
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
from email.mime.text import MIMEText
import pathlib


def send_mail(username, passwd, recv, title, content, mail_host='smtp.163.com', port=25, file=None):
    '''
    发送邮件函数，默认使用163smtp
    :param username: 邮箱账号 xx@163.com
    :param passwd: 邮箱密码
    :param recv: 邮箱接收人地址，多个账号以逗号隔开
    :param title: 邮件标题
    :param content: 邮件内容
    :param mail_host: 邮箱服务器
    :param port: 端口号
    :return:
    '''
    if file:
        msg = MIMEMultipart()
        # 构建正文
        part_text = MIMEText(content)
        msg.attach(part_text)  # 把正文加到邮件体里面去

        # 构建邮件附件
        part_attach1 = MIMEApplication(open(file, 'rb').read())  # 打开附件
        part_attach1.add_header('Content-Disposition', 'attachment', filename=pathlib.Path(file).name)  # 为附件命名
        msg.attach(part_attach1)  # 添加附件
    else:
        msg = MIMEText(content)  # 邮件内容
    msg['Subject'] = title  # 邮件主题
    msg['From'] = username  # 发送者账号
    msg['To'] = recv  # 接收者账号列表
    smtp = smtplib.SMTP(mail_host, port=port)
    smtp.login(username, passwd)  # 登录
    smtp.sendmail(username, recv, msg.as_string())
    smtp.quit()


username = "18801053303@163.com"

passwd = "MWCVYSTIUQOIYCDW" #授权码

recv = "18801053303@163.com"

send_address = username
send_password = passwd  # 授权码登录
receive_address = recv
title = "SeeTaaS接口测试报告"
content = "Hi，你好！这封邮件是python发送的"
reportfilepath = '../report/reporthtml/index.html'
send_mail(send_address, send_password, receive_address, title, content, file=reportfilepath)
# send_mail(username, passwd, recv, title, content, file=attachfilepath)
# print('success')
