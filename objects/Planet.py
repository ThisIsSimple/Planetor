import cocos


class Planet(cocos.sprite.Sprite):
    def __init__(self, x, y):
        # super(Planet, self).__init__(image="assets/planet.png", position=(x, y))
        super(Planet, self).__init__(image="assets/images/planet_icon/Ice.png", position=(x, y))

        self.creatures = []

        self.schedule(self.update)

    def update(self, dt):
        pass

    def set_creatures_position(self):
        for creature in self.creatures:
            pass

