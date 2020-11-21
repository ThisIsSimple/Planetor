import cocos
import math


class Creature(cocos.sprite.Sprite):
    def __init__(self, planet, x, y, gravity=True):
        super(Creature, self).__init__(image="assets/box.png")

        self.planet = planet

        self.position = (320, 300)
        self.gravity = gravity

        self.update_angle()

    def move(self, angle, distance):
        pass

    def update(self, elapsed):
        if self.gravity:
            if self.get_distance() > self.planet.radius:
                pass
        pass

    def update_angle(self):
        tan = (self.planet.x - self.x) / (self.planet.y - self.y)
        self.rotation = math.degrees(math.atan(tan))

    def get_distance(self):
        return math.sqrt(math.pow((self.planet.x - self.x), 2) + math.pow((self.planet.y - self.y), 2))
