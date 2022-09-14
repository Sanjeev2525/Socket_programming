from socket import *

SERVER = "192.168.29.164"

s=socket(AF_INET,SOCK_STREAM)
s.connect((SERVER,5050))
msg=s.recv(1024)
print(msg.decode("utf-8"))