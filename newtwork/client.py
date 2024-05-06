import socket
from threading import Thread
from modules.player import NetworkPlayer

HOST, PORT = '192.168.0.101', 5054

def start(player):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    def sending_data():
        net_player = NetworkPlayer()

        while True:
            # print([player.x, player.y, player.z])
            # print(str(','.join([player.x, player.y, player.z])))
            client.send(str(','.join([str(player.x), str(player.y), str(player.z), str(player.rotation.y), str(player.hand.rotation.x)])).encode())

            data = client.recv(1024)
            # print(data)

            x, y, z, player_angle, hand_angle = [float(pos) for pos in data.decode().split(',')]
            net_player.position = (x, y + 1, z)

            net_player.rotation = (0, player_angle, 0)
            net_player.hand.rotation = (hand_angle, 0, 0)

            # print(x, y, z)

    def client_start():
        Thread(target=sending_data, daemon=True).start()

    client_start()