import os
import sys
import time
import string

import requests

s = requests.session()
r = s.post('http://116.62.137.114:4879/login', data={
    'username': 'admintest2313',
    'password': 'admintest'
})
# r0 = s.post('http://116.62.137.114:4879/suggest', data={
#     'suggest[]': string.printable
# })
r1 = s.get('http://116.62.137.114:4879/suggest')
# r2 = s.get('http://116.62.137.114:4879/js/min-test.js')
# r3 = s.get('http://116.62.137.114:4879/view/admintest2313.html')
# r4 = s.get('http://116.62.137.114:4879/view/memo.html')
print(r.text)
