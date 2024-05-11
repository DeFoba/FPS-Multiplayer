import socket
from threading import Thread
from modules.player import NetworkPlayer

HOST, PORT = '192.168.0.101', 5054

net_players = {}

def start(player, face):
    net_players['admin'] = player
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    def accepted_player(client, addr):
        addr = str(addr)
        net_players[str(addr)] = [NetworkPlayer(), client]
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
            for addr in net_players:
                net_player, client = net_players[addr]
                clients = [net_players[adr][1] for adr in net_players]

                for client in clients:
                    client.sendall(str(','.join([str(addr), str(net_player.x), str(net_player.y), str(net_player.z), str(net_player.rotation.y), str(net_player.hand.rotation.x)])).encode())


    def loop_for_accepting():
        while True:
            Thread(target=accepted_player, args=server.accept(), daemon=True).start()


    def start_server():
        Thread(target=loop_for_accepting, daemon=True).start()
        Thread(target=_thread_sending_all_positions, daemon=True).start()

    start_server()