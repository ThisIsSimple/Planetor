import cocos
from cocos.actions import FadeIn, FadeOut, Hide, Show

from objects.Object import Object

import statics.TAG as TAG


class Building(Object):
    def __init__(self, planet, image, name, gravity=False, angle=0, distance=0, collision_type=TAG.BUILDING):
        super(Building, self).__init__(planet=planet, image=image, gravity=gravity, angle=angle, distance=distance, collision_type=collision_type)

        self.name = name
        self.name_label = cocos.text.RichLabel(self.name, position=(0, 0), anchor_x="center", anchor_y="center", font_size=9)
        self.add(self.name_label, z=10000)
        self.name_label.do(FadeOut(0))

    def show_name(self):
        self.name_label.do(FadeIn(0.15))

    def hide_name(self):
        self.name_label.do(FadeOut(0.15))
