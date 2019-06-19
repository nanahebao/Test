
import pymysql

mysql_db = pymysql.connect(host='10.6.37.180', port=4457, user='dev_blend_pw', password='W6sIpx0LDv4iyqoK9zAT', db='ofo_bi',use_unicode=True,charset='utf8')
#cursor = mysql_db.cursor(cursorclass = pymysql.cursors.DictCursor)
cursor = mysql_db.cursor()
#cursor.execute('select data from janus_t limit 10')

#cursor.execute('SHOW COLUMNS FROM ofo_engine_uuap_role_source')
#clume = cursor.fetchall()
#print(clume)
#找到permission
cursor.execute("select name,belong_area_code group_id, belong_area_name,belong_rail_code   from ofo_bi_master.bi_uuap_permission where belong_area_code !=' '")
data = cursor.fetchall()


#print(data)
for d in data:
    print(d)
    print(d[1])
    gr_id=d[1]
    cursor.execute('select ')


cursor.close()
mysql_db.close()

