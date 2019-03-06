import sys
import socket
host = '10.205.2.223'
port = 2305

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
print("connected with server")
message = "Hello"

while message != 'exit':
    message = input("Type message: ")
    s.send(message.encode())
s.close()
print("connection closed")
