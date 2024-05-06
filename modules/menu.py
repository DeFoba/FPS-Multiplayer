from ursina import Button, Entity

class Menu(Entity):
    def __init__(self):
        super().__init__()

        from modules.world import ground
        # player = Player()