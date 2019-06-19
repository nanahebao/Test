# encoding=utf-8

from project.abtest.test_cases.conf import ip, path
from lib.request_process import HttpRequest
from lib.redis_req import GetRedis
from lib.data_process import to_json
import unittest
import sys

rq = HttpRequest(ip)
rds = GetRedis()


class TestGroup(unittest.TestCase):
    def test_time_invalid(self):
        """
        Description of case
        :the test time is not right
        :50 is end
        :51 not start
        it is useful for all kinds of data
        """
        print(self.test_time_invalid.__doc__)
        ids = ['50', '51']
        keys = ['10000000', '1000000A', "10000100", "10000201", "10004509", "1000250A", "10004502", "10000101"]
        for test_id in ids:
            for key in keys:
                data = {'test_id': test_id, 'key': key}
                rs = rq.http_request(path, json=data)
                print(rs.content, rs.status_code, rs.json())
                assert rs.status_code == 200
                if test_id == '50':
                    assert rs.json()['code'] == -202
                    assert rs.json()['msg'] == 'TEST END!'
                else:
                    assert rs.json()['code'] == -201
                    assert rs.json()['msg'] == 'TEST NOT START!'

    def test_input_lost(self):
        """
        Description of case
        :input params lost test_id,or key,or input null
        :return para error
        :include 3 groups of test data
        """
        print(self.test_input_lost.__doc__)

        datas = [{}, {'test_id': '21'}, {'key': '10000000'}]
        for data in datas:
            rs = rq.http_request(path, json=data)
            print(rs.content, rs.status_code, rs.json())
            assert rs.status_code == 200
            assert rs.json()['code'] == -2
            assert rs.json()['msg'] == 'PARA ERROR!'

    def test_len_exceed(self):
        """
        Description of case
        :input params with longer length
        :return para error
        :include 3 groups of test data
        """
        print(self.test_len_exceed.__doc__)
        param_ex = 'hello,world!this is a test to try a long str,which is exceeded 128,' \
                   'hello,world!this is a test to try a long str,which is bigger  '
        param_eq = 'hello,world!this is a test to try a long str,which is equal to 128,' \
                   'hello,world!this is a test to try a long str,which is equalto'
        param_ls = 'hello,world!this is a test to try a long str,which is short 128,' \
                   'hello,world!this is a test to try a long str,which is shorter'
        print('------', len(param_ex))
        print('------', len(param_eq))
        print('------', len(param_ls))
        datas = [{'test_id': param_ex, 'key': '10000000'},
                 {'test_id': '21', 'key': param_ex},
                 {'test_id': param_eq, 'key': '10000000'},
                 {'test_id': '21', 'key': param_eq},
                 {'test_id': param_ls, 'key': '10000000'},
                 {'test_id': '21', 'key': param_ls}
                 ]
        for data in datas:
            rs = rq.http_request(path, json=data)
            print(rs.content, rs.status_code, rs.json())
            assert rs.status_code == 200
            if data['test_id'] in [param_ex, param_eq, param_ls]:
                assert rs.json()['code'] == -2
                assert rs.json()['msg'] == 'PARA ERROR!'
            elif data['key'] == param_ex:
                assert rs.json()['code'] == -2
                assert rs.json()['msg'] == 'PARA ERROR!'
            else:
                assert rs.json()['code'] == 0
                assert rs.json()['msg'] == 'SUCCESS!'
                assert rs.json()['data']['group'] == ''

    def test_id_invalid(self):
        """
        Description of case
        :input params with test_id which is invalid
        :return para error
        :include 9 groups of test data
        """
        print(self.test_input_lost.__doc__)
        ids = ['null', None, ' ', '', 123, not int, 'test123', [], {}]
        for id in ids:
            data = {'test_id': id,
                    'key': '10000000'}
            rs = rq.http_request(path, json=data)
            #print(rs.content, rs.status_code, rs.json())
            assert rs.status_code == 200
            assert rs.json()['code'] == -2
            assert rs.json()['msg'] == 'PARA ERROR!'

    def test_key_invalid(self):
        """
        Description of case
        :input params with key which is invalid
        :return para error or group is ''
        :include 9 groups of test data
        """
        print(self.test_input_lost.__doc__)
        keys = ['null', None, ' ', '', 123, not int, 'notexist', [], {}]
        for key in keys:
            data = {'test_id': '21',
                    'key': key}
            rs = rq.http_request(path, json=data)
            print(rs.content, rs.status_code, rs.json())
            assert rs.status_code == 200
            #assert rs.json()['code'] == -2
            #assert rs.json()['msg'] == 'PARA ERROR!'

            if key in ['null', 'notexist',' ']:
                assert rs.json()['code'] == 0
                assert rs.json()['msg'] == 'SUCCESS!'
                assert rs.json()['data']['group'] == ''

            else:
                assert rs.json()['code'] == -2
                assert rs.json()['msg'] == 'PARA ERROR!'

            #assert rs.status_code == 200
            #assert rs.json()['code'] == -2
            #assert rs.json()['msg'] == 'PARA ERROR!'

    def test_21_1(self):
        """
        Description of case
        :21 is a test which need type 2 and city(11001,19001)
        :10000000 is a uid whic in city(11001) and end with '0'
        :return the group id, default is 0
        """
        print(self.test_21_1.__doc__)
        data = {'test_id': '21',
                'key': '10000000'}
        rs = rq.http_request(path, json=data)
        assert rs.status_code == 200
        assert rs.json()['msg'] == 'SUCCESS!'
        assert rs.json()['code'] == 0
        assert rs.json()['data']['group'] == '101'
        # print(type(rds.get_hgetall('U_T_G_UID:10000000')), rds.get_hgetall('U_T_G_UID:10000000'))
        rds_values = rds.get_hgetall('U_T_G_UID:10000000')

        assert rds_values[b'21'] == b'101'

    def test_21_2(self):
        """
        Description of case
        :21 is a test which need type 2 and city(11001,19001)
        :10000001 is a uid which in city(11001) and end with '1'
        :return the group id, default is 0
        """
        print(self.test_21_2.__doc__)
        data = {'test_id': '21',
                'key': '10000001'}
        rs = rq.http_request(path, json=data)
        # print(rs.json())
        # print(rs.url)
        assert rs.status_code == 200
        assert rs.json()['msg'] == 'SUCCESS!'
        assert rs.json()['code'] == 0
        assert rs.json()['data']['group'] == '0'
        # print(type(rds.get_hgetall('U_T_G_UID:10000001')), rds.get_hgetall('U_T_G_UID:10000001'))
        rds_alues = rds.get_hgetall('U_T_G_UID:10000001')

        assert rds_alues[b'21'] == b'0'

    def test_21_3(self):
        """
        Description of case
        :21 is a test which need type 2 and city(11001,19001)
        :1000000A is a uid which in city(11001) and end with 'A'
        :not fit for req of type 2
        :return the group id is ''
        """
        print(self.test_21_3.__doc__)
        data = {'test_id': '21',
                'key': '1000000A'}
        rs = rq.http_request(path, json=data)
        # print(rs.json())
        # print(rs.url)
        assert rs.status_code == 200
        assert rs.json()['msg'] == 'SUCCESS!'
        assert rs.json()['code'] == 0
        assert rs.json()['data']['group'] == ''
        # print(type(rds.get_hgetall('U_T_G_UID:1000000A')), rds.get_hgetall('U_T_G_UID:1000000A'))
        rds_values = rds.get_hgetall('U_T_G_UID:1000000A')
        assert rds_values[b'21'] == b''

    def test_22(self):
        """
        Description of case
        :22 is a test which need type 2 and source(1,2,3)
        :10002301 is a uid which end with 1 but source is -1,so return group ''
        :10004302 is a uid which end with 2 ,so directly return group ''
        :10000000 is a uid which end with 0 and source is 1,so return valid group '12435' which is analyzed by mod
        :the number of test data group is 3
        """
        print(self.test_22.__doc__)
        keys = ['10000000', '10004302', '10002301']
        for key in keys:
            data = {'test_id': '22',
                    'key': key}
            rs = rq.http_request(path, json=data)

            # print('params:%s'%data, rs.json())
            # print(rs.url)
            assert rs.status_code == 200
            assert rs.json()['msg'] == 'SUCCESS!'
            assert rs.json()['code'] == 0
            if key == '10000000':
                assert rs.json()['data']['group'] == '12435'
                # print(type(rds.get_hgetall('U_T_G_UID:%s'%key)), rds.get_hgetall('U_T_G_UID:%s'%key))
                rds_values = rds.get_hgetall('U_T_G_UID:%s'%key)
                assert rds_values[b'22'] == b'12435'
            else:
                assert rs.json()['data']['group'] == ''
                # print(type(rds.get_hgetall('U_T_G_UID:%s' % key)), rds.get_hgetall('U_T_G_UID:%s' % key))
                rds_alues = rds.get_hgetall('U_T_G_UID:%s' % key)
                assert rds_alues[b'22'] == b''

    def test_23(self):
        """
        Description of case
        :23 is a test which need type 2 and os(1,2)
        :10002300 is a uid which end with 0 but os is -1,so directly return group ''
        :10004302 is a uid which end with 2 and os is 2, still return group ''
        :1000000A is a uid which end with 1 and os is 1,so return valid group '0' which is analyzed by mod
        :the number of test data group is 3
        """
        print(self.test_23.__doc__)
        keys = ['10002300', '10004302', '10001301']
        for key in keys:
            data = {'test_id': '23',
                    'key': key}
            rs = rq.http_request(path, json=data)
            # print(rs.json())
            # print(rs.url)
            assert rs.status_code == 200
            assert rs.json()['msg'] == 'SUCCESS!'
            assert rs.json()['code'] == 0
            if key == '10001301':
                assert rs.json()['data']['group'] == '0'
                # print(type(rds.get_hgetall('U_T_G_UID:%s' % key)), rds.get_hgetall('U_T_G_UID:%s' % key))
                rds_alues = rds.get_hgetall('U_T_G_UID:%s' % key)
                assert rds_alues[b'23'] == b'0'
            else:
                assert rs.json()['data']['group'] == ''
                # print(type(rds.get_hgetall('U_T_G_UID:%s' % key)), rds.get_hgetall('U_T_G_UID:%s' % key))
                rds_alues = rds.get_hgetall('U_T_G_UID:%s' % key)
                assert rds_alues[b'23'] == b''


    def test_24(self):
        """
        Description of case
        :24 is a test which need type 1 and city(11001,19001)
        :10000000 is a uid which end with 0 and city is 11001,so return group ''
        :10000001 is a uid which end with 1 and city is 11001,so return group ''
        :1000000A is a uid which end with A and city is 11001,so return valid group '0' which is analyzed by mod
        :the number of test data group is 3
        """
        print(self.test_24.__doc__)
        keys = ['10000000', '10000001', '1000000A']
        for key in keys:
            data = {'test_id': '24',
                    'key': key}

            rs = rq.http_request(path, json=data)
            # print(rs.json())
            # print(rs.url)
            assert rs.status_code == 200
            assert rs.json()['msg'] == 'SUCCESS!'
            assert rs.json()['code'] == 0
            if key == '1000000A':
                assert rs.json()['data']['group'] == '204'
                # print(type(rds.get_hgetall('U_T_G_UID:%s' % key)), rds.get_hgetall('U_T_G_UID:%s' % key))
                rds_alues = rds.get_hgetall('U_T_G_UID:%s' % key)
                assert rds_alues[b'24'] == b'204'

            else:
                assert rs.json()['data']['group'] == ''
                # print(type(rds.get_hgetall('U_T_G_UID:%s' % key)), rds.get_hgetall('U_T_G_UID:%s' % key))
                rds_alues = rds.get_hgetall('U_T_G_UID:%s' % key)
                assert rds_alues[b'24'] == b''

    def test_25(self):
        """
        Description of case
        :25 is a test which need type 1 and source(1,2)
        :10004102 is a uid which end with 1 and source is 2,so return valid group '0' which is analyzed by mod
        :10004602 is a uid which end with 1 but source is 3,so return group ''
        :10003907 is a uid which end with 7 ,doesn't care source, directly return group ''
        :the number of test data group is 3
        """
        print(self.test_25.__doc__)
        keys = ['10004102', '10004602', '10003907']
        for key in keys:
            data = {'test_id': '25',
                    'key': key}
            rs = rq.http_request(path, json=data)
            # print(rs.json())
            # print(rs.url)
            assert rs.status_code == 200
            assert rs.json()['msg'] == 'SUCCESS!'
            assert rs.json()['code'] == 0
            if key == '10004102':
                assert rs.json()['data']['group'] == '0'
                # print(type(rds.get_hgetall('U_T_G_UID:%s' % key)), rds.get_hgetall('U_T_G_UID:%s' % key))
                rds_alues = rds.get_hgetall('U_T_G_UID:%s' % key)
                assert rds_alues[b'25'] == b'0'
            else:
                assert rs.json()['data']['group'] == ''
                # print(type(rds.get_hgetall('U_T_G_UID:%s' % key)), rds.get_hgetall('U_T_G_UID:%s' % key))
                rds_alues = rds.get_hgetall('U_T_G_UID:%s' % key)
                assert rds_alues[b'25'] == b''

    def test_26(self):
        """
        Description of case
        :26 is a test which need type 1 and os(1,2)
        :10004702 is a uid which end with 2 and os is -1,so return group ''
        :10004709 is a uid which end with 9 and os is -1,so return group ''
        :10003907 is a uid which end with 9 and os is 1,so return valid group '0' which is analyzed by mod
        :the number of test data group is 3
        """
        print(self.test_26.__doc__)
        keys = ['10004702', '10004709', '10003907']
        for key in keys:
            data = {'test_id': '26',
                    'key': key}
            rs = rq.http_request(path, json=data)
            # print(rs.json())
            # print(rs.url)
            assert rs.status_code == 200
            assert rs.json()['msg'] == 'SUCCESS!'
            assert rs.json()['code'] == 0
            if key == '10004702':
                assert rs.json()['data']['group'] == ''
                # print(type(rds.get_hgetall('U_T_G_UID:%s' % key)), rds.get_hgetall('U_T_G_UID:%s' % key))
                rds_alues = rds.get_hgetall('U_T_G_UID:%s' % key)
                assert rds_alues[b'26'] == b''
            elif key == '10004709':
                assert rs.json()['data']['group'] == ''
                # print(type(rds.get_hgetall('U_T_G_UID:%s' % key)), rds.get_hgetall('U_T_G_UID:%s' % key))
                rds_alues = rds.get_hgetall('U_T_G_UID:%s' % key)
                assert rds_alues[b'26'] == b''
            else:
                assert rs.json()['data']['group'] == '0'
                # print(type(rds.get_hgetall('U_T_G_UID:%s' % key)), rds.get_hgetall('U_T_G_UID:%s' % key))
                rds_alues = rds.get_hgetall('U_T_G_UID:%s' % key)
                assert rds_alues[b'26'] == b'0'

    def test_whitelist(self):
        """
        Description of case
        :all keys in the white list
        :check every test to get the group id which white list in
        :the number of test data group is 6*6(36)
        """
        print(self.test_whitelist.__doc__)
        keys = ["10000100", "10000201", "10004509", "1000250A", "10004502", "10000101"]
        test_ids = ["21", "22", "23", "24", "25", "26"]
        for key in keys:
            for test_id in test_ids:

                data = {'test_id': test_id,
                        'key': key}
                rs = rq.http_request(path, json=data)
                # print(rs.json())
                # print(rs.url)
                assert rs.status_code == 200
                assert rs.json()['msg'] == 'SUCCESS!'
                assert rs.json()['code'] == 0
                # print(type(rds.get_hgetall('U_T_G_UID:%s' % key)), rds.get_hgetall('U_T_G_UID:%s' % key))
                rds_alues = rds.get_hgetall('U_T_G_UID:%s' % key)
                if test_id == '21':
                    assert rs.json()['data']['group'] == '101'
                    # print(type(rds.get_hgetall('U_T_G_UID:%s' % key)), rds.get_hgetall('U_T_G_UID:%s' % key))
                    rds_alues = rds.get_hgetall('U_T_G_UID:%s' % key)
                    assert rds_alues[b'21'] == b'101'
                elif key == '22':
                    assert rs.json()['data']['group'] == '12345'
                    # print(type(rds.get_hgetall('U_T_G_UID:%s' % key)), rds.get_hgetall('U_T_G_UID:%s' % key))
                    rds_alues = rds.get_hgetall('U_T_G_UID:%s' % key)
                    assert rds_alues[b'26'] == b'12345'

                elif key == '23':
                    assert rs.json()['data']['group'] == '101'
                    # print(type(rds.get_hgetall('U_T_G_UID:%s' % key)), rds.get_hgetall('U_T_G_UID:%s' % key))
                    rds_alues = rds.get_hgetall('U_T_G_UID:%s' % key)
                    assert rds_alues[b'26'] == b'101'
                elif key == '24':
                    assert rs.json()['data']['group'] == '204'
                    # print(type(rds.get_hgetall('U_T_G_UID:%s' % key)), rds.get_hgetall('U_T_G_UID:%s' % key))
                    rds_alues = rds.get_hgetall('U_T_G_UID:%s' % key)
                    assert rds_alues[b'26'] == b'204'
                elif key == '25':
                    assert rs.json()['data']['group'] == '201'
                    # print(type(rds.get_hgetall('U_T_G_UID:%s' % key)), rds.get_hgetall('U_T_G_UID:%s' % key))
                    rds_alues = rds.get_hgetall('U_T_G_UID:%s' % key)
                    assert rds_alues[b'26'] == b'201'
                elif key == '26':
                    assert rs.json()['data']['group'] == '201'
                    # print(type(rds.get_hgetall('U_T_G_UID:%s' % key)), rds.get_hgetall('U_T_G_UID:%s' % key))
                    rds_alues = rds.get_hgetall('U_T_G_UID:%s' % key)
                    assert rds_alues[b'26'] == b'201'



if __name__ == '__main__':
    #unittest.main()
    #print(__name__.__doc__)
    suite = unittest.TestSuite()

    tests = [TestGroup("test_21_2")]
    suite.addTests(tests)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
