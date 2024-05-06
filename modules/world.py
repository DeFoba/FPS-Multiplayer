from ursina import Entity, DirectionalLight, AmbientLight, Vec3
from ursina.shaders.lit_with_shadows_shader import lit_with_shadows_shader
from modules.player import Player

# from modules.world import ground
player = Player()

ground = Entity(model='plane', texture='textures/wood_ground', texture_scale=(8, 8), position=(0, 0, 0), scale=20, collider='box', rotation=(0, 0, 0), shader=lit_with_shadows_shader)

# block = Entity(model='cube', collider='box', position=(1, 1, 1), shader=lit_with_shadows_shader)
# sphere = Entity(model='sphere', collider='box', position=(2, 1, 1), shader=lit_with_shadows_shader)


# pivot = Entity()

# AmbientLight(color=(0.5, 0.5, 0.5, 1))
# sun = DirectionalLight(parent=pivot, color=(0.5, 0.5, 0.5, 1), shadows=True, position=(5, 3, 3), direction=(1, 1, 1))


# sun.look_at(Vec3(1, -1, 1))