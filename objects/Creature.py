import cocos
import math


class Creature(cocos.sprite.Sprite):
    def __init__(self, planet, x, y):
        super(Creature, self).__init__(image="assets/box.png")

        self.planet = planet

        self.position = (320, 300)

        self.update_angle()

    def move(self, angle, distance):
        pass

    def update(self, elapsed):
        pass

    def update_angle(self):
        tan = (self.planet.x - self.x) / (self.planet.y - self.y)
        self.rotation = math.degrees(math.atan(tan))
