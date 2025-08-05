import socket
import threading 

header = 64
port = 5050
localServer = socket.gethostbyname(socket.gethostname())
format = 'utf-8'
disconnectMessage = 'Has disconnected.'

serverInstance = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = (localServer, port)
serverInstance.bind(addr)

def handleClient(connection, addr):
    print(f'New connection: {addr}')

    connected = True
    while connected:
        msgLength = connection.recv(header).decode(format)
        if msgLength:
            msg_length = int(msgLength)
            msg = connection.recv(msg_length).decode(format)
            if msg == disconnectMessage:
                connected = False

            print(f'{addr}: {msg}')
    connection.close()

def start():
    serverInstance.listen()
    print('Server is up! listening on', localServer)
    while True:
        connection, addr = serverInstance.accept()
        thread = threading.Thread(target=handleClient, args=(connection, addr))
        thread.start()
        print('Active Connections:', threading.active_count() - 1)

print('Server is starting...')
start()