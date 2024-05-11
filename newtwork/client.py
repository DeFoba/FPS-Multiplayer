import socket
from threading import Thread
from modules.player import NetworkPlayer

HOST, PORT = '192.168.0.102', 5054
MY_ADDR = ''

net_players = {}

def start(player, face):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    def sending_data():
        global MY_ADDR

        addr = client.recv(1024).decode()
        MY_ADDR = addr

        while True:
            client.send(str(','.join([str(player.x), str(player.y), str(player.z), str(player.rotation.y), str(player.hand.rotation.x)])).encode())

            data = client.recv(1024)

            print(f'Data is: "{data.decode()}"')

            id, x, y, z, player_angle, hand_angle = [pos for pos in data.decode().split(',')]

            if not id in net_players:
                net_players[id] = NetworkPlayer()
                net_players[id].y = 1.8

            x, y, z, player_angle, hand_angle = float(x), float(y), float(z), float(player_angle), float(hand_angle)

            net_players[id].position = (x, y + 1.8, z)

            net_players[id].rotation = (0, player_angle, 0)
            net_players[id].hand.rotation = (hand_angle, 0, 0)
            net_players[id].monitor.rotation = (hand_angle, 0, 0)


    def client_start():
        Thread(target=sending_data, daemon=True).start()

    client_start()