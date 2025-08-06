import socket
import threading
import json

header = 64
port = 5050
format = 'utf-8'
disconnectMessage = 'Has disconnected.'
localServer = socket.gethostbyname(socket.gethostname())
addr = ('192.168.1.74', port)

class Client:

    def __init__(self, user, message_callback=None):
        self.username = user.username
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(addr)
        self.message_callback = message_callback
        self.running = True

        loginPayload = json.dumps({
            'type': 'login',
            'username': self.username
        })
        self.client.send(loginPayload.encode(format))

        thread = threading.Thread(target=self.receive_loop, daemon=True)
        thread.start()

    def send(self, msg):
        messagePayload = json.dumps({
            'type': 'message',
            'username': self.username,
            'content': msg
        })
        self.client.send(messagePayload.encode(format))

    def getMessageLength(self):
        msgLength = len(self.message)
        sendLength = str(msgLength).encode(format)
        sendLength += b' ' * (header - len(sendLength))
        self.client.send(sendLength)

    def receive_loop(self):
        while self.running:
            try:
                data = self.client.recv(1024)
                if not data:
                    break

                message_json = json.loads(data.decode('utf-8'))

                # Check if it's a normal chat message
                if message_json.get("type") == "message":
                    sender = message_json.get("from", "Unknown")
                    message = message_json.get("content", "")
                    formatted_message = f"{sender}: {message}"

                    if self.message_callback:
                        self.message_callback(formatted_message)

                # Optional: handle login acknowledgments, etc.
                elif message_json.get("type") == "system":
                    note = message_json.get("message", "")
                    if self.message_callback:
                        self.message_callback(f"[SYSTEM] {note}")

            except Exception as e:
                print(f"Error in receive_loop: {e}")
                break
    def stop(self):
        self.running = False
        self.client.close()