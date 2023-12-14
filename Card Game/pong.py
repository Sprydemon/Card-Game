from kivy.app import App
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
import dimensions
from kivy.core.window import Window
from deck import player
import pyautogui
from charecter import Charecter

# height_dimension = {
#     1: (Window.height/5+Window.height/45)-Window.height/54,
#     2: (Window.height/5+Window.height/45)+Window.height/16, 
#     3: (Window.height/5+Window.height/45)+Window.height/7.08196721311,
#     4: (Window.height/5+Window.height/45)+Window.height/4.54736842105,
#     5: (Window.height/5+Window.height/45)+Window.height/3.3488372093,
#     6: (Window.height/5+Window.height/45)+Window.height/2.65030674847,
#     7: (Window.height/5+Window.height/45)+Window.height/2.19289340102,
#     8: (Window.height/5+Window.height/45)+Window.height/1.86206896552
# } adds Window.height/12.7058823529 each time except for attack

global right_lane
right_lane = ["x", "x", "x", "x", "x", "x", "x", "x"]
global left_lane
left_lane = ["x", "x", "x", "x", "x", "x", "x", "x"]
global mid_lane
mid_lane = ["x", "x", "x", "x", "x", "x", "x", "x"]

#########################################################################################################################################
swordman = Charecter(10, 10, 9999, 0, "player")
global swordman_bool
swordman_bool = False


class game_board(FloatLayout):


    def on_touch_down(self, touch):
#########################################################################################################################################
# hand
        p = pyautogui.position()
        if p[0] > Window.width/5+3*Window.width/5-3*Window.width/5/6+3*Window.width/5/72 and p[0] < Window.width/5+3*Window.width/5-3*Window.width/5/6+3*Window.width/5/72 + 3*Window.width/5/6-3*Window.width/5/36 and Window.height - p[1] > 0 and Window.height - p[1] < Window.height/5-Window.height/Window.height/16:
            player.draw()
            self.ids.hand_one.source = player.stored[0]
            self.ids.hand_two.source = player.stored[1]
            self.ids.hand_three.source = player.stored[2]
            self.ids.hand_four.source = player.stored[3]
            print(player.stored[0])
            print(player.stored[1])
            print(player.stored[2])
            print(player.stored[3])

