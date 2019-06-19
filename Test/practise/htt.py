import requests
'''
payload = {'key1': 'value1', 'key2': 'value2'}
r=requests.get("http://httpbin.org/get",params=payload)
print(r.url)
'''

#payload = {'key1': 'value1', 'key2': ['value2', 'value3']}

#r = requests.get('http://httpbin.org/get', params=payload)
#print(r.url)
#print(r.text)
#print(r.content)
#print(r.json())
'''
url='https://api.github.com/some/endpoint'
headers={'user-agent': 'my-app/0.0.1'}
r=requests.get(url,headers=headers)
print(r.json())
print(r.status_code)
'''
# level 或者zone_id过长时
data_le = 'hello,world!this is a test to try a long str,which is exceeded 128,' \
          'hello,world!this is a test to try a long str,which is bigger  '
print(len(data_le))