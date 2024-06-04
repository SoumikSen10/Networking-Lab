import socket

def addition(a, b):
    return str(a + b)

def subtraction(a, b):
    return str(a - b)

def multiplication(a, b):
    return str(a * b)

def division(a, b):
    if b == 0:  # Handling division by zero
        return "Division by zero error"
    return str(a / b)

def fibonacci(n):
    a, b = 0, 1
    fib_sequence = [a, b]
    for _ in range(n - 2):
        a, b = b, a + b
        fib_sequence.append(b)
    return str(fib_sequence)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_prime(n):
    if is_prime(n):
        return "Prime"
    else:
        return "Not Prime"

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False

def check_leap_year(year):
    if is_leap_year(year):
        return "Leap Year"
    else:
        return "Not a Leap Year"

host = '127.0.0.1'
port = 8002

s = socket.socket()
s.bind((host, port))
s.listen(1)
c, addr = s.accept()
print('A client connected')

while True:
    data_received = c.recv(1024)
    if not data_received:
        break

    data_str = data_received.decode()
    print('Data from client: ' + data_str)

    data = data_str.split()
    
    operation = data[0]
    if operation == 'addition':
        result = addition(int(data[1]), int(data[2]))
    elif operation == 'subtraction':
        result = subtraction(int(data[1]), int(data[2]))
    elif operation == 'multiplication':
        result = multiplication(int(data[1]), int(data[2]))
    elif operation == 'division':
        result = division(int(data[1]), int(data[2]))
    elif operation == 'fibonacci':
        result = fibonacci(int(data[1]))
    elif operation == 'is_prime':
        result = check_prime(int(data[1]))
    elif operation == 'is_leap_year':
        result = check_leap_year(int(data[1]))
    else:
        result = 'Invalid operation'

    c.send(result.encode())

c.close()
