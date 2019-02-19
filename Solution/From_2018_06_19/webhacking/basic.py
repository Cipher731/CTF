import requests

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'


def login():
    data = {
        'id': input('id:'),
        'pw': input('pw:')
    }
    s = requests.session()
    s.post('http://webhacking.kr/index.html?enter=1', data=data)
    s.headers.update({'User-Agent': user_agent})
    return s
