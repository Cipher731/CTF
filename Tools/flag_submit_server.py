import queue
import time
import requests
import threading
import socket

DELAY = 3

q = queue.Queue()
submitted = set()


def submit(answer: str):
    print('[+] Sending flag: ' + answer)
    if answer in submitted:
        print('[-] Already sent')
        return
    post_url = 'https://172.16.4.1/Common/awd_sub_answer'
    token = '35f75d0e0422dc9032ee8006b9965c23'
    result = requests.post(post_url, data={
        'token': token,
        'answer': answer
    }, verify=False)
    print(result.content.decode())
    submitted.add(answer)


def worker():
    former = time.time()
    while True:
        item = q.get()
        time.sleep(max(DELAY - (time.time() - former), 0))
        submit(item)
        former = time.time()


def server(connection: socket.socket):
    while True:
        flag = connection.recv(50)
        if not flag:
            break
        q.put(flag.decode().strip())


t = threading.Thread(target=worker)
t.start()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 6666))
s.listen(5)

while True:
    conn, addr = s.accept()
    threading.Thread(target=server(conn))
