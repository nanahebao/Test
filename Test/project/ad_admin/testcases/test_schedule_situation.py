import unittest

from lib.HTMLTestRunner import HTMLTestRunner
from lib.request_process import HttpRequest
from lib.send_email import SendMail
from project.ad_admin.conf import ip

rq=HttpRequest(ip)
path='/api/schedule/day_situation'
class TestScheduleSituation(unittest.TestCase):
    def test_day_situation(self):
        data={'r_id':'8789',
              'dt':'20180213'}
        rs=rq.http_request(path,'GET',params=data)
        print(rs.content,rs.status_code,rs.json())


if __name__=='__main__':
    suite=unittest.TestSuite()
    tests=[TestScheduleSituation("test_ad")]
    suite.addTests(tests)
    #sendmail=Send_email()
    sendmail=SendMail()
    with open('//Users//ln//Downloads//Test//project//ad_admin//testcases//reports//AdHTMLReport.html', 'w')as f:
        runner = HTMLTestRunner(stream=f,
                                title='Ad_admin Test Report',
                                description='generated by HTMLTestRunner.',
                                verbosity=2
                                )
        runner.run(suite)
        #sendmail.send_em("294714025@qq.com","payxsjuipioobihi","liuna468@sina.com")
        sendmail.send("294714025@qq.com","payxsjuipioobihi","294714025@qq.com")