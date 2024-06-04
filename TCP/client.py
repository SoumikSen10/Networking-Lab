import socket

server_ip = '127.0.0.1'
server_port = 8002

s = socket.socket()
s.connect((server_ip, server_port))

print("Available operations: addition, subtraction, multiplication, division, fibonacci, primecheck , leap_yearcheck")

data_to_server = input('Operation number1 number2: ')

while data_to_server != 'exit':
    s.send(data_to_server.encode())

    data_from_server = s.recv(1024)
    print(data_to_server.split()[0] + ' result: ' + str(data_from_server.decode()))

    data_to_server = input('Operation number1 number2: ')

s.close()
