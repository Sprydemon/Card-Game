from kivy.app import App
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
import dimensions
from kivy.core.window import Window
from deck import player
import pyautogui
from charecter import Charecter

global right_lane
right_lane = ["x", "x", "x", "x", "x", "x", "x", "x", "x"]
global left_lane
left_lane = ["x", "x", "x", "x", "x", "x", "x", "x", "x"]
global mid_lane
mid_lane = ["x", "x", "x", "x", "x", "x", "x", "x", "x"]

#########################################################################################################################################
swordman = Charecter(10, 10, 9999, 0, "player")
global swordman_bool
swordman_bool = False
global swordman_battle
swordman_battle = False
#########################################################################################################################################
ion = Charecter(10, 10, 9999, 0, "opponent")
global ion_bool
ion_bool = False
global ion_battle
ion_battle = False

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
            global swordman_battle
            global swordman_bool
            swordman_bool = True
            global swordman_pos
            swordman_pos = self.ids.swordman.pos[0], self.ids.swordman.pos[1]

        # change lane
        global change_lane
        change_lane = False
        if swordman.index == 0 or swordman.index == 3 or swordman.index == 4 or swordman.index == 7:
            if self.ids.swordman.pos[0] < touch.pos[0] - self.ids.swordman.size[0] and self.ids.swordman.pos[0] + self.ids.swordman.size[0]/2 > touch.pos[0] - self.ids.swordman.size[0] and self.ids.swordman.pos[1] < touch.pos[1] and self.ids.swordman.pos[1] + self.ids.swordman.size[1] > touch.pos[1]:
                if swordman.lane == "left" or swordman.lane == "mid":
                    if swordman.lane == "mid":
                        if right_lane[swordman.index] == "x":
                            change_lane = True
                            swordman.lane = "right"
                            (right_lane[swordman.index], mid_lane[swordman.index]) = (mid_lane[swordman.index], right_lane[swordman.index])
                        else:
                            if right_lane[swordman.index].team == "opponent":
                                swordman_battle = True
                    elif swordman.lane == "left":
                        if mid_lane[swordman.index] == "x":
                            change_lane = True
                            swordman.lane = "mid"
                            (left_lane[swordman.index], mid_lane[swordman.index]) = (mid_lane[swordman.index], left_lane[swordman.index])
                        else:
                            if mid_lane[swordman.index].team == "opponent":
                                swordman_battle = True
                    if change_lane == True:
                        self.ids.swordman.pos[0] += ((Window.width/5+3*Window.width/5/2)-Window.width/1536) - ((Window.width/5+3*Window.width/5/5)-Window.width/1536)
            
            elif self.ids.swordman.pos[0] + self.ids.swordman.size[0]/2 < touch.pos[0] + self.ids.swordman.size[0] and self.ids.swordman.pos[0] + self.ids.swordman.size[0] > touch.pos[0] + self.ids.swordman.size[0] and self.ids.swordman.pos[1] < touch.pos[1] and self.ids.swordman.pos[1] + self.ids.swordman.size[1] > touch.pos[1]:
                if swordman.lane == "right" or swordman.lane == "mid":
                    if swordman.lane == "mid":
                        if left_lane[swordman.index] == "x":
                            change_lane = True
                            swordman.lane = "left"
                            (left_lane[swordman.index], mid_lane[swordman.index]) = (mid_lane[swordman.index], left_lane[swordman.index])
                        else:
                            if left_lane[swordman.index].team == "opponent":
                                swordman_battle = True
                    elif swordman.lane == "right":
                        if mid_lane[swordman.index] == "x":
                            change_lane = True
                            swordman.lane = "mid"
                            (right_lane[swordman.index], mid_lane[swordman.index]) = (mid_lane[swordman.index], right_lane[swordman.index])
                        else:
                            if mid_lane[swordman.index].team == "opponent":
                                swordman_battle = True
                    if change_lane == True:
                        self.ids.swordman.pos[0] -= ((Window.width/5+3*Window.width/5/2)-Window.width/1536) - ((Window.width/5+3*Window.width/5/5)-Window.width/1536)

        if self.ids.swordman.pos[0] > Window.width/2 + self.ids.swordman.size[0]:
            # move up right
            if self.ids.swordman.pos[0] < touch.pos[0] and self.ids.swordman.pos[0] + self.ids.swordman.size[0] > touch.pos[0] and self.ids.swordman.pos[1] + self.ids.swordman.size[1]/2 < touch.pos[1] and self.ids.swordman.pos[1] + self.ids.swordman.size[1] > touch.pos[1] and self.ids.swordman.pos[1] >= Window.height/5 and self.ids.swordman.pos[1] < 4*Window.height/5 - Window.height/12.7058823529 and swordman.spd > 0 and right_lane[swordman.index+1] == "x":
                self.ids.swordman.pos[1] += Window.height/12.7058823529
                swordman.spd -= 1
                (right_lane[swordman.index], right_lane[swordman.index+1]) = (right_lane[swordman.index+1], right_lane[swordman.index])
                swordman.index += 1
            if right_lane[swordman.index+1] != "x" and right_lane[swordman.index+1].team == "opponent":
                swordman_battle = True 
            # move down right
            if self.ids.swordman.pos[0] < touch.pos[0] and self.ids.swordman.pos[0] + self.ids.swordman.size[0] > touch.pos[0] and self.ids.swordman.pos[1] < touch.pos[1] and self.ids.swordman.pos[1] + self.ids.swordman.size[1]/2 > touch.pos[1] and self.ids.swordman.pos[1] >= Window.height/5 and self.ids.swordman.pos[1] > Window.height/5 + Window.height/12.7058823529 and swordman.spd > 0 and right_lane[swordman.index-1] == "x":
                self.ids.swordman.pos[1] -= Window.height/12.7058823529
                swordman.spd -= 1
                (right_lane[swordman.index], right_lane[swordman.index-1]) = (right_lane[swordman.index-1], right_lane[swordman.index])
                swordman.index -= 1
            if right_lane[swordman.index-1] != "x" and right_lane[swordman.index-1].team == "opponent":
                swordman_battle = True 

        elif self.ids.swordman.pos[0] < Window.width/2 - self.ids.swordman.size[0]:
            # move up left
            if self.ids.swordman.pos[0] < touch.pos[0] and self.ids.swordman.pos[0] + self.ids.swordman.size[0] > touch.pos[0] and self.ids.swordman.pos[1] + self.ids.swordman.size[1]/2 < touch.pos[1] and self.ids.swordman.pos[1] + self.ids.swordman.size[1] > touch.pos[1] and self.ids.swordman.pos[1] >= Window.height/5 and self.ids.swordman.pos[1] < 4*Window.height/5 - Window.height/12.7058823529 and swordman.spd > 0 and left_lane[swordman.index+1] == "x":
                self.ids.swordman.pos[1] += Window.height/12.7058823529
                swordman.spd -= 1
                (left_lane[swordman.index], left_lane[swordman.index+1]) = (left_lane[swordman.index+1], left_lane[swordman.index])
                swordman.index += 1
            if left_lane[swordman.index+1] != "x" and left_lane[swordman.index+1].team == "opponent":
                swordman_battle = True 
            # move down left
            if self.ids.swordman.pos[0] < touch.pos[0] and self.ids.swordman.pos[0] + self.ids.swordman.size[0] > touch.pos[0] and self.ids.swordman.pos[1] < touch.pos[1] and self.ids.swordman.pos[1] + self.ids.swordman.size[1]/2 > touch.pos[1] and self.ids.swordman.pos[1] >= Window.height/5 and self.ids.swordman.pos[1] > Window.height/5 + Window.height/12.7058823529 and swordman.spd > 0 and left_lane[swordman.index-1] == "x":
                self.ids.swordman.pos[1] -= Window.height/12.7058823529
                swordman.spd -= 1
                (left_lane[swordman.index], left_lane[swordman.index-1]) = (left_lane[swordman.index-1], left_lane[swordman.index])
                swordman.index -= 1
            if left_lane[swordman.index-1] != "x" and left_lane[swordman.index-1].team == "opponent":
                swordman_battle = True 
        else:
            # move up mid
            if self.ids.swordman.pos[0] < touch.pos[0] and self.ids.swordman.pos[0] + self.ids.swordman.size[0] > touch.pos[0] and self.ids.swordman.pos[1] + self.ids.swordman.size[1]/2 < touch.pos[1] and self.ids.swordman.pos[1] + self.ids.swordman.size[1] > touch.pos[1] and self.ids.swordman.pos[1] >= Window.height/5 and self.ids.swordman.pos[1] < 4*Window.height/5 - Window.height/12.7058823529 and swordman.spd > 0 and mid_lane[swordman.index+1] == "x":
                self.ids.swordman.pos[1] += Window.height/12.7058823529
                swordman.spd -= 1
                (mid_lane[swordman.index], mid_lane[swordman.index+1]) = (mid_lane[swordman.index+1], mid_lane[swordman.index])
                swordman.index += 1
            if mid_lane[swordman.index+1] != "x" and mid_lane[swordman.index+1].team == "opponent":
                swordman_battle = True 
            # move down mid
            if self.ids.swordman.pos[0] < touch.pos[0] and self.ids.swordman.pos[0] + self.ids.swordman.size[0] > touch.pos[0] and self.ids.swordman.pos[1] < touch.pos[1] and self.ids.swordman.pos[1] + self.ids.swordman.size[1]/2 > touch.pos[1] and self.ids.swordman.pos[1] >= Window.height/5 and self.ids.swordman.pos[1] > Window.height/5 + Window.height/12.7058823529 and swordman.spd > 0 and mid_lane[swordman.index-1] == "x":
                self.ids.swordman.pos[1] -= Window.height/12.7058823529
                swordman.spd -= 1
                (mid_lane[swordman.index], mid_lane[swordman.index-1]) = (mid_lane[swordman.index-1], mid_lane[swordman.index])
                swordman.index -= 1
            if mid_lane[swordman.index-1] != "x" and mid_lane[swordman.index-1].team == "opponent":
                swordman_battle = True 
