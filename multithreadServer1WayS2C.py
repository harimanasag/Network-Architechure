import sys
import socket
import _thread
from _thread import start_new_thread
host = '10.205.2.223'
port = 2219
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)
def client_thread(c, addr):
    print("connected by ", addr)
    i = "xx"
    while i != "exit":
        i = c.recv(1024).decode()
        print("received", addr, repr(i))
    print("client connection closed")
    c.close()
while True:
    print("opened connection for clients")
    c, addr = s.accept()
    start_new_thread(client_thread, (c, addr, ))
print("connection closed with all clients")
s.close()
