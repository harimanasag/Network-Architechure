import sys
import socket
host = '10.205.2.223'
port = 2305

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)
X = int(input('how many clients:'))
for j in range(0, X):
    print("opened connection for clients")
    c, addr = s.accept()
    print("connected by", addr)
    i = "xx"
    if i != "exit":
        i = c.recv(1024).decode()
        print("received", repr(i))
        print("client", j+1, 'connection closed')
