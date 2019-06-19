import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import datetime
from common.myconn import Cursor

DBINFO_FT = {
    "host": "rm-2zeuw6gt14vxka98x.mysql.rds.aliyuncs.com",
    "database": "ofo_ftcar_new",
    "user": "ofo_db",
    "password": "UihQ6DzyK9tYI8ZS",
    "port": 3306
}

CORE_AREA = 1
RECYCLE_AREA = 2

DEFAULT_BICYCLE = 0
BAD_BICYCLE = 1
LOWPOWER_BICYCLE = 2
SILENCE_GOOD_BICYCLE = 3
CHECKS = 4

mysqlconn = Cursor.new(**DBINFO_FT)

def merge_by_minute(today, current_minute):
    sql = """select dt, city_id, code, count(distinct(case when status not in (7,8,10) then bicycle_no end)) checks,
             count(distinct(case when tags like '%silence%' and status in (3,4,5,6) then bicycle_no end)) silence_good,
             count(distinct(case when tags like '%silence%' and status = 5 then bicycle_no end)) activated,
             count(distinct(case when tags like '%low_power%' and status in (1,2,9) then bicycle_no end)) lowpower,
             count(distinct(case when tags like '%low_power%' and status = 2 then bicycle_no end)) lowpower_in,
             count(distinct(case when status in (1,2,9) then bicycle_no end)) bad,
             count(distinct(case when status = 2 then bicycle_no end)) bad_in,
             count(distinct(case when status = 10 then bicycle_no end)) recycle from t_car_mark_records
             where dt = '{0}'
             group by dt, city_id, code""".format(today)
    sqlres = mysqlconn.fetchall(sql)
    li = ""
    li_min = ""
    index = 0
    for row in sqlres:
        if row['recycle'] > 0:
            li += "('{0}', '{1}', '{2}', {3}, {4}, {5}, {6}),".format(row['dt'], row['city_id'], row['code'],
                DEFAULT_BICYCLE, RECYCLE_AREA, row['recycle'], 0)
            li_min += "('{0}', '{1}', '{2}', {3}, {4}, {5}, {6}, '{7}'),".format(row['dt'], row['city_id'], row['code'],
                DEFAULT_BICYCLE, RECYCLE_AREA, row['recycle'], 0, current_minute)
        else:
            if row['checks'] > 0:
                li += "('{0}', '{1}', '{2}', {3}, {4}, {5}, {6}),".format(row['dt'], row['city_id'], row['code'],
                     CHECKS, CORE_AREA, row['checks'], 0)
                li_min += "('{0}', '{1}', '{2}', {3}, {4}, {5}, {6}, '{7}'),".format(row['dt'], row['city_id'],
                        row['code'], CHECKS, CORE_AREA, row['checks'], 0, current_minute)
            if row['silence_good'] > 0:
                li += "('{0}', '{1}', '{2}', {3}, {4}, {5}, {6}),".format(row['dt'], row['city_id'], row['code'],
                     SILENCE_GOOD_BICYCLE, CORE_AREA, row['silence_good'], row['activated'])
                li_min += "('{0}', '{1}', '{2}', {3}, {4}, {5}, {6}, '{7}'),".format(row['dt'], row['city_id'],
                        row['code'], SILENCE_GOOD_BICYCLE, CORE_AREA, row['silence_good'], row['activated'], current_minute)
            if row['lowpower'] > 0:
                li += "('{0}', '{1}', '{2}', {3}, {4}, {5}, {6}),".format(row['dt'], row['city_id'], row['code'],
                     LOWPOWER_BICYCLE, CORE_AREA, row['lowpower'], row['lowpower_in'])
                li_min += "('{0}', '{1}', '{2}', {3}, {4}, {5}, {6}, '{7}'),".format(row['dt'], row['city_id'],
                        row['code'], LOWPOWER_BICYCLE, CORE_AREA, row['lowpower'], row['lowpower_in'], current_minute)
            if row['bad'] > 0:
                li += "('{0}', '{1}', '{2}', {3}, {4}, {5}, {6}),".format(row['dt'], row['city_id'], row['code'],
                     BAD_BICYCLE, CORE_AREA, row['bad'], row['bad_in'])
                li_min += "('{0}', '{1}', '{2}', {3}, {4}, {5}, {6}, '{7}'),".format(row['dt'], row['city_id'],
                        row['code'], BAD_BICYCLE, CORE_AREA, row['bad'], row['bad_in'], current_minute)
        index += 1
        if index == 50:
            li = li.strip(',')
            sql = """replace into ofo_carcheck_day_summary (dt, city_id, code, cartype, railtype, num, processed)
                     values {0}""".format(li)
            li = ""
            index = 0
            mysqlconn.execute(sql)
            li_min = li_min.strip(',')
            sql = """replace into ofo_carcheck_minute_summary (dt, city_id, code, cartype, railtype, num, processed, minute)
                     values {0}""".format(li_min)
            li_min = ""
            mysqlconn.execute(sql)
    if li != "":
        li = li.strip(',')
        sql = """replace into ofo_carcheck_day_summary (dt, city_id, code, cartype, railtype, num, processed)
                 values {0}""".format(li)
        mysqlconn.execute(sql)
        li_min = li_min.strip(',')
        sql = """replace into ofo_carcheck_minute_summary (dt, city_id, code, cartype, railtype, num, processed, minute)
                 values {0}""".format(li_min)
        mysqlconn.execute(sql)


if __name__ == '__main__':
    today = datetime.datetime.today().strftime('%Y%m%d')
    current_minute = datetime.datetime.today().strftime('%Y%m%d%H%M')
    merge_by_minute(today, current_minute)