#########################################################################################################################################
# ion
        # summon
        if self.ids.ion.pos[0] < touch.pos[0] and self.ids.ion.pos[0] + self.ids.ion.size[0] > touch.pos[0] and self.ids.ion.pos[1] < touch.pos[1] and self.ids.ion.pos[1] + self.ids.ion.size[1] > touch.pos[1] and self.ids.ion.pos[1] <= Window.height/5 and ion.cd <= 0:
            global ion_battle
            global ion_bool
            ion_bool = True
            global ion_pos
            ion_pos = self.ids.ion.pos[0], self.ids.ion.pos[1]

        # change lane
        global ion_change_lane
        ion_change_lane = False
        if ion.index == 0 or ion.index == 3 or ion.index == 4 or ion.index == 7:
            if self.ids.ion.pos[0] < touch.pos[0] - self.ids.ion.size[0] and self.ids.ion.pos[0] + self.ids.ion.size[0]/2 > touch.pos[0] - self.ids.ion.size[0] and self.ids.ion.pos[1] < touch.pos[1] and self.ids.ion.pos[1] + self.ids.ion.size[1] > touch.pos[1]:
                if ion.lane == "left" or ion.lane == "mid":
                    if ion.lane == "mid":
                        if right_lane[ion.index] == "x":
                            ion_change_lane = True
                            ion.lane = "right"
                            (right_lane[ion.index], mid_lane[ion.index]) = (mid_lane[ion.index], right_lane[ion.index])
                        else:
                            if right_lane[ion.index].team == "opponent":
                                ion_battle = True
                    elif ion.lane == "left":
                        if mid_lane[ion.index] == "x":
                            ion_change_lane = True
                            ion.lane = "mid"
                            (left_lane[ion.index], mid_lane[ion.index]) = (mid_lane[ion.index], left_lane[ion.index])
                        else:
                            if mid_lane[ion.index].team == "opponent":
                                ion_battle = True                    
                    if ion_change_lane == True:
                        self.ids.ion.pos[0] += ((Window.width/5+3*Window.width/5/2)-Window.width/1536) - ((Window.width/5+3*Window.width/5/5)-Window.width/1536)
            
            elif self.ids.ion.pos[0] + self.ids.ion.size[0]/2 < touch.pos[0] + self.ids.ion.size[0] and self.ids.ion.pos[0] + self.ids.ion.size[0] > touch.pos[0] + self.ids.ion.size[0] and self.ids.ion.pos[1] < touch.pos[1] and self.ids.ion.pos[1] + self.ids.ion.size[1] > touch.pos[1]:
                if ion.lane == "right" or ion.lane == "mid":
                    if ion.lane == "mid":
                        if left_lane[ion.index] == "x":
                            ion_change_lane = True
                            ion.lane = "left"
                            (left_lane[ion.index], mid_lane[ion.index]) = (mid_lane[ion.index], left_lane[ion.index])
                        else:
                            if left_lane[ion.index].team == "opponent":
                                ion_battle = True
                    elif ion.lane == "right":
                        if mid_lane[ion.index] == "x":
                            ion_change_lane = True
                            ion.lane = "mid"
                            (right_lane[ion.index], mid_lane[ion.index]) = (mid_lane[ion.index], right_lane[ion.index])
                        else:
                            if mid_lane[ion.index].team == "opponent":
                                ion_battle = True
                    if ion_change_lane == True:
                        self.ids.ion.pos[0] -= ((Window.width/5+3*Window.width/5/2)-Window.width/1536) - ((Window.width/5+3*Window.width/5/5)-Window.width/1536)

        if self.ids.ion.pos[0] > Window.width/2 + self.ids.ion.size[0]:
            # move up right
            if self.ids.ion.pos[0] < touch.pos[0] and self.ids.ion.pos[0] + self.ids.ion.size[0] > touch.pos[0] and self.ids.ion.pos[1] + self.ids.ion.size[1]/2 < touch.pos[1] and self.ids.ion.pos[1] + self.ids.ion.size[1] > touch.pos[1] and self.ids.ion.pos[1] >= Window.height/5 and self.ids.ion.pos[1] < 4*Window.height/5 - Window.height/12.7058823529 and ion.spd > 0 and right_lane[ion.index+1] == "x":
                self.ids.ion.pos[1] += Window.height/12.7058823529
                ion.spd -= 1
                (right_lane[ion.index], right_lane[ion.index+1]) = (right_lane[ion.index+1], right_lane[ion.index])
                ion.index += 1
            if right_lane[ion.index+1] != "x" and right_lane[ion.index+1].team == "opponent":
                ion_battle = True 
            # move down right
            if self.ids.ion.pos[0] < touch.pos[0] and self.ids.ion.pos[0] + self.ids.ion.size[0] > touch.pos[0] and self.ids.ion.pos[1] < touch.pos[1] and self.ids.ion.pos[1] + self.ids.ion.size[1]/2 > touch.pos[1] and self.ids.ion.pos[1] >= Window.height/5 and self.ids.ion.pos[1] > Window.height/5 + Window.height/12.7058823529 and ion.spd > 0 and right_lane[ion.index-1] == "x":
                self.ids.ion.pos[1] -= Window.height/12.7058823529
                ion.spd -= 1
                (right_lane[ion.index], right_lane[ion.index-1]) = (right_lane[ion.index-1], right_lane[ion.index])
                ion.index -= 1
            if right_lane[ion.index-1] != "x" and right_lane[ion.index-1].team == "opponent":
                ion_battle = True 

        elif self.ids.ion.pos[0] < Window.width/2 - self.ids.ion.size[0]:
            # move up left
            if self.ids.ion.pos[0] < touch.pos[0] and self.ids.ion.pos[0] + self.ids.ion.size[0] > touch.pos[0] and self.ids.ion.pos[1] + self.ids.ion.size[1]/2 < touch.pos[1] and self.ids.ion.pos[1] + self.ids.ion.size[1] > touch.pos[1] and self.ids.ion.pos[1] >= Window.height/5 and self.ids.ion.pos[1] < 4*Window.height/5 - Window.height/12.7058823529 and ion.spd > 0 and left_lane[ion.index+1] == "x":
                self.ids.ion.pos[1] += Window.height/12.7058823529
                ion.spd -= 1
                (left_lane[ion.index], left_lane[ion.index+1]) = (left_lane[ion.index+1], left_lane[ion.index])
                ion.index += 1
            if left_lane[ion.index+1] != "x" and left_lane[ion.index+1].team == "opponent":
                ion_battle = True 
            # move down left
            if self.ids.ion.pos[0] < touch.pos[0] and self.ids.ion.pos[0] + self.ids.ion.size[0] > touch.pos[0] and self.ids.ion.pos[1] < touch.pos[1] and self.ids.ion.pos[1] + self.ids.ion.size[1]/2 > touch.pos[1] and self.ids.ion.pos[1] >= Window.height/5 and self.ids.ion.pos[1] > Window.height/5 + Window.height/12.7058823529 and ion.spd > 0 and left_lane[ion.index-1] == "x":
                self.ids.ion.pos[1] -= Window.height/12.7058823529
                ion.spd -= 1
                (left_lane[ion.index], left_lane[ion.index-1]) = (left_lane[ion.index-1], left_lane[ion.index])
                ion.index -= 1
            if left_lane[ion.index-1] != "x" and left_lane[ion.index-1].team == "opponent":
                ion_battle = True 
        else:
            # move up mid
            if self.ids.ion.pos[0] < touch.pos[0] and self.ids.ion.pos[0] + self.ids.ion.size[0] > touch.pos[0] and self.ids.ion.pos[1] + self.ids.ion.size[1]/2 < touch.pos[1] and self.ids.ion.pos[1] + self.ids.ion.size[1] > touch.pos[1] and self.ids.ion.pos[1] >= Window.height/5 and self.ids.ion.pos[1] < 4*Window.height/5 - Window.height/12.7058823529 and ion.spd > 0 and mid_lane[ion.index+1] == "x":
                self.ids.ion.pos[1] += Window.height/12.7058823529
                ion.spd -= 1
                (mid_lane[ion.index], mid_lane[ion.index+1]) = (mid_lane[ion.index+1], mid_lane[ion.index])
                ion.index += 1
            if mid_lane[ion.index+1] != "x" and mid_lane[ion.index+1].team == "opponent":
                ion_battle = True 
            # move down mid
            if self.ids.ion.pos[0] < touch.pos[0] and self.ids.ion.pos[0] + self.ids.ion.size[0] > touch.pos[0] and self.ids.ion.pos[1] < touch.pos[1] and self.ids.ion.pos[1] + self.ids.ion.size[1]/2 > touch.pos[1] and self.ids.ion.pos[1] >= Window.height/5 and self.ids.ion.pos[1] > Window.height/5 + Window.height/12.7058823529 and ion.spd > 0 and mid_lane[ion.index-1] == "x":
                self.ids.ion.pos[1] -= Window.height/12.7058823529
                ion.spd -= 1
                (mid_lane[ion.index], mid_lane[ion.index-1]) = (mid_lane[ion.index-1], mid_lane[ion.index])
                ion.index -= 1
            if mid_lane[ion.index-1] != "x" and mid_lane[ion.index-1].team == "opponent":
                ion_battle = True 
        print("")
        print(right_lane[swordman.index+1])
        print("")

    def on_touch_move(self, touch):
