from socket import *
sn = '127.0.0.1'
sp = 12000
cs = socket(AF_INET,SOCK_DGRAM)
msg = input('Input lowercase sentence:')
cs.sendto(msg.encode(),(sn, sp))
sMsg, serverAddress = cs.recvfrom(2048)
print ('Uppercase Sentence : ',sMsg.decode())
cs.close()
