
import os, sys
import smtplib
import time
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

reportPath = os.path.join(os.getcwd(), 'report')  # 测试报告的路径
print(reportPath)
class SendMail(object):
    def __init__(self, recver=None):
        """接收邮件的人：list or tuple"""
        if recver is None:
            self.sendTo = ['liuna468@sina.com']  # 收件人这个参数，可以是list，或者tulp，以便发送给多人
        else:
            self.sendTo = recver

    def get_report(self):  # 该函数的作用是为了在测试报告的路径下找到最新的测试报告
        dirs = os.listdir(reportPath)
        dirs.sort()
        newreportname = dirs[-1]
        print('The new report name: {0}'.format(newreportname))
        return newreportname  # 返回的是测试报告的名字

    def take_messages(self):  # 该函数的目的是为了 准备发送邮件的的消息内容
        newreport = self.get_report()
        self.msg = MIMEMultipart()
        self.msg['Subject'] = '测试报告主题'  # 邮件的标题
        self.msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')

        with open(os.path.join(reportPath, newreport), 'rb') as f:
                        mailbody = f.read()  # 读取测试报告的内容
        html = MIMEText(mailbody, _subtype='html', _charset='utf-8')  # 将测试报告的内容放在 邮件的正文当中
        self.msg.attach(html)  # 将html附加在msg里

        # html附件    下面是将测试报告放在附件中发送
        att1 = MIMEText(mailbody, 'base64', 'gb2312')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename="AdHTMLReport.html"'
        self.msg.attach(att1)


    def send(self,user,pwd,to):
        self.take_messages()
        self.msg['from'] = user  # 发送邮件的人
        self.msg['pwd']=pwd
        self.msg['to'] = to

        try:
            smtp = smtplib.SMTP_SSL("smtp.qq.com", 465)
            smtp.login(self.msg['from'],self.msg['pwd'])
            smtp.sendmail(self.msg['from'], self.msg['to'], self.msg.as_string())  # 发送邮件
            smtp.quit()
            print("success")

        except smtplib.SMTPException as e:
            print("Falied,%s" % e)


if __name__ == '__main__':
    sendMail = SendMail()
    sendMail.get_report()
    sendMail.send("294714025@qq.com","payxsjuipioobihi","liuna468@sina.com")
    #sendMail.send()
