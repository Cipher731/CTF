import sys
import requests
import re

green = '\033[92m{}\033[0m'
blue = '\033[94m{}\033[0m'


def write_line():
    print(blue.format('------------------------------------------------'))


def add_postfix(s):
    postfix = ['', '.php', '.php~', '.php-', '.php.swp', '.php.swap', '.php.txt', '.php.bak', '.txt', '.zip', '.bak',
               '.rar', '.bak.zip', '.js']
    return list(map(lambda x: s + x, postfix))


def directory_scan(target, add=None):
    interesting_response = []
    write_line()
    print('Start basic directory scan')

    vulnerabilities = [
        '', 'robots.txt', 'readme.md', 'README.md', 'readme.html', 'README.html', 'phpmyadmin.php', '.git', '.hg',
        '.DS_Store', '.svn', '.svn/wc.db', '.svn/entries', '.idea',
        *add_postfix('index')
    ]

    for item in add:
        vulnerabilities += add_postfix(item)

    for t in vulnerabilities:
        print('Trying ' + target + t, end='\t')
        sys.stdout.flush()
        r = requests.get(target + t)
        if not t:
            print(blue.format('Basic request.'))
            interesting_response.append(r)
        elif r.status_code != 404 or r.history:
            print(green.format(f'Interesting directory found. {r.status_code}'))
            interesting_response.append(r)
        else:
            print('Nothing found.')

    write_line()
    return interesting_response


def cookie_scan(response: requests.Response):
    print('Cookie scan on ' + response.request.url, end='\t')
    interesting_cookies = []
    default = [
        'PHPSESSID'
    ]
    for k, v in response.cookies.iteritems():
        if k not in default:
            interesting_cookies.append((k, v))

    if interesting_cookies:
        print(green.format('Interesting cookies found'))
        for cookie in interesting_cookies:
            print(cookie[0], cookie[1])
    else:
        print('Nothing found.')


def history_scan(response: requests.Response):
    print('History scan on ' + response.request.url, end='\t')
    if response.history:
        print(green.format('Interesting history found'))
        for h in response.history:
            full_scan(h)
    else:
        print('Nothing found.')


def comment_scan(response: requests.Response):
    print('Comment scan on ' + response.request.url, end='\t')
    comment = re.findall('<!--.*?-->', response.text)
    if comment:
        print(green.format('Interesting comment found'))
        for c in comment:
            print(c)
    else:
        print('Nothing found.')


def headers_scan(response: requests.Response):
    print('Headers scan on ' + response.request.url, end='\t')
    common_headers = {
        'Accept', 'Accept-Charset', 'Accept-Encoding', 'Accept-Language', 'Cookie', 'Set-Cookie',
        'Connection', 'ETag', 'If-Match', 'If-None-Match', 'If-Modified-Since', 'If-Unmodified-Since',
        'Last-Modified', 'Age', 'Expires', 'Pragma', 'Cache-Control', 'Authorization', 'Date', 'Accept-Ranges',
        'Proxy-Authenticate', 'Proxy-Authorization', 'Content-Length', 'Content-Type', 'Content-Encoding',
        'Content-Language', 'Content-Location', 'Location', 'Server', 'X-Powered-By', 'Keep-Alive', 'Vary',
        'Transfer-Encoding', 'Accept-Ranges'
    }
    interesting_headers = []
    for header_entry_key, header_entry_value in response.headers.items():
        if header_entry_key not in common_headers:
            interesting_headers.append((header_entry_key, header_entry_value))

    if interesting_headers:
        print(green.format('Interesting headers found'))
        for h in interesting_headers:
            print(h[0] + ': ' + h[1])
    else:
        print('Nothing found.')


def full_scan(response: requests.Response):
    write_line()
    print('Start full scan on ' + response.request.url + '\n')
    history_scan(response)
    comment_scan(response)
    cookie_scan(response)
    headers_scan(response)
    print('\nFull scan finished.')
    write_line()


if __name__ == '__main__':
    url = input('Please input the target url: ').strip()
    adds = []
    expand = input('Do you have any idea about hidden directories? (y/N) ')
    if expand.lower() == 'y':
        adds = input('Please input those suspicions: ').split(' ')

    guess = input('Do you want to scan tips/hint/flag/admin/test ? (y/N) ')
    if guess.lower() == 'y':
        adds += ['tips', 'hint', 'flag', 'admin', 'test', 'common']

    print('Start scanning.')

    rs = directory_scan(url, add=adds)
    s = set()
    for i in rs:
        if i.url not in s:
            full_scan(i)
            s.add(i.url)
