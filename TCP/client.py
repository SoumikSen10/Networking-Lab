import socket

server_ip = '127.0.0.1'
server_port = 8002

s = socket.socket() #create client side socket

s.connect((server_ip,server_port))

data_to_server = input('Operation number1 number2: ')  #enter client's message to server


while data_to_server != 'exit': #keep on sending data to server until 'exit' is entered
    s.send(data_to_server.encode()) #send byte data to server

    data_from_server = s.recv(1024) #receive data from server
    print(data_to_server.split()[0]+' is ' + str(data_from_server.decode())) #display server's message in string format

    data_to_server = input('Operation number1 number2: ') #enter data to be sent to server

s.close() #close connection
    
