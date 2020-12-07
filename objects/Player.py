from collections import defaultdict
from pyglet.window import key

from objects.Creature import Creature

import cocos

from statics import TAG


class Player(Creature):
    KEY_PRESSED = defaultdict(int)

    def __init__(self, planet, image="assets/box.png", gravity=True, angle=0, distance=0, collision_type=TAG.PLAYER):
        super(Creature, self).__init__(planet=planet, image=image, gravity=gravity, angle=angle, distance=distance,
                                       collision_type=collision_type)

        self.move_speed = 50
        self.jump_force = 600
        self.jumping = True

        self.on_ground = False

        self.shape.elasticity = 0

    def update(self, elapsed):
        pressed = Player.KEY_PRESSED

        movement = pressed[key.D] - pressed[key.A]
        jump = pressed[key.W]

        self.center_direction = ((self.planet.x - self.x) / self.get_distance(),
                                 (self.planet.y - self.y) / self.get_distance())

        if self.on_ground:
            self.body.velocity_func = self.zero_gravity
            if self.jumping:
                self.jumping = False
            if not jump:
                self.body.velocity = (0, 0)
        else:
            self.body.velocity_func = self.planet_gravity

        self.position = self.body.position

        self.update_angle()

        if movement:
            self.move(30 * movement, elapsed)
        if jump:
            if self.on_ground and not self.jumping:
                self.body.apply_impulse_at_local_point(
                    (self.center_direction[0] * -1 * self.jump_force, self.center_direction[1] * -1 * self.jump_force),
                    (0, 0))
                self.jumping = True
                self.on_ground = False
