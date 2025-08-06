import socket
import threading
from ClientGUI import username

host = socket.gethostbyname(socket.gethostname())
port = 5050

class Server:
    
    def __init__(self, message_callback=None):
        self.__connected = False
        self.message_callback = message_callback

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
                print(f"New connection on {addr}\nUser: {ClientInstance}")
                client_thread = threading.Thread(target=self.clientHandler, args=(client, addr))
                client_thread.daemon = True
                client_thread.start()

        except Exception as e:
            print(f'Failed to start server: {e}')
    
    def clientHandler(self, client, addr):
        try:
            while True:
                self.data = client.recv(1024)
                if not self.data:
                    print(f"connection closed by {self.addr}\n")
                    break
                message = self.data.decode('utf-8')
                print(f"{addr}: {message}")

                if self.message_callback:
                    self.message_callback(f'{addr}: {message}')
                    
        except Exception as e:
            print(f"{addr}: {e}\nACTIVE USERS: {threading.active_count() -3}")

        finally:
            client.close()

    def sendMessage(self, recipient):
        #TODO probably make it client side, idk yet. 
        pass

    def checkConnection(self):
        return True if self.__connected else False
