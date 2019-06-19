    import os

from  project.bikes.test_cases.conf import *
import  unittest
class TestBikes(unittest.TestCase):
    def test_addSilence(self):
        with t3.open_writer(partition="dt=20171221", create_partition=True) as writer:
            records = [[2, 20047, None, '1', 30.6426143646, 114.212059021, 27001, None, '2017-12-20 09:20:38', 0, None,
                        '2017-12-11 20:37:51', '2017-12-18 22:00:27', 0, 'wt3nqfq', '武汉市', 'JH91_W', '2700101709070311',
                        '20171221']
                       ]
            writer.write(records)  # 7天内有心跳
        with t2.open_writer(partition="dt=20171218", create_partition=True) as writer:
            records = [['t_order7', 2, 3187, 11983637, 20047, '2017-12-18 20:54:03', 1, 39.990197, 116.313852, 1,
            '2017-12-17 20:57:03', 39.9908409, 116.3079544, -18013, 0, 0, 180, 1, 0.05, 100, 1, '武汉市',
            '武汉大学', '2017', '12', '18', '51', '武汉大学', '1', '武汉市', '100''20171218']
                           ]
            writer.write(records)  #27个小时内有订单
        with t1.open_writer(partition="dt=20171218", create_partition=True) as writer:
            records = [[12, 20047, 1, 1, 11080, 'silence', 99, None, 38.0605734592, 114.4531328668, None, None,
                        '2017-11-21 00:00:05', '2017-11-21 00:00:06', '20171218']
                       ]
            writer.write(records)  # 是否运维
        with t4.open_writer(partition="dt=20171218", create_partition=True) as writer:
            records = [
                ['t_order7', 678362081, 3187, 11983637, 20047, '2017-12-18 20:54:03', 1, 39.990197, 116.313852, 1,
                 '2017-12-17 20:57:03', 39.9908409, 116.3079544, -18013, 0, 0, 180, 1, 0.05, 100, 1, '武汉市', '武汉',
                 '武汉大学', 1, 0, '20171218']
                ]
            writer.write(records)  # hg
        with t5.open_writer(partition="dt=20171218", create_partition=True) as writer:
            records = [[20047, '2017-12-18 20:54:03', 11001, 2, 'CK593', '20171218']]
            writer.write(records)  # station
    def test_addSilence2(self):#另一个城市的
        with t3.open_writer(partition="dt=20171221", create_partition=True) as writer:
            records = [[2, 87678, None, '1', 30.6426143646, 114.212059021, 27001, None, '2017-12-20 09:20:38', 0, None,
                        '2017-12-11 20:37:51', '2017-12-18 22:00:27', 0, 'wt3nqfq', '北京市', '北京古城八角外环', '2700101709070311',
                        '20171221']
                       ]
            writer.write(records)  # 7天内有心跳
        with t2.open_writer(partition="dt=20171218", create_partition=True) as writer:
            records = [['t_order7', 2, 3187, 11983637, 87678, '2017-12-18 20:54:03', 1, 39.990197, 116.313852, 1,
            '2017-12-17 20:57:03', 39.9908409, 116.3079544, -18013, 0, 0, 180, 1, 0.05, 100, 1, '武汉市',
            '武汉大学', '2017', '12', '18', '51', '武汉大学', '1', '武汉市', '100''20171218']
                           ]
            writer.write(records)  #27个小时内有订单
        with t1.open_writer(partition="dt=20171218", create_partition=True) as writer:
            records = [[12, 87678, 1, 1, 11080, 'silence', 99, None, 38.0605734592, 114.4531328668, None, None,
                        '2017-11-21 00:00:05', '2017-11-21 00:00:06', '20171218']
                       ]
            writer.write(records)  # 是否运维
        with t4.open_writer(partition="dt=20171218", create_partition=True) as writer:
            records = [
                ['t_order7', 678362081, 3187, 11983637, 87678, '2017-12-18 20:54:03', 1, 39.990197, 116.313852, 1,
                 '2017-12-17 20:57:03', 39.9908409, 116.3079544, -18013, 0, 0, 180, 1, 0.05, 100, 1, '武汉市', '武汉',
                 '武汉大学', 1, 0, '20171218']
                ]
            writer.write(records)  # hg
        with t5.open_writer(partition="dt=20171218", create_partition=True) as writer:
            records = [[87678, '2017-12-18 20:54:03', 11001, 2, 'CK593', '20171218']]
            writer.write(records)  # station
    def test_addSilence3(self):#武汉另一个围栏
        with t3.open_writer(partition="dt=20171221", create_partition=True) as writer:
            records = [[2, 377678, None, '1', 30.6426143646, 114.212059021, 27001, None, '2017-12-20 09:20:38', 0, None,
                        '2017-12-11 20:37:51', '2017-12-18 22:00:27', 0, 'wt3nqfq', '武汉市', '外环', '2700101709070311',
                        '20171221']
                       ]
            writer.write(records)  # 7天内有心跳
        with t2.open_writer(partition="dt=20171218", create_partition=True) as writer:
            records = [['t_order7', 2, 3187, 11983637, 377678, '2017-12-18 20:54:03', 1, 39.990197, 116.313852, 1,
            '2017-12-17 20:57:03', 39.9908409, 116.3079544, -18013, 0, 0, 180, 1, 0.05, 100, 1, '武汉市',
            '武汉大学', '2017', '12', '18', '51', '武汉大学', '1', '武汉市', '100''20171218']
                           ]
            writer.write(records)  #27个小时内有订单
        with t1.open_writer(partition="dt=20171218", create_partition=True) as writer:
            records = [[12, 377678, 1, 1, 11080, 'silence', 99, None, 38.0605734592, 114.4531328668, None, None,
                        '2017-11-21 00:00:05', '2017-11-21 00:00:06', '20171218']
                       ]
            writer.write(records)  # 是否运维
        with t4.open_writer(partition="dt=20171218", create_partition=True) as writer:
            records = [
                ['t_order7', 678362081, 3187, 11983637, 377678, '2017-12-18 20:54:03', 1, 39.990197, 116.313852, 1,
                 '2017-12-17 20:57:03', 39.9908409, 116.3079544, -18013, 0, 0, 180, 1, 0.05, 100, 1, '武汉市', '武汉',
                 '武汉大学', 1, 0, '20171218']
                ]
            writer.write(records)  # hg
        with t5.open_writer(partition="dt=20171218", create_partition=True) as writer:
            records = [[377678, '2017-12-18 20:54:03', 11001, 2, 'CK593', '20171218']]
            writer.write(records)  # station

    def test_continueSilence(self):
        with t3.open_writer(partition="dt=20171221", create_partition=True) as writer:
            records = [[2, 10000, None, '1', 30.6426143646, 114.212059021, 27001, None, '2017-12-20 09:20:38', 0, None,
                        '2017-12-11 20:37:51', '2017-12-18 22:00:27', 0, 'wt3nqfq', '武汉市', 'JH91_W', '2700101709070311',
                        '20171221']
                       ]
            writer.write(records)  # 7天内有心跳
        with t2.open_writer(partition="dt=20171216", create_partition=True) as writer:
            records = [['t_order7', 2, 3187, 11983637, 10000, '2017-12-16 20:54:03', 1, 39.990197, 116.313852, 1,
            '2017-12-17 20:57:03', 39.9908409, 116.3079544, -18013, 0, 0, 180, 1, 0.05, 100, 1, '武汉市',
            '武汉大学', '2017', '12', '18', '51', '武汉大学', '1', '武汉市', '100''20171216']
                           ]
            writer.write(records)  #27个小时内没有订单
        with t1.open_writer(partition="dt=20171216", create_partition=True) as writer:
            records = [[12, 10000, 1, 1, 11080, 'silence', 99, None, 38.0605734592, 114.4531328668, None, None,
                        '2017-11-21 00:00:05', '2017-11-21 00:00:06', '20171216']
                       ]
            writer.write(records)  # 是否运维
        with t4.open_writer(partition="dt=20171216", create_partition=True) as writer:
            records = [
                ['t_order7', 678362081, 3187, 11983637, 10000, '2017-12-16 20:54:03', 1, 39.990197, 116.313852, 1,
                 '2017-12-17 20:57:03', 39.9908409, 116.3079544, -18013, 0, 0, 180, 1, 0.05, 100, 1, '武汉市', '武汉',
                 '武汉大学', 1, 0, '20171216']
                ]
            writer.write(records)  # hg
        with t5.open_writer(partition="dt=20171216", create_partition=True) as writer:
            records = [[10000, '2017-12-16 20:54:03', 11001, 2, 'CK593', '20171216']]
            writer.write(records)  # station

    def test_continueActive(self):
        with t3.open_writer(partition="dt=20171221", create_partition=True) as writer:
            records = [[2, 30000, None, '1', 30.6426143646, 114.212059021, 27001, None, '2017-12-20 09:20:38', 0, None,
                        '2017-12-11 20:37:51', '2017-12-18 22:00:27', 0, 'wt3nqfq', '武汉市', 'JH91_W', '2700101709070311',
                        '20171221']
                       ]
            writer.write(records)  # 7天内有心跳
        with t2.open_writer(partition="dt=20171221", create_partition=True) as writer:
            records = [['t_order7', 2, 3187, 11983637, 30000, '2017-12-21 20:54:03', 1, 39.990197, 116.313852, 1,
            '2017-12-21 20:57:03', 39.9908409, 116.3079544, -18013, 0, 0, 180, 1, 0.05, 100, 1, '武汉市',
            '武汉大学', '2017', '12', '18', '51', '武汉大学', '1', '武汉市', '100''20171217']
                           ]
            writer.write(records)  #27个小时内有订单
        with t1.open_writer(partition="dt=20171221", create_partition=True) as writer:
            records = [[12, 30000, 1, 1, 11080, 'silence', 99, None, 38.0605734592, 114.4531328668, None, None,
                        '2017-11-21 00:00:05', '2017-11-21 00:00:06', '20171221']
                       ]
            writer.write(records)  # 是否运维
        with t4.open_writer(partition="dt=20171221", create_partition=True) as writer:
            records = [
                ['t_order7', 678362081, 3187, 11983637, 30000, '2017-12-21 20:54:03', 1, 39.990197, 116.313852, 1,
                 '2017-12-21 20:57:03', 39.9908409, 116.3079544, -18013, 0, 0, 180, 1, 0.05, 100, 1, '武汉市', '武汉',
                 '武汉大学', 1, 0, '20171221']
                ]
            writer.write(records)  # hg
        with t5.open_writer(partition="dt=20171221", create_partition=True) as writer:
            records = [[30000, '2017-12-21 20:54:03', 11001, 2, 'CK593', '20171217']]
            writer.write(records)  # station
    def test_noOrder1(self):#有心跳没订单
        with t3.open_writer(partition="dt=20171221", create_partition=True) as writer:
            records = [[2, 90001, None, '1', 30.6426143646, 114.212059021, 27001, None, '2017-12-20 09:20:38', 0, None,
                        '2017-12-11 20:37:51', '2017-12-18 22:00:27', 0, 'wt3nqfq', '武汉市', 'JH91_W', '2700101709070311',
                        '20171221']
                       ]
    def test_noOrder2(self):#没心跳没订单
        with t3.open_writer(partition="dt=20171221", create_partition=True) as writer:
            records = [[2, 55555, None, '1', 30.6426143646, 114.212059021, 27001, None, '2017-12-16 09:20:38', 0, None,
                        '2017-12-11 20:37:51', '2017-12-18 22:00:27', 0, 'wt3nqfq', '武汉市', 'JH91_W', '2700101709070311',
                        '20171221']
                       ]
    def test_noStation(self):
        with t3.open_writer(partition="dt=20171221", create_partition=True) as writer:
            records = [[2, 90002, None, '1', 30.6426143646, 114.212059021, 27001, None, '2017-12-20 09:20:38', 0, None,
                        '2017-12-11 20:37:51', '2017-12-18 22:00:27', 0, 'wt3nqfq', '武汉市', 'JH91_W', '2700101709070311',
                        '20171221']
                       ]
            writer.write(records)  # 7天内有新跳
    def test_zrActive(self):
        with t2.open_writer(partition="dt=20171221", create_partition=True) as writer:
            records = [['t_order7', 2, 3187, 11983637, 70001, '2017-12-21 20:54:03', 1, 39.990197, 116.313852, 1,
            '2017-12-21 20:57:03', 39.9908409, 116.3079544, -18013, 0, 0, 180, 1, 0.05, 100, 1, '武汉市',
            '武汉大学', '2017', '12', '18', '51', '武汉大学', '1', '武汉市', '100''20171221']
                           ]
            writer.write(records)  #27个小时内有订单
        with t1.open_writer(partition="dt=20171221", create_partition=True) as writer:
            records = [[12, 70001, 1, 1, 11080, 'silence', 99, None, 38.0605734592, 114.4531328668, None, None,
                        '2017-11-21 00:00:05', '2017-11-21 00:00:06', '20171221']
                       ]
            writer.write(records)  # 是否运维
        with t4.open_writer(partition="dt=20171221", create_partition=True) as writer:
            records = [
                ['t_order7', 678362081, 3187, 11983637, 70001, '2017-12-21 20:54:03', 1, 39.990197, 116.313852, 1,
                 '2017-12-21 20:57:03', 39.9908409, 116.3079544, -18013, 0, 0, 180, 1, 0.05, 100, 1, '武汉市', '武汉',
                 '武汉大学', 1, 0, '20171221']
                ]
            writer.write(records)  # hg
        with t5.open_writer(partition="dt=20171221", create_partition=True) as writer:
            records = [[70001, '2017-12-21 20:54:03', 11001, 2, 'CK593', '20171221']]
            writer.write(records)  # station

    def test_engineActive(self):
        with t2.open_writer(partition="dt=20171221", create_partition=True) as writer:
            records = [['t_order7', 2, 3187, 11983637, 70002, '2017-12-21 20:54:03', 1, 39.990197, 116.313852, 1,
            '2017-12-21 20:57:03', 39.9908409, 116.3079544, -18013, 0, 0, 180, 1, 0.05, 100, 1, '武汉市',
            '武汉大学', '2017', '12', '18', '51', '武汉大学', '1', '武汉市', '100''20171221']
                           ]
            writer.write(records)  #27个小时内有订单
        with t1.open_writer(partition="dt=20171221", create_partition=True) as writer:
            records = [[12, 70002, 5, 1, 11080, 'silence', 99, None, 38.0605734592, 114.4531328668, None, None,
                        '2017-11-21 00:00:05', '2017-11-21 00:00:06', '20171221']
                       ]
            writer.write(records)  # 是否运维
        with t4.open_writer(partition="dt=20171221", create_partition=True) as writer:
            records = [
                ['t_order7', 678362081, 3187, 11983637, 70002, '2017-12-21 20:54:03', 1, 39.990197, 116.313852, 1,
                 '2017-12-21 20:57:03', 39.9908409, 116.3079544, -18013, 0, 0, 180, 1, 0.05, 100, 1, '武汉市', '武汉',
                 '武汉大学', 1, 0, '20171221']
                ]
            writer.write(records)  # hg
        with t5.open_writer(partition="dt=20171221", create_partition=True) as writer:
            records = [[70002, '2017-12-21 20:54:03', 11001, 2, 'CK593', '20171221']]
            writer.write(records)  # station
    def test_noStation1(self): #新增沉默
        with t3.open_writer(partition="dt=20171221", create_partition=True) as writer:
            records = [[2, 90000, None, '1', 30.6426143646, 114.212059021, 27001, None, '2017-12-12 09:20:38', 0, None,
                        '2017-12-11 20:37:51', '2017-12-18 22:00:27', 0, 'wt3nqfq', '武汉市', 'JH91_W', '2700101709070311',
                        '20171221']
                       ]
            writer.write(records)  # 7天内无位置信息
        with t2.open_writer(partition="dt=20171218", create_partition=True) as writer:
            records = [['t_order7', 2, 3187, 11983637, 90000, '2017-12-18 20:54:03', 1, 39.990197, 116.313852, 1,
            '2017-12-17 20:57:03', 39.9908409, 116.3079544, -18013, 0, 0, 180, 1, 0.05, 100, 1, '武汉市',
            '武汉大学', '2017', '12', '18', '51', '武汉大学', '1', '武汉市', '100''20171218']
                           ]
            writer.write(records)  #27个小时内有订单
        with t1.open_writer(partition="dt=20171218", create_partition=True) as writer:
            records = [[12, 90000, 1, 1, 11080, 'silence', 99, None, 38.0605734592, 114.4531328668, None, None,
                        '2017-11-21 00:00:05', '2017-11-21 00:00:06', '20171218']
                       ]
            writer.write(records)  # 是否运维
        with t4.open_writer(partition="dt=20171218", create_partition=True) as writer:
            records = [
                ['t_order7', 678362081, 3187, 11983637, 90000, '2017-12-18 20:54:03', 1, 39.990197, 116.313852, 1,
                 '2017-12-17 20:57:03', 39.9908409, 116.3079544, -18013, 0, 0, 180, 1, 0.05, 100, 1, '武汉市', '武汉',
                 '武汉大学', 1, 0, '20171218']
                ]
            writer.write(records)  # hg
        with t5.open_writer(partition="dt=20171218", create_partition=True) as writer:
            records = [[90000, '2017-12-18 20:54:03', 11001, 2, 'CK593', '20171218']]
            writer.write(records)  # station
    def test_noStation2(self): #持续沉默
        with t3.open_writer(partition="dt=20171221", create_partition=True) as writer:
            records = [[2, 70002, None, '1', 30.6426143646, 114.212059021, 27001, None, '2017-12-12 09:20:38', 0, None,
                        '2017-12-11 20:37:51', '2017-12-18 22:00:27', 0, 'wt3nqfq', '武汉市', 'JH91_W', '2700101709070311',
                        '20171221']
                       ]
            writer.write(records)  # 7天内有心跳
        with t2.open_writer(partition="dt=20171216", create_partition=True) as writer:
            records = [['t_order7', 2, 3187, 11983637, 70002, '2017-12-16 20:54:03', 1, 39.990197, 116.313852, 1,
            '2017-12-17 20:57:03', 39.9908409, 116.3079544, -18013, 0, 0, 180, 1, 0.05, 100, 1, '武汉市',
            '武汉大学', '2017', '12', '18', '51', '武汉大学', '1', '武汉市', '100''20171216']
                           ]
            writer.write(records)  #27个小时内没有订单
        with t1.open_writer(partition="dt=20171216", create_partition=True) as writer:
            records = [[12, 70002, 1, 1, 11080, 'silence', 99, None, 38.0605734592, 114.4531328668, None, None,
                        '2017-11-21 00:00:05', '2017-11-21 00:00:06', '20171216']
                       ]
            writer.write(records)  # 是否运维
        with t4.open_writer(partition="dt=20171216", create_partition=True) as writer:
            records = [
                ['t_order7', 678362081, 3187, 11983637, 70002, '2017-12-16 20:54:03', 1, 39.990197, 116.313852, 1,
                 '2017-12-17 20:57:03', 39.9908409, 116.3079544, -18013, 0, 0, 180, 1, 0.05, 100, 1, '武汉市', '武汉',
                 '武汉大学', 1, 0, '20171216']
                ]
            writer.write(records)  # hg
        with t5.open_writer(partition="dt=20171216", create_partition=True) as writer:
            records = [[70002, '2017-12-16 20:54:03', 11001, 2, 'CK593', '20171216']]
            writer.write(records)  # station
    def test_noOrder3(self): #无心跳
        with t3.open_writer(partition="dt=20171221", create_partition=True) as writer:
            records = [[2, 678901235, None, '1', 30.6426143646, 114.212059021, 27001, None, '2017-12-12 09:20:38', 0, None,
                        '2017-12-11 20:37:51', '2017-12-18 22:00:27', 0, 'wt3nqfq', '武汉市', 'JH91_W', '2700101709070311',
                        '20171221']
                       ]
            writer.write(records)  # 7天内有心跳
if __name__ == '__main__':
    #unittest.main()
    #print(__name__.__doc__)
    #suite = unittest.TestSuite()
    #test_lowPowerNum1 test_lowPowerNum11 test_lowPowerTrend_1
    #test_slienceNum1 test_slienceNum11 test_slienceTrend_1  test_indentifyNum1 test_indentifyTrend_1
    #test_troubleNum1 test_troubleTrend_1 test_recoveryNum1 test_recoveryTrend_1
    #tests = [TestBikes("test_addSilence3")]
    #suite.addTests(tests)

    #runner = unittest.TextTestRunner(verbosity=2)
    #runner.run(suite)

    test_dir=os.path.join(os.getcwd())
    discover=unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')
    runner=unittest.TextTestRunner()
    runner.run(discover)
