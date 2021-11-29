import os
import time
import sys
from email import mime

from scipy.optimize._trustregion_constr.tests import test_report

from common.Logs import Log
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import email.mime.text
import traceback
from common import Consts

my_sender = '18801053303@163.com'

my_passwd = 'MWCVYSTIUQOIYCDW'  # 授权码

my_user = '18801053303@163.com'
my_smtp_host = 'smtp.163.com'  # 163的smtp服务器地址

file = os.path.basename(sys.argv[0])
print(file)
log = Log(file)
logger = log.Logger


def mail():
    try:
        # 开始打包邮件
        msg = MIMEMultipart()
        msg['From'] = my_sender  # 设置发件人
        msg['To'] = my_user  # 设置收件人
        msg['Subject'] = 'AutoDL接口测试报告'

        result_body = Consts.RESULT_LIST
        len_result = len(result_body)
        T = 0
        F = 0
        Error = 0
        for r in result_body:
            if r == 'pass':
                T = T + 1
            if r == 'fail':
                F = F + 1
        if T + F == len_result:
            pass
        else:
            Error = len_result - F - T

        rate = (float(T) / float(len_result) * 100)
        # 下面是正文内容
        content = 'Hi，all\n本次接口自动化报告如下: \n' + '执行时间：' + time.ctime() + '\n' + '执行脚本数为：' + str(
            len_result) + ', ' + '成功数为：' + str(T) + ', ' + '失败数为：' + str(F) + ', ' + '异常数：' + str(
            Error) + '。\n ' + '通过率为： ' + str(rate) + '% '
        text = email.mime.text.MIMEText(content, 'html', 'utf-8')
        # 随便找的html文件，后面两个参数是告诉程序以html格式和utf-8字符
        msg.attach(text)

        # 下面是各种类型的附件了
        file_msg = MIMEApplication(
            open('../report/reporthtml/index.html', 'rb').read())
        file_msg.add_header('Content-Disposition', 'attachment', filename='test_report.html')
        msg.attach(file_msg)

        server = smtplib.SMTP(my_smtp_host, 25)  # smtp服务器端口默认是25
        # server.set_debuglevel(1)# 设置为调试模式，就是在会话过程中会有输出信息
        server.login(my_sender, my_passwd)
        server.sendmail(my_sender, [my_user], msg.as_string())
        server.quit()
        logger.info("邮件发送成功，详见邮件内容结果！")
    except Exception as e:
        print(e)
        logger.info("邮件发送失败，详见日志分析原因！", e)
