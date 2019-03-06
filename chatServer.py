import sys
import socket
host = '10.205.2.223'
port = 6362

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)
print("Waiting for clients")
c, addr = s.accept()

print("connected by ", addr)

i = "xx"

while i != "exit":
    i = c.recv(1024).decode()
    print("received", repr(i))

c.close()
print("connection closed")
