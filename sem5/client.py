import socket
from _thread import start_new_thread

client= socket.socket()

client.connect(('192.168.210.68', int(3000)))

data = client.recv(1024)
print('code:', data)
print('message:', data.decode())

message = 'helo serv'
data = message.encode()
client.send(data)

def getMessages():
    while True:
        data = client.recv(1024)
        print('Input', data.decode())
        if data.decode() == 'Close!':
            break
    client.close()

start_new_thread(getMessages, ())    

while True:
    message = input('Input your message:')
    data = message.encode()
    client.send(data)
    if message == 'Close!':
        break

client.close()