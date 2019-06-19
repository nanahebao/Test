import logging
import pandas as pd


from project.BI import dbreq

logger=logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler=logging.FileHandler('log_a')
formt=logging.Formatter('%(asctime)s - %(message)s')
handler.setFormatter(formt)
logger.addHandler(handler)
master_sql = 'select name,belong_rail_code from `bi_uuap_permission` where `belong_area_code`=""'
data=dbreq.masterdata(master_sql)
df=pd.DataFrame(list(data),columns=['name', 'rail_ids'])
ans=[]

for i in range(len(df.index)):
    name,rail_ids=df.iloc[i]
    print(df.iloc[i])
    if type(eval(rail_ids)) is int:
        #print(eval(rail_ids))
        sql1='select group_id'


