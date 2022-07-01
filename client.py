from http import client
from socket import *

c=socket(AF_INET, SOCK_STREAM)
c.connect(('192.168.139.132',5959))
data=c.recv(1024)
msg=data.decode('utf-8')
print(f'Server msg: \n\t{msg}')
c.send('Good'.encode('utf-8'))

input("end")