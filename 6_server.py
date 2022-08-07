from socket import *
s = socket(AF_INET, SOCK_STREAM)    
s.bind(('localhost', 12345))
s.listen(1)
sock, addr = s.accept()
a = 0
while a != 'stop':
    a = sock.recv(1024).decode()
    print ('Client: ', a)
sock.close()
