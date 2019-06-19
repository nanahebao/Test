
# encoding=utf-8
from odps import ODPS
import pymysql

odps = ODPS('LTAI2wkz5kLt3205','RfTGzh2dfoBljs3ZZKwfpYw6OK9KYX','ofo')
project = odps.get_project()
print(project)

print(project.__getstate__())
t = odps.get_table('ofo_t_puser_partition')


with odps.execute_sql('select id from ofo_t_puser_partition where oauth in (1)').open_reader() as reader:
    
    #返回结构化结果
    #返回结果：
             
                odps.Record {
                 id  90637
                 }
                 odps.Record {
                 id  90640
                 }
             
    for record in reader:#返回结构化结果
        print(record)
    
    #返回原始sql结果
    print(reader)

'''
mysql_db = pymysql.connect(host='192.168.19.188', port=3306, user='janus', password='janus!@#', db='janus')
#cursor = mysql_db.cursor(cursorclass = pymysql.cursors.DictCursor)
cursor = mysql_db.cursor()
#cursor.execute('select data from janus_t limit 10')

cursor.execute('SHOW COLUMNS FROM janus_t')
clume = cursor.fetchall()
print(clume)
cursor.execute("select * from janus_t where tag='source'")
data = cursor.fetchall()


#print(data)
for d in data:
    print(d)
cursor.close()
mysql_db.close()
'''