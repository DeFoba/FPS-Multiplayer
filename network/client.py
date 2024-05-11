import socket
from threading import Thread
from modules.player import NetworkPlayer
from network.config import HOST, PORT

players = []

def start(player, face):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    def sending_data():
        count = client.recv(1024).decode()

        while True:
            client.send(player.send_value.encode())

            try: data = client.recv(1024).decode()
            except: break

            datas = data.split('\n')

            if len(datas) > len(players):
                players.append(NetworkPlayer())

            players_count = 0
            for net_player in players:
                net_player.from_text_to_move(datas[players_count])
                players_count += 1




    def client_start():
        Thread(target=sending_data, daemon=True).start()

    client_start()