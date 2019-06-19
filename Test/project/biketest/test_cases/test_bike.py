# encoding=utf-8

from project.biketest.test_cases.conf import *
from lib.request_process import HttpRequest
import unittest
import json
rq = HttpRequest(ip)
headers = {'Authorization': 'dc8b2e8ca1879cd850d05780045a60c9',
           "X-Trace-Id": "14444",
           "X-Trace-RpcId": "233"}
class TestBike(unittest.TestCase):
        def test_lowPowerNum1(self):
            datas = [{'level': 'society', 'zone_id': 'MI'}, {'level': 'city', 'zone_id': 29006}]
            for data in datas:
                rs=rq.http_request(get_lowPowernum_path,params=data,headers=headers)
                print(rs.json())
                assert rs.status_code==200
                assert rs.json()['msg']=='Success'
        def test_lowPowerTrend_1(self):
            datas=[{'level':'society','zone_id':'MI',"start_time":'2017-12-08',"end_time": '2017-12-09'},
                   {'level':'city','zone_id':29006,"start_time":'2017-12-08',"end_time": '2017-12-09'}]
            for data in datas:
                rs = rq.http_request(get_lowPowerTrend_path, params=data, headers=headers)
                print(rs.json())
                assert rs.status_code == 200
                assert rs.json()['msg'] == 'Success'


        def test_slienceNum1(self):
            datas = [{'level': 'society', 'zone_id': 'MI'}, {'level': 'city', 'zone_id': 29006}]
            for data in datas:
                rs = rq.http_request(get_slienceNum_path, params=data, headers=headers)
                print(rs.json())
                assert rs.status_code == 200
                assert rs.json()['msg'] == 'Success'
        def test_slienceTrend_1(self):
            datas=[{'level':'society','zone_id':'MI',"start_time":'2017-12-08',"end_time": '2017-12-09'},
                   {'level':'city','zone_id':29006,"start_time":'2017-12-08',"end_time": '2017-12-09'}]
            for data in datas:
                rs = rq.http_request(get_slienceTrend_path, params=data, headers=headers)
                print(rs.json())
                assert rs.status_code == 200
                assert rs.json()['msg'] == 'Success'

        def test_indentifyNum1(self):
            datas=[{'level':'society','zone_id':'MI'},{'level':'city','zone_id':29006}]
            for data in datas:
                rs = rq.http_request(get_identifyNum_path, params=data, headers=headers)
                print(rs.json())
                assert rs.status_code == 200
                assert rs.json()['msg'] == 'Success'
        def test_indentifyTrend_1(self):
            datas = [{'level': 'society', 'zone_id': 'cd_wenjiang24_w', "start_time": '2017-12-08', "end_time": '2017-12-08'},
                    {'level': 'city', 'zone_id': 33001, "start_time": '2017-12-09', "end_time": '2017-12-09'}]
            for data in datas:
                rs = rq.http_request(get_identifyTrend_path, params=data, headers=headers)
                print(rs.json())
                assert rs.status_code == 200
                assert rs.json()['msg'] == 'Success'

        def test_troubleNum1(self):
            datas = [{'level': 'society', 'zone_id': 'MI'}, {'level': 'city', 'zone_id': 29006}]
            for data in datas:
                rs = rq.http_request(get_troubleNum_path, params=data, headers=headers)
                print(rs.json())
                assert rs.status_code == 200
                assert rs.json()['msg'] == 'Success'


        def test_troubleTrend_1(self):
            datas = [{'level': 'society', 'zone_id': 'iejeif', "start_time": '2017-12-08', "end_time": '2017-12-08'},
            {'level': 'city', 'zone_id': 29006, "start_time": '2017-12-08', "end_time": '2017-12-08'}]
            for data in datas:
                rs = rq.http_request(get_troubleTrend_path, params=data, headers=headers)
                print(rs.json())



        def test_recoveryNum1(self):
            datas = [{'level': 'society', 'zone_id': 'MI'}, {'level': 'city', 'zone_id': 29006}]
            for data in datas:
                rs = rq.http_request(get_recoveryNum_path, params=data, headers=headers)
                print(rs.json())
                assert rs.status_code == 200
                assert rs.json()['msg'] == 'Success'
        def test_recoveryTrend_1(self):
            datas = [{'level': 'society', 'zone_id': 'MI', "start_time": '2017-12-08', "end_time": '2017-12-09'},
                         {'level': 'city', 'zone_id': 29006, "start_time": '2017-12-08', "end_time": '2017-12-09'}]
            for data in datas:
                rs = rq.http_request(get_recoverTrend_path, params=data, headers=headers)
                print(rs.json())
                assert rs.status_code == 200
                assert rs.json()['msg'] == 'Success'








        #level 或者zone_id不合法时候
        def test_level_invalid(self):
            levels = ['null', None, ' ', '', 123, 'test', [], {}]
            for level in levels:
                data = {'level': level,
                        'zone_id': 'MI'}
                rs = rq.http_request(get_slienceTrend_path, params=data,headers=headers)
                print(rs.json())
                # print(rs.content, rs.status_code, rs.json())
                assert rs.status_code == 200
                #assert rs.json()['code'] == -1
                #assert rs.json()['msg'] == '服务器错误'

        def test_zone_id_invalid(self):
            zone_ids=['null', None, ' ', '', 123, 76575454878676553354243221675564433,'test', [], {}]
            for zone_id in zone_ids:
                data={
                    'level':'city',
                    'zone_id':zone_id}
                rs = rq.http_request(get_lowPowernum_path, params=data, headers=headers)
                print(rs.json())
                # print(rs.content, rs.status_code, rs.json())
                assert rs.status_code == 200
                # assert rs.json()['code'] == -1
                # assert rs.json()['msg'] == '服务器错误'
