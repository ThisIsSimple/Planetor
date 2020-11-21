import cocos

from objects.Planet import Planet
from objects.Creature import Creature
from objects.Player import Player


class GameLayer(cocos.layer.Layer):
    is_event_handler = True

    def on_key_press(self, k, _):
        Player.KEY_PRESSED[k] = 1

    def on_key_release(self, k, _):
        Player.KEY_PRESSED[k] = 0

    def __init__(self):
        super(GameLayer, self).__init__()

        planet = Planet(320, 200)
        self.add(planet)

        self.player = Player(planet)
        self.add(self.player)

        self.text_label = cocos.text.Label("test")
        self.add(self.text_label)

        self.schedule(self.update)

    def update(self, dt):
        self.player.update(dt)
