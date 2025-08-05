import socket

header = 64
port = 9090
format = 'utf-8'
disconnectMessage = 'Has disconnected.'
localServer = socket.gethostbyname(socket.gethostname())
addr = ('192.168.1.74', port)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(addr)

def send(msg):
    message = msg.encode(format)
    msgLength = len(message)
    sendLength = str(msgLength).encode(format)
    sendLength += b' ' * (header - len(sendLength)) 
    client.send(sendLength)
    client.send(message)

while True:
    message = input("Type message: ")
    send(message)