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

    def getMessageLength(self):
        msgLength = len(self.message)
        sendLength = str(msgLength).encode(format)
        sendLength += b' ' * (header - len(sendLength))
client.send(sendLength)
    def send(self, msg):
        self.message = msg.encode(format)
        #client.send(sendLength)
        self.client.send(self.message)
    def mainLoop(self):
        while True:
            message = input("Type message: ")
            send(self.message)