import re

import requests

target = 'http://120.24.86.145:8002/web10/'

regex = re.compile('key.*key.{4,7}key:/./(.*key)[a-z]_')
print(regex.search('key0key0000key:/0/000keya_') is not None)

print(regex.pattern)

r = requests.get(target, params={
    'id': 'key0key0000key:/0/000keya_'
})

print(r.content.decode())
