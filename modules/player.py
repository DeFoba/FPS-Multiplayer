from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.health_bar import HealthBar
from ursina import Entity, color, camera, Text


class Hand(Entity):
    def __init__(self):
        super().__init__()

        self.model = 'cube'
        self.scale = (0.2, 0.2, 1)
        self.position = (0.5, 1.8, 0.2)
        # self.position = (0.5, 0, 0)
        self.origin = (0, 0, -.6)

class Wheel(Entity):
    def __init__(self):
        super().__init__()

        self.model = 'models/player/robot-weels'
        self.texture = 'models/player/WheelsTex'
        self.scale = .8
        self.origin = (0, 0, 0)
        self.y = -.9


class Player(FirstPersonController):
    def __init__(self):
        super().__init__()
        self.hp = HealthBar()

        self.hand = Hand()
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
    def __init__(self, nickname='0_0'):
        super().__init__(collider='box')

        self.model = 'models/player/robot'
        self.texture = 'models/player/robot'
        # self.scale = (1, 2, 1)
        self.scale = .7
        self.position = (0, 1, 0)

        self.nickname = nickname

        self.hand = Hand()
        self.hand.parent = self

        self.wheel = Wheel()
        self.wheel.parent = self

        self.face = Text(parent=self, text=self.nickname, position=(0, 1.5, 1.2), scale=20, rotation=(0, self.rotation_y, 0), origin=(0, 0, 0))
        self.face.rotation = (0, self.rotation_y + 180, 0)

        self.color = color.random_color()

        self.hand.scale = (0.2, 0.2, 1.3)
        self.hand.color = self.color
        self.hand.y = self.y + .3
        self.hand.x += .7

    def update(self):
        pass