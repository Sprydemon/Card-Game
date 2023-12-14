from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.config import Config
from kivy.uix.button import Button
import dimensions
from kivy.animation import Animation
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector
#from kivy.core.window import Window
#Window.size = (dimensions.screen_width, dimensions.screen_height)
Config.set('graphics', 'width', dimensions.screen_width)
Config.set('graphics', 'height', dimensions.screen_height)


class game_board(RelativeLayout):
    pass

class ImageShapeWindow(App):
    def build(self):
        return game_board()





if __name__ == "__main__":
    ImageShapeWindow().run()

