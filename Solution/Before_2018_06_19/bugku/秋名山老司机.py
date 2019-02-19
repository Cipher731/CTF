import requests
import re

target = 'http://120.24.86.145:8002/qiumingshan/'


r = requests.get(target)
exp = re.search('<div>(.*)=\?;</div>', r.content.decode()).group(1)

flag = requests.post(target, data={'value': eval(exp)}, cookies=r.cookies)
print(flag.content.decode())
