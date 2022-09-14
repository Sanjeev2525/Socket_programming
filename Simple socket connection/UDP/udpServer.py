from socket import *
sp = 12000
ss = socket(AF_INET, SOCK_DGRAM)
ss.bind(('', sp))
print ('The server is ready to receive')
while True:
    msg, ca = ss.recvfrom(2048)
    print('Received input : ',msg.decode())
    modifiedmsg = msg.decode().upper()
    print('Modified message : ',modifiedmsg)
    ss.sendto(modifiedmsg.encode(),ca)
