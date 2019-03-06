from socket import socket
serverName = '10.205.2.223'
serverPort = 2223
clientSocket = socket()
clientSocket.connect((serverName,serverPort))
f = open('na1.txt','r')
msg = f.read()
f.close()
print(msg)
clientSocket.send(msg.encode('utf-8'))
rcvd = clientSocket.recv(1024)
print('From Server: \n', rcvd.decode())
clientSocket.close()
