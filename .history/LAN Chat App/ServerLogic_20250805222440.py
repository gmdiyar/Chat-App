import socket
import threading
import json

host = socket.gethostbyname(socket.gethostname())
port = 5050

class Server:
    
    def __init__(self, message_callback=None):
        self.__connected = False
        self.message_callback = message_callback
        self.clients = []
        self.client_usernames = {}

    def initiateMultiThreading(self):
        thread = threading.Thread(target=self.startServer)
        thread.daemon = True
        thread.start()

    def startServer(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.server.bind((host, port))
            self.server.listen(5)
            self.__connected = True
            print(f"Successfully connected on {host}: {port}\n")
            while  self.__connected:
                client, addr = self.server.accept()
                print(f"New connection on {addr}\n")
                self.clients.append(client)
                client_thread = threading.Thread(target=self.clientHandler, args=(client, addr))
                client_thread.daemon = True
                client_thread.start()

        except Exception as e:
            print(f'Failed to start server: {e}')
    
    def clientHandler(self, client, addr):
        try:
            loginData = client.recv(1024).decode('utf-8')
            loginJSON = json.loads(loginData)
            if loginJSON.get('type') == 'login':
                username = loginJSON.get('username')
                self.client_usernames[client] = username
                print(f'{username} connected from {addr}')
            else:
                print('Expected login message, closing.')
                client.close()
                return
            while True:
                self.data = client.recv(1024)
                if not self.data:
                    print(f"{self.client_usernames.get(client)} disconnected.")
                    break
                try:
                    message_json = json.loads(data.decode('utf-8'))
                    if message_json.get('type') == 'message':
                        message_text = message_json.get('message')
                        print(f'{self.client_usernames[client]}: {message_text}')
                        self.relayMessage(message_text, sender=client)
                except json.JSONDecodeError:
                    print('Invalid message format.')

                self.relayMessage(message_text, sender=client)

                if self.message_callback:
                    self.message_callback(f'{addr}: {message}')
                    
        except Exception as e:
            print(f"{addr}: {e}\nACTIVE USERS: {threading.active_count() -3}")

        finally:
            self.clients.remove(client)
            self.client_usernames.pop(client, None)
            client.close()

    def sendMessage(self, recipient):
        #TODO probably make it client side, idk yet. 
        pass

    def relayMessage(self, message, sender):
        senderUsername = self.client_usernames.get(sender, 'Anonymous')

        for client in self.clients:
            if client != sender:
                try:
                    relay_payload = json.dumps({
                        'type': 'message',
                        'from': senderUsername,
                        'message': message
                    })
                    client.send(relay_payload.encode('utf-8'))
                except Exception as e:
                    print(f'Error sending to {self.client_usernames.get(client, 'Unknown')}: {e}')
                    self.clients.remove(client)
                    self.client_usernames.pop(client, None)

    def checkConnection(self):
        return True if self.__connected else False
