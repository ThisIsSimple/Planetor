import cocos
from cocos import draw

import pyglet
from pyglet import shapes

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


class MainLayer(cocos.layer.Layer):
    def __init__(self):
        super(MainLayer, self).__init__()

        planet = Planet(10)
        self.add(planet)


class Planet(cocos.sprite.Sprite):
    def __init__(self, radius):
        batch = pyglet.graphics.Batch()
        shape = shapes.Circle(300, 150, 100, color=(50, 225, 30), batch=batch)
        super(Planet, self).__init__(shape)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cocos.director.director.init(caption='Planetor')
    scene = cocos.scene.Scene()
    cocos.director.director.run(scene)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
