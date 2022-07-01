from socket import *

s=socket(AF_INET, SOCK_STREAM)
s.bind(('192.168.139.132',5959))
s.listen(2)

user,addr= s.accept()
print(f"CONNECT:\n{user}\n{addr}")
user.send('You are connected'.encode('UTF-8'))
msg=user.recv(1024).decode('utf-8')
print(f'user msg:\n\t{msg}')