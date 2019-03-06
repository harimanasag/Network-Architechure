import sys
import socket
import _thread
from _thread import start_new_thread
host = '10.205.2.223'
port = 2218
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
def rec_print():
    while True:
        z = s.recv(1024).decode()
        print("echoed reply from:", z)
message = "Hello"
print("Connected ")
rec_thread = start_new_thread(rec_print, ())
while message != "exit":
    message = input('Type Message: ')
    s.send(message.encode())
s.close()
print("connection closed")
