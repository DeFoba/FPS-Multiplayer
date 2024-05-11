import socket
from threading import Thread

HOST, PORT = '192.168.0.102', 5054

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))


def start():
    client.sendall(b'Hello everyone!')
    while True:
        data = client.recv(1024).decode()
        print(f'from (server) get message: "{data}"')


if __name__ == '__main__':
    Thread(target=start).start()