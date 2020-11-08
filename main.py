import cocos
from cocos import draw
import cocos.collision_model as cm
from cocos.euclid import Vector2

import pyglet
from pyglet import shapes

from collections import defaultdict
from pyglet.window import key


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


class MainLayer(cocos.layer.Layer):
    def __init__(self):
        super(MainLayer, self).__init__()

        line = draw.Line((0, 0), (550, 450), (255, 255, 255, 255))
        self.add(line)

        # circle = draw.Circle(Vector2(300, 300), 10.0)
        # self.add(circle)

        player = Player()
        self.add(player)

        planet = Planet((10, 10))
        self.add(planet)

        self.schedule(self.update)

    def update(self, dt):
        pass


class Actor(cocos.sprite.Sprite):
    def __init__(self, image, position, color=None):
        if color:
            super(Actor, self).__init__(image, position, color=color)
        else:
            super(Actor, self).__init__(image, position)

        self.position = position
        cm.CircleShape(self.position, self.width * 0.5)


class Planet(Actor):
    def __init__(self, position, color=None):
        if color:
            super(Planet, self).__init__("assets/planet.png", position=position, color=color)
        else:
            super(Planet, self).__init__("assets/planet.png", position=position)


class Player(Actor):
    def __init__(self):
        super(Player, self).__init__("assets/planet.png", position=(100, 100))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cocos.director.director.init(caption='Planetor')
    mainLayer = MainLayer()
    scene = cocos.scene.Scene(mainLayer)
    cocos.director.director.run(scene)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
