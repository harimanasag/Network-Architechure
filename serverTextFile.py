from socket import socket
serverName = '10.205.2.223'
serverPort = 2223
serverSocket = socket()
serverSocket.bind((serverName,serverPort))
serverSocket.listen(1)
print('Server is ready')
connectionSocket, addr = serverSocket.accept()
rcvd = connectionSocket.recv(1024).decode()
print(rcvd)
f = open('servermodified.txt','w')
f.write(rcvd)
f.close()
connectionSocket.send(rcvd.encode())
connectionSocket.close()
