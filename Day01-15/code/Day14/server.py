import socket
 
s = socket.socket()
s.bind(('127.0.0.1', 12345))
 
s.listen(5)
while True:
    c,addr = s.accept()
    print ('addr:', addr)
    c.send('hello yyc'.encode())
    c.close()