from ursina import Ursina, camera, Text, Vec3, Entity
from modules.player import Player, NetworkPlayer


app = Ursina(borderless=False, size=(600, 500))
# app = Ursina(borderless=False)
MODE = None



from modules.world import ground
player = Player()


def input(key):
    global MODE

    if MODE == None:
            if key == 'x':
                MODE = True
                import newtwork.server
                newtwork.server.start(player)

            if key == 'c':
                MODE = True
                import newtwork.client
                newtwork.client.start(player)

# NetworkPlayer()

if __name__ == '__main__':
    app.run()