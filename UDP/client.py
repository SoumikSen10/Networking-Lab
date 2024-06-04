#UDP client that receives messages from server

import socket

server_name = 'localhost'
server_port = 8001

#create a client side UDP socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#s.bind((server_name,server_port)) #connect to server with server_name and server port

serverAddrPort = ("127.0.0.1", 8001)

data_to_send = input("Data to server:")
while data_to_send!='exit':
    s.sendto(data_to_send.encode(), serverAddrPort)

    data_from_server = s.recvfrom(1024)
    msg = "Message from Server :{}".format(data_from_server[0].decode())  
    print(msg)
    #print('server says: '+str(data_from_server.decode()))
    data_to_send = input("Data to server:")

s.close() #close the connection
