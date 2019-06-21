import socket

host = '192.168.1.6'
port = 3000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (host,port)

s.connect(dest)
print('Conectado com ',host)

rec = s.recv(1024)
rec = rec.decode('ascii')
print(rec)

msg = input()
msg = msg.encode('ascii')

while True:
    s.send(msg)
    msg = input()
    msg = msg.encode('ascii')
    
s.close()
