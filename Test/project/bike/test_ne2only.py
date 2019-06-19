from odps import ODPS
import pymysql
from odps.models import partitions

o= ODPS('LTAIiLBfcRtW2Trt', 'wvQYMvfJknEpOoJorrEkB0bwUBZxf7', 'ofo_test')
project = o.get_project()
print(project)
with o.execute_sql("""select A.carno,
    A.cname As Acname ,A.cvalue Acvalue,
    B.cname As Bcname ,B.cvalue Bcvalue,
    C.cname As Ccname, C.cvalue Ccvalue,
    D.cname As Dcname ,D.cvalue Dcvalue,
    E.cname As Ecname ,E.cvalue Ecvalue,
    'location' As Qcname, location AS Qcvalue
 from
 (select carno, 'city' as cname, city as cvalue, area from  ofo_t_bike_location where dt=20171222 ) A
left outer join
(select carno, 'order_num' as cname, 1 as cvalue from  ofo_t_bike_location where dt=20171221
and TO_CHAR(locate_time, 'yyyymmdd') >= '20171215') B on A.carno = B.carno
left outer join
(select carno, 'area' as cname, area as cvalue from  ofo_t_bike_location where dt=20171222
and TO_CHAR(locate_time, 'yyyymmdd') >= '20171215') D on A.carno = D.carno
left outer join
(select carno, 'lock_type' as cname, lock_type as cvalue from  ofo_t_bike_location where dt=20171221
and TO_CHAR(locate_time, 'yyyymmdd') >= '20171215') E on A.carno = E.carno
left outer join
(select carno, concat_ws(';',cast(lng as string), cast(lat as string) ) As location from ofo_t_bike_location where dt=20171222) Q on A.carno = Q.carno
left outer join
(
select carno,'silent_tag' as cname, tag as cvalue from (
select t_last_day_silent.carno,
    case when  t_today_order.carno is not null and t_engine_jd.bicycle_no is null then 'zr_active'
    when t_today_order.carno is not null and t_engine_jd.bicycle_no is not null then 'engine_active'
    when t_today_order.carno is null then 'continue_silent' end as tag

from
    (select carno from (
        select carno from (
            select carno from (select *,row_number() over(partition by carno order by createtime desc ) rn from  ofo_t_order_state where dt<=20171221
            ) a where rn=1 and dt<20171219
    union all
    select bicycle_no as carno from ofo_t_bicycle_mark_records where dt=20171222 and tags like '%silence%' and status=5 group by bicycle_no ) tmp group by carno ) tt ) t_last_day_silent
    left outer join
    (select carno from  ofo_t_order_hg where dt=20171222
    group by carno) t_today_order on t_last_day_silent.carno = t_today_order.carno
    left outer join
    ( select bicycle_no from ofo_t_bicycle_mark_records where dt=20171221 and status=5 and  tags like '%silence%' group by bicycle_no) t_engine_jd
    on t_last_day_silent.carno = t_engine_jd.bicycle_no
union all
select t_today_silent.carno, 'new_add_silent' as tag
from
    (select carno from  (
        select carno from (select *,row_number() over(partition by carno order by createtime desc ) rn from  ofo_t_order_state where dt<=20171221
            ) a where rn=1 and dt<20171219
    union all
    select bicycle_no as carno from ofo_t_bicycle_mark_records where dt=20171221 and tags like '%silence%' and status=5 group by bicycle_no ) tmp group by carno ) t_last_day_silent
    right outer join
    (select carno from (select *,row_number() over(partition by carno order by createtime desc ) rn from  ofo_t_order_hg where dt<=20171222
            ) a where rn=1 and createtime < '2017-12-20 00:00:00' ) t_today_silent on t_last_day_silent.carno = t_today_silent.carno
where t_last_day_silent.carno is null
    ) AA
union all
  select tt.carno, 'silent_tag' as cname,'continue_acitve' as cvalue from (
select carno from ofo_t_order_hg where dt>='20171219' group by carno
) tt left outer join
(select carno,'silent_tag' as cname, tag as cvalue from (
select t_last_day_silent.carno,
    case when  t_today_order.carno is not null and t_engine_jd.bicycle_no is null then 'zr_active'
    when t_today_order.carno is not null and t_engine_jd.bicycle_no is not null then 'engine_active'
    when t_today_order.carno is null then 'continue_silent' end as tag

from
    (select carno from (
        select carno from (
            select carno from (select *,row_number() over(partition by carno order by createtime desc ) rn from  ofo_t_order_state where dt<=20171221
            ) a where rn=1 and dt<20171219
    union all
    select bicycle_no as carno from ofo_t_bicycle_mark_records where dt=20171222 and tags like '%silence%' and status=5 group by bicycle_no ) tmp group by carno ) tt ) t_last_day_silent
    left outer join
    (select carno from  ofo_t_order_hg where dt=20171222
    group by carno) t_today_order on t_last_day_silent.carno = t_today_order.carno
    left outer join
    ( select bicycle_no from ofo_t_bicycle_mark_records where dt=20171221 and tags like '%silence%' and status=5 group by bicycle_no) t_engine_jd
    on t_last_day_silent.carno = t_engine_jd.bicycle_no
union all
select t_today_silent.carno, 'new_add_silent' as tag
from
    (select carno from (
        select carno from (
            select carno from (select *,row_number() over(partition by carno order by createtime desc ) rn from  ofo_t_order_state where dt<=20171221
            ) a where rn=1 and dt<20171219
    union all
    select bicycle_no as carno from ofo_t_bicycle_mark_records where dt=20171221 and tags like '%silence%' and status=5 group by bicycle_no ) tmp group by carno ) tt ) t_last_day_silent
    right outer join
    (select carno from (select *,row_number() over(partition by carno order by createtime desc ) rn from  ofo_t_order_hg where dt<=20171222
            ) a where rn=1 and createtime < '2017-12-20 00:00:00' ) t_today_silent on t_last_day_silent.carno = t_today_silent.carno
where t_last_day_silent.carno is null
    ) AB ) BB on tt.carno = BB.carno where BB.carno is null
) C on A.carno = C.carno

left outer join (
select carno from  ofo_t_station_record where dt<='20171222' and dt>='20171215' and record_type=1
group by carno
) SS on A.carno = SS.carno
where SS.carno is  null""").open_reader() as reader:
    for record in reader:
        print(record)