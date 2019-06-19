import requests

files = ['f.png']
descs={'测试水印2',
       }

url = 'https://qatest.api.ofo.com/ofo/Api/photo/uploadImage'

for item in files:
    for desc in descs:
        data = {
            'token': 'c0a97b50-faeb-11e6-99cd-1753dd72a8f0',
            'desc': desc,
            'lng': '116',
            'lat': '39',
            'location': '北京'
        #'file': open(item, 'rb')
     }
        headers = {'content/type': 'form'}
        file = {'file': open(item, 'rb')}
        rs = requests.post(url, data=data, files=file)
        print(rs.json())