import requests
import re
from bs4 import BeautifulSoup

s = requests.session()
host = 'http://34.216.132.109:8083'

r = s.get(host + '/fp')
i = 1
while True:
    flag = re.search('CodefestCTF{.*}', r.text, re.I)
    if flag:
        print(r.text)
        break
    soup = BeautifulSoup(r.text, 'html.parser')
    print(soup.body)
    print(str(i) + ': ' + host + soup.form['action'] + '?')
    i += 1
    r = s.get(host + soup.form['action'] + '?')
