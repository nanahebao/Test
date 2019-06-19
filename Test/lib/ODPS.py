from odps import ODPS
import pymysql
from odps.models import partitions

o= ODPS('LTAIiLBfcRtW2Trt', 'wvQYMvfJknEpOoJorrEkB0bwUBZxf7', 'ofo_test')
project = o.get_project()
print(project)

#print(project.__getstate__())
t1 = o.get_table('ofo_test.ofo_t_bicycle_mark_records')#运维激活
t2=o.get_table('ofo_test.ofo_t_order_state')
t3=o.get_table('ofo_test.ofo_t_bike_location') #全量表
t4=o.get_table('ofo_test.ofo_t_order_hg')
t5=o.get_table('ofo_test.ofo_t_station_record')
#print(t3.schema)
#print(t3.exist_partition('dt=20171221'))
'''
CreatTime={
    ''
}
'''
with t3.open_writer(partition="dt=20171221",create_partition=True) as writer:
    records = [[2, 90001,None, '1',30.6426143646, 114.212059021, 27001, None,'2017-12-20 09:20:38',0,None,'2017-12-11 20:37:51','2017-12-18 22:00:27',0,'wt3nqfq','武汉市','JH91_W','2700101709070311','20171221']
                ]
    writer.write(records) #7天内是否有新跳

'''

with t2.open_writer(partition="dt=20171217",create_partition=True) as writer:
    records = [['t_order7', 2,3187, 11983637,20041, '2017-12-17 20:54:03', 1, 39.990197,116.313852,1,'2017-12-17 20:57:03',39.9908409,116.3079544,-18013,0,0,180,1,0.05,100,1,'武汉市','武汉大学','2017','12','18','51','武汉大学','1','武汉市','100''20171217']
                ]
    writer.write(records)#订单


with t1.open_writer(partition="dt=20171217",create_partition=True) as writer:
    records = [[12, 20041,1, 1,11080, 'silence', 99, None,38.0605734592,114.4531328668,None,None,'2017-11-21 00:00:05','2017-11-21 00:00:06','20171217']
                ]
    writer.write(records)#是否运维


with t4.open_writer(partition="dt=20171217",create_partition=True) as writer:
    records = [['t_order7', 678362081,3187, 11983637,20041, '2017-12-17 20:54:03', 1, 39.990197,116.313852,1,'2017-12-17 20:57:03',39.9908409,116.3079544,-18013,0,0,180,1,0.05,100,1,'武汉市','武汉','武汉大学',1,0,'20171217']
                ]
    writer.write(records)#hg


with t5.open_writer(partition="dt=20171217",create_partition=True) as writer:
    records =[[20041,'2017-12-17 20:54:03',11001,2,'CK593','20171217']]
    writer.write(records)#station




'''



