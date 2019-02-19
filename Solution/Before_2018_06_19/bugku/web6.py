import requests
import base64

target = 'http://120.24.86.145:8002/web6/'

s = requests.Session()

r = s.get(target)
flag = base64.b64decode(r.headers['flag']).decode()
print(flag)
flag = base64.b64decode(flag.split(': ')[1]).decode()

r2 = s.post(target, data={'margin': flag})
print(r2.content.decode())
