import socket
import time

client_name = 'localhost'
client_port = 8001


#create a UDP socket at server side 
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((client_name, client_port))
#time.sleep(2) #let the server wait for 2 seconds 

#data_receive, addr = s.recvfrom(msg,(client_name,client_port))  #specifying client address as UDP is connectionless protocol, server does not know where to send the packet

while True:
    name, addr1 = s.recvfrom(1024)
    print('Message from client: ' +str(name.decode()))
    data_send = input("Message to client:")
    s.sendto(data_send.encode(), addr1)

s.close() #close the connection


