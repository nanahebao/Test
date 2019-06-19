
from lib.request_process import HttpRequest
uri="http://192.168.19.229:9080"
rq=HttpRequest(uri)
path='/res/adid/setnx'
adids=['null', None, ' ', '', not str, 'test123jijihihfiehgheigegngiengeg_44598787868676555', [], {}]
for adid in adids:
 data={
 'adid':adid,
 'expire_time':"2"
  }
 rs=rq.http_request(path,params=data)
 js=rs.json()
 print(js)