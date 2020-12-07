import cocos
import cocos.euclid as eu
from math import sqrt, degrees, radians, atan, sin, cos

from objects.Planet import Planet
from objects.Object import Object
from objects.Building import Building
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
        self.building_name_label.element.text = arbiter.shapes[1].object.name
        arbiter.shapes[1].object.show_name()
        return False

    def collide_end_building(self, arbiter, space, data):
        self.building_name_label.element.text = ""
        arbiter.shapes[1].object.hide_name()
        return False

    def collide_with_planet(self, arbiter, space, data):
        arbiter.shapes[0].object.on_ground = True
        return True

    def collide_between_building(self, arbiter, space, data):
        return False

    def __init__(self):
        super(GameLayer, self).__init__()

        self.space = pymunk.Space()
        self.space.gravity = (0, 0)

        # Collision Setting
        self.ch1 = self.space.add_collision_handler(TAG.PLAYER, TAG.BUILDING)
        self.ch1.begin = self.collide_with_building
        self.ch1.separate = self.collide_end_building

        self.ch2 = self.space.add_collision_handler(TAG.PLAYER, TAG.PLANET)
        self.ch2.begin = self.collide_with_planet

        self.ch3 = self.space.add_collision_handler(TAG.BUILDING, TAG.BUILDING)
        self.ch3.begin = self.collide_between_building

        # UI 화면 중심 좌표를 기준으로 위치 지정
        self.UI_objects = []

        self.planet_name_label = cocos.text.Label("Planet Name", anchor_x="center", font_size=12)
        self.UI_objects.append({
            'position': (0, -215),
            'object': self.planet_name_label
        })

        self.building_name_label = cocos.text.Label("_", anchor_x="center", font_size=11)
        self.building_name_label.element.text = ""
        self.UI_objects.append({
            'position': (0, 215),
            'object': self.building_name_label
        })

        self.tooltip_label = cocos.text.Label("", anchor_x="right", font_size=10)
        self.UI_objects.append({
            'position': (300, -215),
            'object': self.tooltip_label
        })

        # Planet & Creatures & Buildings
        self.updateable_objects = []

        p = Planet(image="assets/images/planets/Baren.png", name="화산 행성", scale=0.3)
        self.updateable_objects.append(p)

        k = Planet(image="assets/images/planets/Ice.png", name="물 행성", scale=0.5, position=(400, 300))
        self.updateable_objects.append(k)

        self.updateable_objects.append(
            Building(planet=p, image="assets/images/Tree.png", name="촌장의 집", angle=45))

        self.updateable_objects.append(
            Building(planet=p, image="assets/images/House1.png", name="촌장의 집", angle=30))

        self.updateable_objects.append(
            Building(planet=p, image="assets/images/House3.png", name="촌장의 집", angle=10))

        self.updateable_objects.append(
            Building(planet=p, image="assets/images/Spaceship.png", name="우주선", angle=90))

        self.updateable_objects.append(
            Building(planet=p, image="assets/images/Factory.png", name="우주선", angle=-20, distance=0))

        self.player = Player(planet=p)
        self.updateable_objects.append(self.player)

        # Add Updateable Objects
        for item in self.updateable_objects:
            self.add(item)
            self.space.add(item.body, item.shape)

        # Add UI Objects
        for item in self.UI_objects:
            self.add(item['object'], z=100)

        self.schedule(self.update)

    def update(self, dt):
        self.space.step(dt)

        self.camera.center = eu.Point3(self.player.position[0], self.player.position[1], 0)
        self.camera.eye = eu.Point3(self.player.position[0], self.player.position[1], self.camera.eye[2])

        self.update_ui_position()

        for child in self.updateable_objects:
            child.update(dt)

    def update_ui_position(self):
        for item in self.UI_objects:
            item['object'].position = (self.camera.center[0] + item['position'][0],
                                       self.camera.center[1] + item['position'][1])
