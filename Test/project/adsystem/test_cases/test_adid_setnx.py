
from lib.request_process import HttpRequest
uri="http://192.168.19.229:9080"
rq=HttpRequest(uri)
path='/res/adid/setnx'
adids=['67568787',
       'uyuy',
       '_87w',
       'ygrg_89',
       '87_yues']
for adid in adids:
 data={
 'adid':adid,
 'expire_time':10
  }
 rs=rq.http_request(path,params=data)
 js=rs.json()
 print(js)