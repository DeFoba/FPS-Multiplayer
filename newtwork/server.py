import socket
from threading import Thread
from modules.player import NetworkPlayer

HOST, PORT = '192.168.0.101', 5054

def start(player):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    def accepted_player(client, addr):
        print('Connected addr:', addr)
        net_player = NetworkPlayer()

        while True:
            data = client.recv(1024).decode()

            # print(data)
            # print([player.x, player.y, player.z])
            # print(str(','.join([player.x, player.y, player.z])))

            x, y, z, player_angle, hand_angle = [float(pos) for pos in data.split(',')]
            net_player.position = (x, y + 1, z)

            net_player.rotation = (0, player_angle, 0)
            net_player.hand.rotation = (hand_angle, 0, 0)

            client.send(str(','.join([str(player.x), str(player.y), str(player.z), str(player.rotation.y), str(player.hand.rotation.x)])).encode())


    def loop_for_accepting():
        while True:
            Thread(target=accepted_player, args=server.accept(), daemon=True).start()


    def start_server():
        Thread(target=loop_for_accepting, daemon=True).start()

    start_server()