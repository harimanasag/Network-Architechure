import socket
import _thread
from _thread import start_new_thread
host = '10.205.2.223'
port = 2218
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)
client_list = [];
def client_broadcast(addr,strg):
    for i in client_list:
        i.sendall(str(addr).encode())
        print("sent to all!")
def client_thread(c):
    print("connected by ", addr)
    i = "xx"
    while i != "exit":
        i = c.recv(1024).decode()
        print("received", addr, repr(i))
        start_new_thread(client_broadcast,(addr, i, ))
        print("client connection closed", addr)
    c.close()
    client_list.pop(client_list.index(c));
while True:
    print("opened connection for clients")
    c, addr = s.accept()
    client_list.append(c);
    start_new_thread(client_thread, (c,))
print("connection closed with all clients")
s.close()
