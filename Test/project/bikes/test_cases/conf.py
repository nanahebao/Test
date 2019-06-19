from odps import ODPS
import pymysql
from odps.models import partitions

o= ODPS('LTAIiLBfcRtW2Trt', 'wvQYMvfJknEpOoJorrEkB0bwUBZxf7', 'ofo_test')
project = o.get_project()
t1 = o.get_table('ofo_test.ofo_t_bicycle_mark_records')#运维激活
t2=o.get_table('ofo_test.ofo_t_order_state')
t3=o.get_table('ofo_test.ofo_t_bike_location') #全量表
t4=o.get_table('ofo_test.ofo_t_order_hg')
t5=o.get_table('ofo_test.ofo_t_station_record')