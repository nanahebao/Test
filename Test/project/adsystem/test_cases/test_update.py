from lib.request_process import HttpRequest
uri='http://192.168.19.221:7771'
rq = HttpRequest(uri)
path="mobile/api/update"

DEVICE={
"device_id": "62d788f7c5d142acaadf4824c271ca29",
"token": "46d61bc1fbb31466976f2da0e13de7c55f0e35cd"
}
API={
"os": "android",
"version": "1.7"
}

datas={
"verify_params": DEVICE,
"api_params": API
}

rs=rq.http_request(path,json=datas)
print(datas)
assert rs.status_code==200
print(rs.json())