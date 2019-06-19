import unittest

from lib.request_process import HttpRequest
from project.ad_admin.conf import ip

rq=HttpRequest(ip)
path='/api/schedule/check_schedule'
class TestCheckSchedule(unittest.TestCase):
    def test_check_schedule(self):
        header={
            'content type':'application/json'
        }
        sche_params_ls={
            'dt':'',
            "adment_id":'',
            "smethod_id":'',
            "region_city":''
        }
        data={
            'r_id':'',
            'sche_params_ls':sche_params_ls
        }
        rs=rq.http_request(path,'post',params=data,header=header)
        print(rs.content,rs.status_code,rs.json())