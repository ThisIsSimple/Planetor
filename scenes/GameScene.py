import cocos
import cocos.euclid as eu
from math import sqrt, degrees, radians, atan, sin, cos

from objects.Planet import Planet
from objects.Object import Object
from objects.Player import Player

import pymunk

import statics.TAG as TAG

from collections import defaultdict
from pyglet.window import key

import PIL.ImageDraw as ImageDraw
import PIL.Image as Image


class GameLayer(cocos.layer.Layer):
    is_event_handler = True

    def on_key_press(self, k, _):
        Player.KEY_PRESSED[k] = 1

    def on_key_release(self, k, _):
        Player.KEY_PRESSED[k] = 0

    def collide_with_building(self, arbiter, space, data):
        return False

    def collide_with_planet(self, arbiter, space, data):
        arbiter.shapes[0].object.on_ground = True
        return True

    def __init__(self):
        super(GameLayer, self).__init__()

        self.space = pymunk.Space()
        self.space.gravity = (0, 0)

        self.ch1 = self.space.add_collision_handler(TAG.PLAYER, TAG.BUILDING)
        self.ch1.begin = self.collide_with_building

        self.ch2 = self.space.add_collision_handler(TAG.PLAYER, TAG.PLANET)
        self.ch2.begin = self.collide_with_planet

        p = Planet(scale=3)
        self.add(p)
        self.space.add(p.body, p.shape)

        self.t = Object(planet=p, image="assets/house.png", angle=45, collision_type=TAG.BUILDING)
        self.add(self.t)
        self.space.add(self.t.body, self.t.shape)

        self.player = Player(p)
        self.add(self.player)
        self.space.add(self.player.body, self.player.shape)

        self.schedule(self.update)

    def update(self, dt):
        self.space.step(dt)

        self.camera.center = eu.Point3(self.player.position[0], self.player.position[1], 0)
        self.camera.eye = eu.Point3(self.player.position[0], self.player.position[1], self.camera.eye[2])

        for child in self.children:
            child[1].update(dt)
