import cocos
from cocos import draw
import cocos.collision_model as cm
from scenes.TitleScene import TitleLayer


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    director = cocos.director.director
    director.init(caption='Planetor', width=640, height=480)

    titleScene = cocos.scene.Scene(TitleLayer())
    director.run(titleScene)
