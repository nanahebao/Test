import pymysql
conn=pymysql.connect(host='10.6.27.61',port=3306,user='photo_audit_w',passwd='PhotoAuditW@$123',db='photo_test')
cursor=conn.cursor()
cursor.execute('SHOW COLUMNS FROM t_photo_audit')
column=cursor.fetchall()
cursor.execute('select * from t_photo_audit')
data=cursor.fetchall()
#print(column)
print(data)
cursor.close()
conn.close()


