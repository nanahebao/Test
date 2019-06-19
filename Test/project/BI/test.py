
import pandas as pd
import logging

from project.BI import dbreq

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler('log123.txt')
formt = logging.Formatter('%(asctime)s - %(message)s')
handler.setFormatter(formt)
logger.addHandler(handler)
master_sql = 'select name,belong_area_code ,city_code from `bi_uuap_permission` where `belong_area_code`!="" '
data = dbreq.masterdata(master_sql)
df = pd.DataFrame(list(data), columns=['name', 'group_id','city_code'])
ans = []

for i in range(len(df.index)):
    name, group_id ,city_code= df.iloc[i]
    print(df.iloc[i])
    if type(eval(group_id)) is int:
        #print([eval(group_id)])
        sql1 = '''select count(*) from t_rail where group_id='%s' AND city_id='%s' AND deleted=0''' % (eval(group_id),city_code)
        expect_num = dbreq.uuapdata(sql1)
        sql2 = '''select count(*) from (select code from t_rail where group_id='%s AND deleted=0') a join (select distinct rail_code from ofo_engine_uuap_role_source where user_name='%s') b on a.code=b.rail_code''' % (eval(group_id), name)
        actual_num = dbreq.uuapdata(sql2)
        logger.info((name, eval(group_id), expect_num[0][0], actual_num[0][0], '%.2f%%' % ((actual_num[0][0]/expect_num[0][0])*100)))
        #ans.append((name, eval(group_id), expect_num[0][0], actual_num[0][0], '%.2f' % ((actual_num[0][0]/expect_num[0][0])*100)))
    else:
        for tmp in eval(group_id):
            #print(tmp)
            sql1 = '''select count(*) from t_rail where group_id='%s'  AND deleted=0''' % tmp
            print('********')
            expect_num = dbreq.uuapdata(sql1)
            sql2 = '''select count(*) from (select code from t_rail where group_id='%s' AND deleted=0) a join (select distinct rail_code from ofo_engine_uuap_role_source where user_name='%s') b on a.code=b.rail_code''' % (tmp, name)
            actual_num = dbreq.uuapdata(sql2)
            logger.info((name, tmp, expect_num[0][0], actual_num[0][0], '%.2f%%' % ((actual_num[0][0]/expect_num[0][0])*100)))
            #ans.append((name, tmp, expect_num[0][0], actual_num[0][0]), '%.2f' % ((actual_num[0][0]/expect_num[0][0])*100))