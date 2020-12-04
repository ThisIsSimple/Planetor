import cocos

import scenes.GameScene as GameScene


if __name__ == "__main__":
    cocos.director.director.init(caption="Planetor")

    scene = cocos.scene.Scene(GameScene.GameLayer())
    cocos.director.director.run(scene)
