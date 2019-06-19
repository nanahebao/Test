from  project.bikes.test_cases.conf import *
import  unittest
class TestBikes(unittest.TestCase):
    '''
    def test_nextday(self):
        carnos={
            2002,
            70000,
            80000,
            90000,
            4822591,
            20046,
            2001,
            2003,
            1993,
            7687231,
            90001,
            678901235
        }
        for carno in  carnos:
            with t3.open_writer(partition="dt=20171222", create_partition=True) as writer:
                records = [[2, carno, None, '1', 30.6426143646, 114.212059021, 27001, None, '2017-12-20 09:20:38', 0, None,
                    '2017-12-11 20:37:51', '2017-12-18 22:00:27', 0, 'wt3nqfq', ' 武汉市', 'JH91_W', '2700101709070311',
                    '20171222']
                   ]
                writer.write(records)
'''
    def test_zrActive(self):
        with t2.open_writer(partition="dt=20171222", create_partition=True) as writer:
            records = [['t_order7', 2, 3187, 11983637, 80000, '2017-12-22 20:54:03', 1, 39.990197, 116.313852, 1,
            '2017-12-21 20:57:03', 39.9908409, 116.3079544, -18013, 0, 0, 180, 1, 0.05, 100, 1, '武汉市',
            '武汉大学', '2017', '12', '18', '51', '武汉大学', '1', '武汉市', '100''20171222']
                           ]
            writer.write(records)  #27个小时内有订单
        with t1.open_writer(partition="dt=20171222", create_partition=True) as writer:
            records = [[12, 80000, 1, 1, 11080, 'silence', 99, None, 38.0605734592, 114.4531328668, None, None,
                        '2017-11-21 00:00:05', '2017-11-21 00:00:06', '20171222']
                       ]
            writer.write(records)  # 是否运维
        with t4.open_writer(partition="dt=20171222", create_partition=True) as writer:
            records = [
                ['t_order7', 678362081, 3187, 11983637, 80000, '2017-12-22 20:54:03', 1, 39.990197, 116.313852, 1,
                 '2017-12-21 20:57:03', 39.9908409, 116.3079544, -18013, 0, 0, 180, 1, 0.05, 100, 1, '武汉市', '武汉',
                 '武汉大学', 1, 0, '20171221']
                ]
            writer.write(records)  # hg
        with t5.open_writer(partition="dt=20171222", create_partition=True) as writer:
            records = [[80000, '2017-12-22 20:54:03', 11001, 2, 'CK593', '20171221']]
            writer.write(records)  # station


if __name__ == '__main__':
    #unittest.main()
    #print(__name__.__doc__)
    suite = unittest.TestSuite()
    #test_lowPowerNum1 test_lowPowerNum11 test_lowPowerTrend_1
    #test_slienceNum1 test_slienceNum11 test_slienceTrend_1  test_indentifyNum1 test_indentifyTrend_1
    #test_troubleNum1 test_troubleTrend_1 test_recoveryNum1 test_recoveryTrend_1
    tests = [TestBikes("test_zrActive")]
    suite.addTests(tests)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
