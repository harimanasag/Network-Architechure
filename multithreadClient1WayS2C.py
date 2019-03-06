import sys
import socket
host = '10.205.2.223'
port = 2219
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
message = "Hello"
print(' Connected ')
while message != "exit":
    message = input('Type Message: ')
    s.send(message.encode())
s.close()
print('connection closed')
