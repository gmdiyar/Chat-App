import socket

header = 64
port = 5050
format = 'utf-8'
disconnectMessage = 'Has disconnected.'
localServer = socket.gethostbyname(socket.gethostname())
addr = ('192.168.1.7', port)

class Client:

    def __init__(self, user):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(addr)

    def send(msg):
        message = msg.encode(format)
        msgLength = len(message)
        sendLength = str(msgLength).encode(format)
        sendLength += b' ' * (header - len(sendLength)) 
        #client.send(sendLength)
        self.client.send(message)

    while True:
        message = input("Type message: ")
        send(message)