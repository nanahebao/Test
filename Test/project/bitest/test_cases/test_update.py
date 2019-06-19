from lib.request_process import HttpRequest
#uri='http://192.168.19.221:7771'
host='https://observatory.ofo.so/'
rq = HttpRequest(host)
path="mobile/api/update"

DEVICE={
"device_id": "62d788f7c5d142acaadf4824c271ca29",
"token": "46d61bc1fbb31466976f2da0e13de7c55f0e35cd"

}
#服务器为1.2
versions={
    "0.2",#低于服务器版本 major
    "1.1",#低于服务器版本，minor
    "1.2",#等于服务器版本
    "2.1"#大于服务器版本
}
for version in versions:
    print(version)
    API={
    "os": "ios",
    "version": version
    }

    datas={
    "verify_params": DEVICE,
    "api_params": API
    }

    rs=rq.http_request(path,json=datas)
    #print(datas)
    #assert rs.status_code==200
    print(rs.json())