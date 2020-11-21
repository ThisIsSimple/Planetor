import cocos
from objects.Creature import Creature

from collections import defaultdict
from pyglet.window import key


class Player(Creature):
    KEY_PRESSED = defaultdict(int)

    def __init__(self, planet):
        super(Player, self).__init__(planet, 100, 100)

        self.speed = 50

    def move(self, angle, distance):



        pass

    def update(self, elapsed):
        pressed = Player.KEY_PRESSED

        movement = pressed[key.RIGHT] - pressed[key.LEFT]
        movement2 = pressed[key.UP] - pressed[key.DOWN]

        self.x += movement * elapsed * self.speed
        self.y += movement2 * elapsed * self.speed
        self.update_angle()

    def gravity(self):

        pass
