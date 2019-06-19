from lib.request_process import HttpRequest
from project.ad_admin.conf import ip

rq=HttpRequest(ip)
path='/api/schedule/situation/36'
rs=rq.http_request(path,method='GET')
print(rs.json(),rs.status_code)