#########################################################################################################################################
# swordman
        # summon
        if self.ids.swordman.pos[0] < touch.pos[0] and self.ids.swordman.pos[0] + self.ids.swordman.size[0] > touch.pos[0] and self.ids.swordman.pos[1] < touch.pos[1] and self.ids.swordman.pos[1] + self.ids.swordman.size[1] > touch.pos[1] and self.ids.swordman.pos[1] <= Window.height/5 and swordman.cd <= 0:
            global swordman_bool
            swordman_bool = True
            global swordman_pos
            swordman_pos = self.ids.swordman.pos[0], self.ids.swordman.pos[1]

        # change lane
        global change_lane
        change_lane = False
        if swordman.index == 0 or swordman.index == 3 or swordman.index == 4 or swordman.index == 7:
            if self.ids.swordman.pos[0] < touch.pos[0] - self.ids.swordman.size[0] and self.ids.swordman.pos[0] + self.ids.swordman.size[0]/2 > touch.pos[0] - self.ids.swordman.size[0]:
                if swordman.lane == "left" or swordman.lane == "mid":
                    if swordman.lane == "mid":
                        if right_lane[swordman.index] == "x":
                            change_lane = True
                            swordman.lane = "right"
                            (right_lane[swordman.index], mid_lane[swordman.index]) = (mid_lane[swordman.index], right_lane[swordman.index])
                    elif swordman.lane == "left":
                        if mid_lane[swordman.index] == "x":
                            change_lane = True
                            swordman.lane = "mid"
                            (left_lane[swordman.index], mid_lane[swordman.index]) = (mid_lane[swordman.index], left_lane[swordman.index])
                    if change_lane == True:
                        self.ids.swordman.pos[0] += ((Window.width/5+3*Window.width/5/2)-Window.width/1536) - ((Window.width/5+3*Window.width/5/5)-Window.width/1536)
            
            elif self.ids.swordman.pos[0] + self.ids.swordman.size[0]/2 < touch.pos[0] + self.ids.swordman.size[0] and self.ids.swordman.pos[0] + self.ids.swordman.size[0] > touch.pos[0] + self.ids.swordman.size[0]:
                if swordman.lane == "right" or swordman.lane == "mid":
                    if swordman.lane == "mid":
                        if left_lane[swordman.index] == "x":
                            change_lane = True
                            swordman.lane = "left"
                            (left_lane[swordman.index], mid_lane[swordman.index]) = (mid_lane[swordman.index], left_lane[swordman.index])
                    elif swordman.lane == "right":
                        if mid_lane[swordman.index] == "x":
                            change_lane = True
                            swordman.lane = "mid"
                            (right_lane[swordman.index], mid_lane[swordman.index]) = (mid_lane[swordman.index], right_lane[swordman.index])
                    if change_lane == True:
                        self.ids.swordman.pos[0] -= ((Window.width/5+3*Window.width/5/2)-Window.width/1536) - ((Window.width/5+3*Window.width/5/5)-Window.width/1536)

        if self.ids.swordman.pos[0] > Window.width/2 + self.ids.swordman.size[0]:
            # move up right
            if self.ids.swordman.pos[0] < touch.pos[0] and self.ids.swordman.pos[0] + self.ids.swordman.size[0] > touch.pos[0] and self.ids.swordman.pos[1] + self.ids.swordman.size[1]/2 < touch.pos[1] and self.ids.swordman.pos[1] + self.ids.swordman.size[1] > touch.pos[1] and self.ids.swordman.pos[1] >= Window.height/5 and self.ids.swordman.pos[1] < 4*Window.height/5 - Window.height/12.7058823529 and swordman.spd > 0 and right_lane[swordman.index+1] == "x":
                self.ids.swordman.pos[1] += Window.height/12.7058823529
                swordman.spd -= 1
                (right_lane[swordman.index], right_lane[swordman.index+1]) = (right_lane[swordman.index+1], right_lane[swordman.index])
                swordman.index += 1
            # move down right
            if self.ids.swordman.pos[0] < touch.pos[0] and self.ids.swordman.pos[0] + self.ids.swordman.size[0] > touch.pos[0] and self.ids.swordman.pos[1] < touch.pos[1] and self.ids.swordman.pos[1] + self.ids.swordman.size[1]/2 > touch.pos[1] and self.ids.swordman.pos[1] >= Window.height/5 and self.ids.swordman.pos[1] > Window.height/5 + Window.height/12.7058823529 and swordman.spd > 0 and right_lane[swordman.index-1] == "x":
                self.ids.swordman.pos[1] -= Window.height/12.7058823529
                swordman.spd -= 1
                (right_lane[swordman.index], right_lane[swordman.index-1]) = (right_lane[swordman.index-1], right_lane[swordman.index])
                swordman.index -= 1

        elif self.ids.swordman.pos[0] < Window.width/2 - self.ids.swordman.size[0]:
            # move up left
            if self.ids.swordman.pos[0] < touch.pos[0] and self.ids.swordman.pos[0] + self.ids.swordman.size[0] > touch.pos[0] and self.ids.swordman.pos[1] + self.ids.swordman.size[1]/2 < touch.pos[1] and self.ids.swordman.pos[1] + self.ids.swordman.size[1] > touch.pos[1] and self.ids.swordman.pos[1] >= Window.height/5 and self.ids.swordman.pos[1] < 4*Window.height/5 - Window.height/12.7058823529 and swordman.spd > 0 and left_lane[swordman.index+1] == "x":
                self.ids.swordman.pos[1] += Window.height/12.7058823529
                swordman.spd -= 1
                (left_lane[swordman.index], left_lane[swordman.index+1]) = (left_lane[swordman.index+1], left_lane[swordman.index])
                swordman.index += 1
            # move down left
            if self.ids.swordman.pos[0] < touch.pos[0] and self.ids.swordman.pos[0] + self.ids.swordman.size[0] > touch.pos[0] and self.ids.swordman.pos[1] < touch.pos[1] and self.ids.swordman.pos[1] + self.ids.swordman.size[1]/2 > touch.pos[1] and self.ids.swordman.pos[1] >= Window.height/5 and self.ids.swordman.pos[1] > Window.height/5 + Window.height/12.7058823529 and swordman.spd > 0 and left_lane[swordman.index-1] == "x":
                self.ids.swordman.pos[1] -= Window.height/12.7058823529
                swordman.spd -= 1
                (left_lane[swordman.index], left_lane[swordman.index-1]) = (left_lane[swordman.index-1], left_lane[swordman.index])
                swordman.index -= 1
        else:
            # move up mid
            if self.ids.swordman.pos[0] < touch.pos[0] and self.ids.swordman.pos[0] + self.ids.swordman.size[0] > touch.pos[0] and self.ids.swordman.pos[1] + self.ids.swordman.size[1]/2 < touch.pos[1] and self.ids.swordman.pos[1] + self.ids.swordman.size[1] > touch.pos[1] and self.ids.swordman.pos[1] >= Window.height/5 and self.ids.swordman.pos[1] < 4*Window.height/5 - Window.height/12.7058823529 and swordman.spd > 0 and mid_lane[swordman.index+1] == "x":
                self.ids.swordman.pos[1] += Window.height/12.7058823529
                swordman.spd -= 1
                (mid_lane[swordman.index], mid_lane[swordman.index+1]) = (mid_lane[swordman.index+1], mid_lane[swordman.index])
                swordman.index += 1
            # move down mid
            if self.ids.swordman.pos[0] < touch.pos[0] and self.ids.swordman.pos[0] + self.ids.swordman.size[0] > touch.pos[0] and self.ids.swordman.pos[1] < touch.pos[1] and self.ids.swordman.pos[1] + self.ids.swordman.size[1]/2 > touch.pos[1] and self.ids.swordman.pos[1] >= Window.height/5 and self.ids.swordman.pos[1] > Window.height/5 + Window.height/12.7058823529 and swordman.spd > 0 and mid_lane[swordman.index-1] == "x":
                self.ids.swordman.pos[1] -= Window.height/12.7058823529
                swordman.spd -= 1
                (mid_lane[swordman.index], mid_lane[swordman.index-1]) = (mid_lane[swordman.index-1], mid_lane[swordman.index])
                swordman.index -= 1
        

            



    def on_touch_move(self, touch):
