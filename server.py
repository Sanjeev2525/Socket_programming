from socket import *

SERVER = "192.168.29.164"

s = socket(AF_INET, SOCK_STREAM) 		#Creates a socket
s.bind(('',5050)) 						#Binds the socket with hostname and portnumber
s.listen(1) 							#Server creates an listening socket
print("server ready!!")

while True:
	clts,add =s.accept()				#Accepts connections from outside
	print(f"Connection to {add}established")  
	clts.send(bytes("Socket Programming in Python","utf-8 "))

