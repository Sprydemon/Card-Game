from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.config import Config
import dimensions
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
    window = ImageShapeWindow()
    window.run()

print(dimensions.screen_width)
print(dimensions.screen_height)
print(dimensions.board_width)
print(dimensions.board_height)
print(dimensions.board_width_pos)