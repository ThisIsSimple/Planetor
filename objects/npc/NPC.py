import cocos

from objects.Creature import Creature

from statics import TAG


class NPC(Creature):
    def __init__(self, planet, image, name, gravity=True, angle=0, distance=0, collision_type=TAG.CREATURE):
        super(NPC, self).__init__(planet=planet, image=image, name=name, gravity=gravity, angle=angle,
                                  distance=distance, collision_type=collision_type)

    def interact(self):
        pass
