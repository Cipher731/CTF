import requests
import hashlib
import re


def md5(plain: str):
    m = hashlib.md5()
    m.update(plain.encode())
    return m.hexdigest()


dic = {}
for i in range(10000000):
    dic[md5(str(i))[:5]] = i

s = requests.session()
s.cookies.set('PHPSESSID', 'ni75q4lifi9hbgifdmar8lht67')


def send_message(my_url):
    url = 'http://117.50.10.234/index.php?action=message'
    r = s.get(url)
    h = re.search("substr\(md5\(\$code\),0,5\)=='(.*)'", r.text).group(1)
    data = {
        'url': my_url,
        'code': dic[h]
    }
    r = s.post(url, data=data)
    print(r.text)
