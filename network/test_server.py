import socket
from threading import Thread

HOST, PORT = '192.168.0.102', 5054

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []

def accept_addres(client, addr):
    clients.append(client)

    while True:
        try: data = client.recv(1024).decode()
        except: break

        print(f'from ({addr}) get message: "{data}"')

        for _client in clients:
            _client.send(f'from ({addr}) get message: "{data}"'.encode())

def loop_connection():
    while True:
        Thread(target=accept_addres, args=server.accept(), daemon=True).start()

if __name__ == '__main__':
    Thread(target=loop_connection).start()