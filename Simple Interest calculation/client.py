from socket import *
serverName='127.0.0.1'
serverPort=12000
clientSocket=socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
p=input("principle amount:")
n=input("No of years:")
r=input("Rate of interest:")
clientSocket.send(p.encode())
clientSocket.send(n.encode())
clientSocket.send(r.encode())
si=clientSocket.recv(1024)
print("From server Simple Interest is:",si.decode())
clientSocket.close()