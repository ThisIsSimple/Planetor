from objects.Object import Object

import cocos
import cocos.euclid as eu
from math import sqrt, degrees, radians, atan, sin, cos

import pymunk

import statics.TAG as TAG


class Creature(Object):

    def __init__(self, planet, image, gravity=True, angle=0, distance=0, collision_type=TAG.CREATURE):
        super(Creature, self).__init__(planet=planet, image=image, gravity=gravity, angle=angle, distance=distance, collision_type=collision_type)

    def move(self, angle, elapsed):
        angle = -1 * radians(angle) * elapsed

        x = self.x - self.planet.x
        y = self.y - self.planet.y
        rotate = (
            x * cos(angle) - y * sin(angle),
            x * sin(angle) + y * cos(angle)
        )
        new_pos = (self.planet.x + rotate[0], self.planet.y + rotate[1])

        self.body.position = new_pos
