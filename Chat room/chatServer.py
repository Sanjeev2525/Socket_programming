#UDP
from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print ('The server is ready to receive')
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    print('Received message from client : ',message.decode())
    sentMessage = input('Enter message to be send : ')
    serverSocket.sendto(sentMessage.encode(),clientAddress)
