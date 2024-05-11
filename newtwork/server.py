import socket
from threading import Thread
from modules.player import NetworkPlayer

HOST, PORT = '192.168.0.102', 5054

net_players_entity = []
net_players_clients = []
net_players = {}

def start(player, face):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    net_players['admin'] = [player, server]


    def accepted_player(client, addr):
        addr = str(addr)
        net_players[str(addr)] = [NetworkPlayer(), client]
        net_players_entity.append(net_players[str(addr)][0])
        net_players_clients.append(client)

        print('Connected addr:', addr)

        net_player, _ = net_players[addr]

        client.send(str(addr).encode())

        while True:
            data = client.recv(1024).decode()

            x, y, z, player_angle, hand_angle = [pos for pos in data.split(',')]
            x, y, z, player_angle, hand_angle = float(x), float(y), float(z), float(player_angle), float(hand_angle)

            net_player.position = (x, y + 1.8, z)

            net_player.rotation = (0, player_angle, 0)
            net_player.hand.rotation = (hand_angle, 0, 0)
            net_player.monitor.rotation = (hand_angle, 0, 0)

    
    def _thread_sending_all_positions():
        while True:
            # for addr in net_players:
            #     net_player, client = net_players[addr]

            for net_player in net_players_entity:

                for client in net_players_clients:
                    client.send(str(','.join([str('addr'), str(net_player.x), str(net_player.y), str(net_player.z), str(net_player.rotation.y), str(net_player.hand.rotation.x)])).encode())


    def loop_for_accepting():
        while True:
            Thread(target=accepted_player, args=server.accept(), daemon=True).start()


    def start_server():
        Thread(target=loop_for_accepting, daemon=True).start()
        Thread(target=_thread_sending_all_positions, daemon=True).start()

    start_server()