#########################################################################################################################################
# swordman
        if swordman_bool == True:
            self.ids.swordman.pos = touch.spos[0]*Window.width-self.ids.swordman.size[0]/2,touch.spos[1]*Window.height-self.ids.swordman.size[1]/2
#########################################################################################################################################
# ion
        if ion_bool == True:
            self.ids.ion.pos = touch.spos[0]*Window.width-self.ids.ion.size[0]/2,touch.spos[1]*Window.height-self.ids.ion.size[1]/2


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
        global swordman_battle
        if swordman_battle == True:
            print("battle begins")
            swordman_battle = False
#########################################################################################################################################
# ion
        global ion_bool
        if ion_bool == True:
            if p[0] < Window.width/2 and left_lane[1] == "x":
                self.ids.ion.pos = (Window.width/5+3*Window.width/5/5)-Window.width/102.4, (Window.height/5+Window.height/45)+Window.height/16
                left_lane[1] = ion
                ion.lane = "left"
            elif p[0] > Window.width/2 and right_lane[1] == "x":
                self.ids.ion.pos = (Window.width/5+3*Window.width/5/5*4)-Window.width/102.4, (Window.height/5+Window.height/45)+Window.height/16
                right_lane[1] = ion 
                ion.lane = "right"
            else:
                self.ids.ion.pos = ion_pos
        ion_bool = False
        global ion_battle
        if ion_battle == True:
            print("battle begins")
            ion_battle = False




class PongApp(App):
    def build(self):
        self.width = Window.width
        self.height = Window.height
        return game_board()


if __name__ == '__main__':
    print(dimensions.screen_width)
    PongApp().run()


