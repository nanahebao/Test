# encoding=utf-8

import json

import requests

from config.conf import logger


class HttpRequest:
    def __init__(self, url):
        self.url = url

    # def httprequest(url, path, params = '', d = None, headers = None, method = 'GET'):
    def http_request(self, path, method='POST', **kwargs):
        try:
            _func = {
                'GET': requests.get,
                'POST': requests.post,
                'PUT': requests.put,
                'DELETE': requests.delete,
            }
            #print(path)
            url = self.url + path
            #print(kwargs)
            #print(url)
            logger.set_log('url is :%s'%url, level='debug')
            #if self.data is not None:
                #self.data = json.dumps(self.data)
            #if json:
            #    logger.set_log('data is:',json)
            logger.set_log('start sending request...,params:%s'%kwargs, level='debug')
            rs = _func[method](url, **kwargs)
            logger.set_log('the content of response is :%s' % rs.content, level='debug')
            logger.set_log('request success, status code is: %d' % rs.status_code, level='info')
            return rs
        except Exception as e:
            logger.set_log('Exception:%s' % str(e), level='error')
            print(str(e))
            # def transfer(self):
#class ThriftClient:
    #def client(self):


if __name__ == '__main__':
    ip = 'http://192.168.19.186:7001'
    path0 = '/api/bigdata/persona/noah/get_config'
    path1 = '/ofo/get_config'
    request = HttpRequest(ip)
    rq = request.http_request(path=path0, method='GET', params={'x': 1})
    #print(to_json(rq.content))
    print(rq.json()['err_message'])
    print(rq.content)
    print(rq.url)
