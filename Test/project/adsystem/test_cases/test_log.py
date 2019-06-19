# encoding=utf-8

#from project.mobile.test_cases.conf import ip, mobiletk_path
from lib.request_process import HttpRequest
host = 'https://ma.ofo.com/'
#uri = 'http://192.168.19.221:7771'
uri = 'https://review.ofo.com/ads'
rq = HttpRequest(uri)
path = '/adLog'
data = {"apiVersion":"1.1",
        "logInfo":"{\"client_ping\":[\"https:\/\/www.baidu.com\/\",\"https:\/\/review.ofo.com\/clientPing\/\"],\"info\":{\"upload_params\":\"device_imei=&device_ifa=FC0F3445-0FCE-40EE-8646-3CA8BB2663EA&device_model=iPhone&device_vendor=Apple&os_type=2&os_version=2.9.0&screen_width=750&screen_height=1334&app_version=2.9.0&conn_type=1&ip=10.200.50.141&date_time_number=1511502742&userid=98f090fb135ae1271f8e6c8d7fe3a3a1&ad_source_type=union&ad_source_name=toutiao&ad_id=72596015046&ad_action=show&ad_type=3&advertiser=&page_name=&position=&ad_content_type=\"},\"method\":0,\"server_ping\":\"\"}\n",
        "logType":1,
        "requestId":"bbcde26b1f5721405f6757c673898159",
        "source-locale":"zh_CN",
        "source-version":"14600",
        "source-model":"Le X620",
        "source":"2",
        "source-system":"6.0",
        "token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1MTI1NDc4ODQsImEiOjM1NzI1MTM4NywiYiI6MjgwMjgwODYwNjk5OTc5MzQyMiwiYyI6MjU2MTIxNjI2NzEwMzA2MzgyMn0.bJkiM2qvV3T9jTRQLOdk_o2Eb9-uEa8mWSTlJF0Pfdo"
        }

rs = rq.http_request(path, json=data)
print(data)
print(rs.content)
print(rs.json())