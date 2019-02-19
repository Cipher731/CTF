import base64
import urllib

import requests

url = 'http://139.59.61.57:49120/'


def cbc_flip(value, index, c1, c2):
    lst = list(value)
    lst[index] = chr(ord(lst[index]) ^ ord(c1) ^ ord(c2))
    return ''.join(lst)


def hack(username, index, c1, c2):
    r = requests.post(url + 'login.php', data={
        'username': username,
        'password': 'Password1'
    })

    auth = urllib.parse.unquote(r.cookies['auth'])
    iv = urllib.parse.unquote(r.cookies['iv'])

    raw_auth = base64.b64decode(auth)
    raw_iv = base64.b64decode(iv)

    new_auth = urllib.parse.quote(base64.b64encode(cbc_flip(raw_auth, index, c1, c2).encode()).decode())
