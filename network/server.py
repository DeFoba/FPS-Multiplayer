import socket
from threading import Thread
from modules.player import NetworkPlayer
from network.config import HOST, PORT
from time import sleep

players = {}
clients = []

def start(player, face):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    def accepted_player(client, addr):
        
        print('Connected addr:', addr)

        net_player = NetworkPlayer()
        players[str(addr)] = net_player

        clients.append(client)
        client.send(str(addr).encode())

        # count += 1

        while True:
            try: data = client.recv(1024).decode()
            except: break

            net_player.from_text_to_move(data)

    
    def _thread_sending_all_positions():
        while True:
            message = ''
            for name in players:
                message += players[name].send_value + '\n'
            
            for client in clients:
                client.send(message.encode())

            sleep(1)
            


    def loop_for_accepting():
        while True:
            Thread(target=accepted_player, args=server.accept(), daemon=True).start()


    def start_server():
        Thread(target=loop_for_accepting, daemon=True).start()
        Thread(target=_thread_sending_all_positions, daemon=True).start()

    start_server()