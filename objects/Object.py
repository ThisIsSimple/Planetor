import cocos
import cocos.euclid as eu
from math import sqrt, degrees, radians, atan, sin, cos

import pymunk

import statics.TAG as TAG

import PIL.ImageDraw as ImageDraw
import PIL.Image as Image


class Object(cocos.sprite.Sprite):

    @staticmethod
    def create_box_image(width, height):
        image = Image.new("RGB", (width, height))

        draw = ImageDraw.Draw(image)

        points = ((0, 0), (width, 0), (width, height), (0, height))
        draw.polygon((points), fill=200)

        return image

    def __init__(self, planet, image, name="", scale=1, gravity=False, angle=0, distance=0, collision_type=TAG.OBJECT):

        super(Object, self).__init__(image)

        self.name = name
        self.scale = scale

        self.center_direction = (0, 0)
        self.planet = planet

        self.gravity = gravity

        self.body = pymunk.Body(10, 1)

        self.shape = pymunk.Circle(self.body, self.width / 2)
        self.shape.collision_type = collision_type
        self.shape.object = self  # For external reference

        if not self.gravity:
            self.body.velocity_func = self.zero_gravity

        self.set_angle_distance(angle, distance)

    def update(self, elapsed):
        self.center_direction = ((self.planet.x - self.x) / self.get_distance(),
                                 (self.planet.y - self.y) / self.get_distance())

        if self.gravity:
            if self.grounded():
                self.body.velocity_func = self.zero_gravity
            else:
                self.body.velocity_func = self.planet_gravity

        self.position = self.body.position

        self.update_angle()

    def set_angle_distance(self, angle, distance):
        r = self.planet.radius + self.height / 2 + distance
        dx = cos(radians(angle)) * r
        dy = sin(radians(angle)) * r

        self.position = self.body.position = (
            self.planet.x + dx,
            self.planet.y + dy
        )

        self.update_angle()

    @staticmethod
    def zero_gravity(body, gravity, damping, dt):
        pymunk.Body.update_velocity(body, (0, 0), damping, dt)

    def planet_gravity(self, body, gravity, damping, dt):
        pymunk.Body.update_velocity(body, (self.center_direction[0] * self.planet.gravity, self.center_direction[1] * self.planet.gravity), damping, dt)

    def grounded(self):
        if self.get_distance() <= self.planet.width / 2 + self.height / 2 + 0.5:
            return True
        return False

    def update_angle(self):
        try:
            tan_a = (self.x - self.planet.x) / (self.y - self.planet.y)
            if (self.y - self.planet.y) > 0:
                self.rotation = degrees(atan(tan_a))
                self.shape.angle = atan(tan_a)
            else:
                self.rotation = 180 + degrees(atan(tan_a))
                self.shape.angle = radians(180) + atan(tan_a)
        except ZeroDivisionError:
            self.rotation = 0
            self.body.angle = 0

    def get_distance(self):
        return sqrt(pow((self.planet.x - self.x), 2) + pow((self.planet.y - self.y), 2))
