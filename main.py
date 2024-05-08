from ursina import Ursina, camera, Text, Vec3, Entity
from modules.player import Player, NetworkPlayer
from modules.menu import Menu


# app = Ursina(borderless=False, size=(600, 500))
app = Ursina(borderless=False)
MODE = None



# from modules.world import ground
# player = Player()
menu = Menu()

NetworkPlayer()

if __name__ == '__main__':
    app.run()