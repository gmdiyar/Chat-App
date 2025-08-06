import socket
import threading

header = 64
port = 5050
format = 'utf-8'
disconnectMessage = 'Has disconnected.'
localServer = socket.gethostbyname(socket.gethostname())
addr = ('192.168.1.74', port)

class Client:

    def __init__(self, user, message_callback=None):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(addr)
        self.message_callback = message_callback
        self.running = True

        thread = threading.Thread(target=self.receive_loop, daemon=True)
        thread.start()

    def send(self, msg):
        encoded = msg.encode(format)
        self.client.send(self.message)

    def getMessageLength(self):
        msgLength = len(self.message)
        sendLength = str(msgLength).encode(format)
        sendLength += b' ' * (header - len(sendLength))
        self.client.send(sendLength)

    def receive_loop(self):
        while self.running:
            try:
                message = self.client.recv(1024).decode(format)
                if self.message_callback:
                    self.message_callback(message)
            exc