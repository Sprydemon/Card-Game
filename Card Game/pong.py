from kivy.app import App
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.config import Config
from kivy.uix.button import Button
import dimensions
from kivy.animation import Animation
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector
from kivy.core.window import Window


class game_board(Widget):
    pass


class PongApp(App):
    def build(self):
        self.width = Window.width
        self.height = Window.height
        return game_board()


if __name__ == '__main__':
    print(dimensions.screen_width)
    PongApp().run()