#########################################################################################################################################
# swordman
        if swordman_bool == True:
            self.ids.swordman.pos = touch.spos[0]*Window.width-self.ids.swordman.size[0]/2,touch.spos[1]*Window.height-self.ids.swordman.size[1]/2



    def on_touch_up(self, touch):
        p = pyautogui.position()
#########################################################################################################################################
# swordman
        global swordman_bool
        if swordman_bool == True:
            if p[0] < Window.width/2 and left_lane[1] == "x":
                self.ids.swordman.pos = (Window.width/5+3*Window.width/5/5)-Window.width/102.4, (Window.height/5+Window.height/45)+Window.height/16
                left_lane[1] = swordman
                swordman.lane = "left"
            elif p[0] > Window.width/2 and right_lane[1] == "x":
                self.ids.swordman.pos = (Window.width/5+3*Window.width/5/5*4)-Window.width/102.4, (Window.height/5+Window.height/45)+Window.height/16
                right_lane[1] = swordman 
                swordman.lane = "right"
            else:
                self.ids.swordman.pos = swordman_pos
        swordman_bool = False





class PongApp(App):
    def build(self):
        self.width = Window.width
        self.height = Window.height
        return game_board()


if __name__ == '__main__':
    print(dimensions.screen_width)
    PongApp().run()


