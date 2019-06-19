# encoding=utf-8

#from project.mobile.test_cases.conf import ip, mobiletk_path
from lib.request_process import HttpRequest
host='https://review.ofo.com'
#uri='http://192.168.19.221:7771'
rq = HttpRequest(host)
path='/ads/getAd?test=1&dump_time=1'
GEO = {
        "longitude": 0,
        "latitude": 0

    }
uids = [
'18f090fb135ae1271f8e6c8d7fe3a3a3',
'28f090fb135ae1271f8e6c8d7fe3a3a3',
'32f090fb135ae1271f8e6c8d7fe3a3a3',
'4198f090fb135ae1271f8e6c8d7fe3a3a3',
'5398f090fb135ae1271f8e6c8d7fe3a3a3',
'6198f090fb135ae1271f8e6c8d7fe3a3a3',
'798f090fb135ae1271f8e6c8d7fe3a3a3',
'8998f090fb135ae1271f8e6c8d7fe3a3a3',
'0198f090fb135ae1271f8e6c8d7fe3a3a3',
'998f090fb135ae1271f8e6c8d7fe3a3a3',
'1867685',
'3235435423',
'19d33199a9dc5a04'
]

DEVICEv13 = {
        "phoneName": "勇超胡的 iPhone",
        "powerOnTime": "206375037.989292",
        "wifiMac": "a0:8c:f8:cf:d0:b3",
        "type": 1,
        "os": 2,
        "screenHeight": 1334,
        "language": "zh",
        #"did": "00000000-0000-0000-0000-000000000000",
        "did": "FC0F3445-0FCE-40EE-8646-3CA8BB2663EA",
        "ssid": "ofo-Office",
        "vendor": "Apple",
        "connType": 1,
        "screenWidth": 750,
        "osVersion": "2.9.0",
        "model": "iPhone" ,
        "wnua":"Mozilla/5.0 (Linux; Android 7.0; MHA-AL00 Build/HUAWEIMHA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.98 Mobile Safari/537.36"
    }

for uid in uids :

    data={
        "adslotIds": ["2","3","4","5"],
        "uid": uid,
        "requestId": "93C7C483-6296-4D0B-A9D8-007114188698",
        "appVersion": "2.9.0",
        "sourceType": "app",
        "apiVersion": "1.1",
        "geo": GEO,
        "ip": "10.200.50.141",
        "device": DEVICEv13
    }
    rs = rq.http_request(path, json=data)
    #assert rs.status_code == 200
    js = rs.json()
    print(js)
    print(uid)










