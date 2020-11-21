import cocos
from cocos import draw
import cocos.collision_model as cm
from scenes.TitleScene import TitleLayer


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

        title_label = cocos.text.RichLabel(text="Planetor", x=320, y=240, font_name="monogram", font_size=48, anchor_x="center", anchor_y="center")
        self.add(title_label)

        label = cocos.text.Label(text="test123", position=(300, 320))
        label.color = (255, 255, 255, 1)
        self.add(label)

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
    director = cocos.director.director
    director.init(caption='Planetor', width=640, height=480)

    titleScene = cocos.scene.Scene(TitleLayer())
    director.run(titleScene)

    # scene = cocos.scene.Scene(mainLayer)
    # cocos.director.director.run(scene)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
