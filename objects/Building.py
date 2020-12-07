import cocos
from cocos.actions import FadeIn, FadeOut, Hide, Show

import pymunk

from objects.Object import Object

import statics.TAG as TAG


class Building(Object):
    def __init__(self, planet, image, name, scale=1, gravity=False, angle=0, distance=0, collision_type=TAG.BUILDING):
        super(Building, self).__init__(planet=planet, scale=scale, image=image, name=name, gravity=gravity, angle=angle, distance=distance, collision_type=collision_type)

        points = [(-self.width/2, -self.height/2), (-self.width/2, self.height/2), (self.width/2, self.height/2), (self.width/2, -self.height/2)]
        self.shape = pymunk.Poly(self.body, points)
        self.shape.collision_type = collision_type
        self.shape.object = self

        self.name_label = cocos.text.RichLabel(self.name, position=(0, self.height / 2), anchor_x="center", anchor_y="center", font_size=9)
        self.add(self.name_label, z=10000)
        self.name_label.do(FadeOut(0))

    def show_name(self):
        self.name_label.do(FadeIn(0.15))

    def hide_name(self):
        self.name_label.do(FadeOut(0.15))
