import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.1.6'
#host = socket.gethostbyname(socket.gethostname())
port = 3000
orig = (host,port)
env = 'Eae cliente'

s.bind(orig)
s.listen(3)
print('***Servidor rodando***/n')
while True:
    con, client = s.accept()
    print('Conectado por ', client)
    env = env.encode('ascii')
    con.send(env)
    while True:
        msg = con.recv(1024)
        msg = msg.decode('ascii')
        print(client, msg)
        
    con.close()
