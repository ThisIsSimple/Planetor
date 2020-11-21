import cocos
from cocos.actions import ScaleTo, Rotate, Repeat
from scenes.GameScene import GameLayer

import pyglet


class TitleLayer(cocos.layer.Layer):
    is_event_handler=True

    def __init__(self):
        super(TitleLayer, self).__init__()

        texture = pyglet.image.load('assets/textures/background.png').get_texture()
        background = cocos.sprite.Sprite(texture, position=(320, 240))
        # background.do(Repeat(Rotate(10, 2)))
        self.add(background)

        title_label = cocos.text.RichLabel(text="Planetor", position=(320, 320), font_name="monogram", font_size=60, anchor_x="center")
        self.add(title_label)

        # menu items
        self.menu_items = []

        self.start_label = cocos.text.RichLabel(text="Game Start", position=(320, 260), font_name="monogram", font_size=24, anchor_x="center")
        self.menu_items.append(self.start_label)
        self.add(self.start_label)

        self.quit_label = cocos.text.RichLabel(text="Quit Game", position=(320, 220), font_name="monogram", font_size=24, anchor_x="center")
        self.menu_items.append(self.quit_label)
        self.add(self.quit_label)

        self.planet = cocos.sprite.Sprite(image="assets/planet.png", position=(320, -947), color=(100, 255, 100))
        self.planet.do(Repeat(Rotate(10, 5)))
        self.add(self.planet)

    def on_mouse_motion(self, x, y, dx, dy):
        # check if mouse on menu items
        for menu_item in self.menu_items:
            if self.check_mouse_on_label(menu_item, x, y):
                menu_item.do(ScaleTo(1.2, 0.075))
            else:
                menu_item.do(ScaleTo(1, 0.075))

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        print(x, y)

    def on_mouse_press(self, x, y, buttons, modifiers):
        # This next line seems a bit odd, and that's because it is!
        self.position_x, self.position_y = cocos.director.director.get_virtual_coordinates(x, y)
        # It introduces a new topic, virtual coordinates
        # If I had used default coordinates, the position might be updated in the OS's coordinates rather than the scene
        # The director provides us with the appropriate coordinates within our "virtual" window

        if self.check_mouse_on_label(self.start_label, x, y):
            cocos.director.director.push(cocos.scene.Scene(GameLayer()))
        elif self.check_mouse_on_label(self.quit_label, x, y):
            cocos.director.director.pop()

    def check_mouse_on_label(self, label, x, y):
        labelPos = label.position
        labelWidth = label.element.content_width
        labelHeight = label.element.content_height
        if labelPos[0] - labelWidth / 2 < x < labelPos[0] + labelWidth / 2 and labelPos[1] - labelHeight / 2 < y < \
                labelPos[1] + labelHeight / 2:
            return True
        else:
            return False