#电子围栏时
        def test_lowPowerNum21(self):
            data={
                'level':'society',
                'zone_id':'bj_beishatandatun1,bj_fangzhaungsongjiazhuang2,'}
            rs = rq.http_request(get_lowPowernum_path, params=data, headers=headers)
            print(rs.json())

        def test_slienceNum21(self):
            data = {
                'level': 'society',
                'zone_id': 'bj_beishatandatun1,cd_wenjiang24_w,st_jinbihuayuan'}
            rs = rq.http_request(get_slienceNum_path, params=data, headers=headers)
            print(rs.json())
        def test_slienceNum231(self):
            data = {
                'level': 'city',
                'zone_id': '33001'}
            rs = rq.http_request(get_slienceNum_path, params=data, headers=headers)
            print(rs.json())

        def test_troubleNum21(self):

            data = {
                'level': 'society',
                'zone_id': 'bj_beishatandatun1,bj_fangzhaungsongjiazhuang2,cd_wenjiang24_w'}
            rs = rq.http_request(get_troubleNum_path, params=data, headers=headers)
            print(rs.json())
        def test_recoveryNum21(self):
            data = {
                'level': 'society',
                'zone_id': 'bj_beishatandatun1,bj_fangzhaungsongjiazhuang2,sz_qianhaiwan3'}
            rs = rq.http_request(get_recoveryNum_path, params=data, headers=headers)
            print(rs.json())
        def test_identifyNum21(self):
            data = {
                'level': 'society',
                'zone_id': 'bj_beishatandatun1,cd_wenjiang24_w,st_jinbihuayuan'}
            rs = rq.http_request(get_identifyNum_path, params=data, headers=headers)
            print(rs.json())
        def test_identifyNum21_1(self):
            data = {
                'level': 'city',
                'zone_id': '33001'}
            rs = rq.http_request(get_identifyNum_path, params=data, headers=headers)
            print(rs.json())
        def test_slienceTrend_21(self):
                data = {
                    'level': 'society',
#                    'zone_id': 'bj_beishatandatun1,bj_fangzhaungsongjiazhuang2,cd_wenjiang24_w',
                    'zone_id': 'bj_beishatandatun1,cd_wenjiang24_w,st_jinbihuayuan',
                    "start_time": '2017-12-12',
                    "end_time": '2017-12-13'}
                rs = rq.http_request(get_slienceTrend_path, params=data, headers=headers)
                print(rs.json())

#沉默车
        def test_slienceNum22(self):
            data = {
                'level': 'society',
                'zone_id': 'cd_wenjiang24_w'}
            rs = rq.http_request(get_slienceNum_path, params=data, headers=headers)
            print(rs.json())
#损坏车
        def test_troubleNum22(self):
            data = {
                'level': 'society',
                'zone_id': 'cd_wenjiang24_w'}
            rs = rq.http_request(get_troubleNum_path, params=data, headers=headers)
            print(rs.json())
#鉴定车
        def test_identifyNum22(self):
            data = {
                'level': 'society',
                'zone_id': 'st_jinbihuayuan'}
            rs = rq.http_request(get_identifyNum_path, params=data, headers=headers)
            print(rs.json())
#回收车
        def test_recoveryNum22(self):
            data = {
                'level': 'society',
                'zone_id': 'cd_wenjiang24_w'}
            rs = rq.http_request(get_recoveryNum_path, params=data, headers=headers)
            print(rs.json())
if __name__ == '__main__':
    #unittest.main()
    #print(__name__.__doc__)
    suite = unittest.TestSuite()
    #test_lowPowerNum1 test_lowPowerNum11 test_lowPowerTrend_1
    #test_slienceNum1 test_slienceNum11 test_slienceTrend_1  test_indentifyNum1 test_indentifyTrend_1
    #test_troubleNum1 test_troubleTrend_1 test_recoveryNum1 test_recoveryTrend_1
    tests = [TestBike("test_indentifyTrend_1")]
    suite.addTests(tests)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
