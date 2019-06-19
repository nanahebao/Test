import unittest

from lib.request_process import HttpRequest
from project.ad_admin.conf import ip

rq=HttpRequest(ip)
path='/api/schedule/get_adment_by_schedule'
header = {'content type': 'application/json'}
class TestGetAdment(unittest.TestCase):
    def test_get_adment(self):
        data={
            'r_id':'',
            'dt':'',
            'smethod_id':'',
            'carousel_id': '',
            'td_start_time': '',
            'td_end_time': '',
            'region_city_ls': '',
        }
        rs=rq.http_request(path,'post',params=data,header=header)
        print(rs.content,rs.status_code,rs.json())