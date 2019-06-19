import pandas as pd
import pymysql
import logging
class DbReq:
    def __init__(self, host, user, password, db, port=3306):
        try :
            self.host = host
            self.user = user
            self.password = password
            self.db = db
            self.port = port
            self.db = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db, port=self.port, use_unicode=True, charset='utf8')
            self.cursor = self.db.cursor()
        except Exception as e:
            print(e)
            print('DB连接错误')

    def cursors_sql(self, sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
            print('sql执行错误')

    def cursors_close(self):
        self.cursor.close()

    def db_close(self):
        self.db.close()


def masterdata(sql):
    db = DbReq('10.6.37.180', 'dev_blend_pw', 'W6sIpx0LDv4iyqoK9zAT', 'ofo_bi_master', port=4457)
    data = db.cursors_sql(sql)
    db.cursors_close()
    db.db_close()
    # print(data)
    return data

def uuapdata(sql):
    db = DbReq('10.6.37.180', 'dev_blend_pw', 'W6sIpx0LDv4iyqoK9zAT', 'ofo_bi', port=4457)
    data = db.cursors_sql(sql)
    db.cursors_close()
    db.db_close()
    return data