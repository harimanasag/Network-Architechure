import sys
import socket
host = '10.205.2.223'
port = 6363
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
print("hello from server-NA1Proj")
message = "hello"
while message != "bye from client-NA1Proj":
    message = input("Type Message : ")
    s.send(message.encode())
s.close()
print("bye from server-NA1Proj")
