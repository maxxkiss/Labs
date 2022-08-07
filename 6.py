from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 12345))
a = 0
while a != 'stop':
    a = input('Enter the next string ')
    b = s.send(a.encode())
s.close()
