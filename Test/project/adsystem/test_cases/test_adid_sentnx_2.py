from lib.request_process import HttpRequest
uri="http://192.168.19.229:9080"
rq=HttpRequest(uri)
path='/res/adid/setnx'
times=['null', None, ' ', '', not str, 'test123jijihihfiehgheigegngiengeg_44598787868676555', [],{}]
for expire_time in times:
 data={
 'adid':'878_ue08878ou7',
 'expire_time':expire_time
  }
 rs=rq.http_request(path,params=data)
 js=rs.json()
 print(js)