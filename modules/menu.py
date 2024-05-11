from ursina import Button, Entity, camera, color, InputField

class Menu(Entity):
    def __init__(self):
        super().__init__()

        
        self.background = Entity(model='quad', scale=(15, 10, 1), rotation=(90, 0, 0), color=color.rgb(44, 154, 142), double_sided=True)
        self.background.texture = 'textures/wood_wall'
        self.background.texture_scale = (3, 3)
        self.background.look_at(camera)

        self.nickname = InputField('0_0', character_limit=5, position=(0, .2, 0), scale=(.3, .1))

        self.btn_server = Button('Create', scale=(.3, .1), position=(0, .05, 0))
        self.btn_server.on_click = lambda: self.start_game(True)

        self.btn_client = Button('Join', scale=(.3, .1), position=(0, -.07, 0))
        self.btn_client.on_click = lambda: self.start_game(False)


    def start_game(self, is_server):
        from modules.world import ground, player

        self.ground = ground
        self.player = player

        self.background.disable()
        self.btn_client.disable()
        self.btn_server.disable()
        self.nickname.disable()

        if is_server: self.command_server()
        else: self.command_client()

    def command_server(self):
        import network.server
        network.server.start(self.player, self.nickname.text)

    def command_client(self):
        import network.client
        network.client.start(self.player, self.nickname.text)