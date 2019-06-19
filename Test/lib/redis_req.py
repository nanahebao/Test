# encoding=utf-8

import redis
'''
print(redis.__file__)
r = redis.Redis(host='192.168.19.188', port=6997, password='poiu0987')
name = r.hget('USERINFO_UID:9527', 'city')
print(name)
group = r.hget('USERINFO_UID:9527', 'group')
print(group)
print(r.keys('*'))
print(r.hgetall('U_T_G_UID:113011119'))


print('9527', r.hgetall('U_T_G_UID:9527'))
print(name)
'''

class GetRedis:
    def __init__(self):
        #self.redis = redis.Redis(host=HOST, port=PORT, password=PSWD)
        self.redis = redis.Redis(host='192.168.4.45', port=3000, password='MKL7cOEehQf8aoIBtHxs')

    def get_valuebykey(self, name, key):
        return self.redis.hget(name, key)

    def list_keys(self):
        return self.redis.keys('*')

    def get_hgetall(self, name):
        return self.redis.hgetall(name)

    def del_key(self, name, *keys):
        return self.redis.hdel(name, *keys)

#r = redis.Redis(host='127.0.0.1', port=6379)
#r.set('name','test')
#print(r.get('name'))
if __name__ == '__main__':
    rds = GetRedis()
    print(rds.get_hgetall('U_T_G_UID:10000001'))
    print(rds.get_hgetall('USERINFO_UID:9527'))
    print(rds.get_valuebykey('U_T_G_UID:9527', '1'))
    print(rds.list_keys())
    print(rds.del_key('U_T_G_UID:10000001', '21'))
    print(rds.get_valuebykey('U_T_G_UID:9527', '1'))
    print(rds.get_hgetall('U_T_G_UID:10000001'))

