import cocos

import pymunk

import statics.TAG as TAG


class Planet(cocos.sprite.Sprite):
    def __init__(self, image, name, gravity=100, position=(0, 0), scale=1):
        super(Planet, self).__init__(image)

        self.name = name
        self.gravity = gravity
        self.scale = scale

        self.radius = self.width / 2

        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.body.position = self.position = position

        self.shape = pymunk.Circle(self.body, self.width / 2)
        self.shape.collision_type = TAG.PLANET

    def update(self, elapsed):
        self.position = self.body.position
