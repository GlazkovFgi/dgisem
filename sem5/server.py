import socket
from _thread import start_new_thread

server = socket.socket()

server.bind(('192.168.210.68', 3000))

server.listen(5)
print(server)

con, addr = server.accept()
message = 'helo serv'
data = message.encode()
con.send(data)

def getMessages():
    while True:
        data = con.recv(1024)
        print('Input', data.decode())
        if data.decode() == 'Close!':
            break
    con.close()
    server.close()

start_new_thread(getMessages,())

print('connection_con', con)
print('connection_addr', addr)

while True:
        data = con.recv(1024)
        print('Input', data.decode())
        if data.decode() == 'Close!':
            break
con.close()
server.close()