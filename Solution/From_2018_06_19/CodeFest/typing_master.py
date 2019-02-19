import socket
import re

host = '34.216.132.109'
port = 9093

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
question = s.recv(1024)
print(question.decode())
a, b, c, d = re.search("'(.)' ([0-9]*).*'(.)' ([0-9]*)", question.decode()).groups()
print(a, b, c, d)
result = a * int(b) + c * int(d) + str(ord(a) + ord(c)) + '\n'
s.send(result.encode())
print(s.recv(1024))
