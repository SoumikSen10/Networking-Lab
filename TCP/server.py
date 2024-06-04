import socket

def addition(a,b):
    return str(a+b)

def subtraction(a,b):
    return str(a-b)

def multiplication(a,b):
    return str(a*b)

def division(a,b):
    return str(a/b)

host = '127.0.0.1'
port = 8002

s = socket.socket() #create server side socket

s.bind((host,port)) #binding the socket to host and port

s.listen(1) # max num of connections allowed

c, addr = s.accept() #wait till a client connects

print('A client connected')

#server runs continuously until all data is received from client
while True:
    data_received = c.recv(1024) #receive byte data from client

    if not data_received: #if client sends empty string, stop
        break
    
    print('Data from client: ' + str(data_received.decode())) #display clients raw/byte message as string
    data = data_received.decode().split()
    n1, n2 = map(int, data[1:])
    data_to_send = ''
    if data[0] == 'addition':
        data_to_send = addition(n1,n2) #server's message to client
    elif data[0] == 'subtraction':
        data_to_send = subtraction(n1,n2)
    elif data[0] == 'multiplication':
        data_to_send = multiplication(n1,n2)
    elif data[0] == 'division':
        data_to_send = division(n1,n2)

    c.send(data_to_send.encode()) #send the data to client in byte format
c.close() #close connection
