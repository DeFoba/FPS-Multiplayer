from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.health_bar import HealthBar
from ursina import Entity, color, camera, Text


class Hand(Entity):
    def __init__(self):
        super().__init__()

        self.model = 'cube'
        self.scale = (0.2, 0.2, 1)
        # self.position = (0.5, 1.8, 0.2)
        # self.position = (0.5, 0, 0)
        self.origin = (0, 0, -.6)

class PlayerHand(Entity):
    def __init__(self):
        super().__init__()

        self.model = 'cube'
        self.scale = (0.2, 0.2, 1)
        self.position = (0.5, 1.8, 0.2)
        # self.position = (0.5, 0, 0)
        self.origin = (0, 0, -.6)

    # def update(self):
    #     self.rotation_x += 1

class Wheel(Entity):
    def __init__(self):
        super().__init__()

        self.model = 'models/player/robot-weels'
        self.texture = 'models/player/textures/WheelsTex'
        self.scale = (1.1, 2, 2)
        self.origin = (0, 0, 0)
        self.y = -.9

class Monitor(Entity):
    def __init__(self, nickname):
        super().__init__()

        self.model = 'models/player/RobotMonitor'
        self.texture = 'models/player/textures/RobotMonitorTex'
        self.scale = 1
        self.origin = (0, 0, 0)

        self.nickname = nickname

        self.face = Text(parent=self, text=self.nickname, position=(0, 0, 1.8), scale=20, rotation=(0, self.rotation_y, 0), origin=(0, 0, 0))
        self.face.rotation = (0, self.rotation_y + 180, 0)

    # def update(self):
    #     self.rotation_x += 1



class Player(FirstPersonController):
    def __init__(self):
        super().__init__()
        self.hp = HealthBar()

        self.hand = PlayerHand()
        self.hand.parent = self
        # self.hand.parent = self.camera_pivot

    def update(self):
        self.hand.rotation = self.camera_pivot.rotation

        return super().update()

    def input(self, key):
        if key == 'q':
            exit()

        if key == 'space':
            self.jump()


class NetworkPlayer(Entity):
    def __init__(self, nickname='0_0', pl_color=color.random_color()):
        super().__init__(collider='box')

        self.color = pl_color

        self.model = 'models/player/RobotBody'
        self.texture = 'models/player/textures/RobotBodyTex'
        # self.scale = (1, 2, 1)
        self.scale = .4
        self.position = (0, 1.8, 0)

        self.nickname = nickname

        self.hand = Hand()
        self.hand.parent = self

        self.wheel = Wheel()
        self.wheel.parent = self
        self.wheel.position = (0, -3, 0)

        self.monitor = Monitor(self.nickname)
        self.monitor.parent = self
        self.monitor.color = self.color
        self.monitor.position = (0, 0, 0)



        self.hand.scale = (0.2, 0.2, 1.3) * 2
        self.hand.position = (3, 0, 0)
        self.hand.color = self.color

    def update(self):
        pass