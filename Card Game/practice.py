
# id
# id_bool
# id_pos
# id_change_lane

#########################################################################################################################################
id = Charecter(10, 10, 9999, 0, "player")
global id_bool
id_bool = False

class game_board(FloatLayout):


    def on_touch_down(self, touch):
#########################################################################################################################################
# id
        # summon
        if self.ids.id.pos[0] < touch.pos[0] and self.ids.id.pos[0] + self.ids.id.size[0] > touch.pos[0] and self.ids.id.pos[1] < touch.pos[1] and self.ids.id.pos[1] + self.ids.id.size[1] > touch.pos[1] and self.ids.id.pos[1] <= Window.height/5 and id.cd <= 0:
            global id_bool
            id_bool = True
            global id_pos
            id_pos = self.ids.id.pos[0], self.ids.id.pos[1]

        # change lane
        global id_change_lane
        id_change_lane = False
        if id.index == 0 or id.index == 3 or id.index == 4 or id.index == 7:
            if self.ids.id.pos[0] < touch.pos[0] - self.ids.id.size[0] and self.ids.id.pos[0] + self.ids.id.size[0]/2 > touch.pos[0] - self.ids.id.size[0]:
                if id.lane == "left" or id.lane == "mid":
                    if id.lane == "mid":
                        if right_lane[id.index] == "x":
                            id_change_lane = True
                            id.lane = "right"
                            (right_lane[id.index], mid_lane[id.index]) = (mid_lane[id.index], right_lane[id.index])
                    elif id.lane == "left":
                        if mid_lane[id.index] == "x":
                            id_change_lane = True
                            id.lane = "mid"
                            (left_lane[id.index], mid_lane[id.index]) = (mid_lane[id.index], left_lane[id.index])
                    if id_change_lane == True:
                        self.ids.id.pos[0] += ((Window.width/5+3*Window.width/5/2)-Window.width/1536) - ((Window.width/5+3*Window.width/5/5)-Window.width/1536)
            
            elif self.ids.id.pos[0] + self.ids.id.size[0]/2 < touch.pos[0] + self.ids.id.size[0] and self.ids.id.pos[0] + self.ids.id.size[0] > touch.pos[0] + self.ids.id.size[0]:
                if id.lane == "right" or id.lane == "mid":
                    if id.lane == "mid":
                        if left_lane[id.index] == "x":
                            id_change_lane = True
                            id.lane = "left"
                            (left_lane[id.index], mid_lane[id.index]) = (mid_lane[id.index], left_lane[id.index])
                    elif id.lane == "right":
                        if mid_lane[id.index] == "x":
                            id_change_lane = True
                            id.lane = "mid"
                            (right_lane[id.index], mid_lane[id.index]) = (mid_lane[id.index], right_lane[id.index])
                    if id_change_lane == True:
                        self.ids.id.pos[0] -= ((Window.width/5+3*Window.width/5/2)-Window.width/1536) - ((Window.width/5+3*Window.width/5/5)-Window.width/1536)

        if self.ids.id.pos[0] > Window.width/2 + self.ids.id.size[0]:
            # move up right
            if self.ids.id.pos[0] < touch.pos[0] and self.ids.id.pos[0] + self.ids.id.size[0] > touch.pos[0] and self.ids.id.pos[1] + self.ids.id.size[1]/2 < touch.pos[1] and self.ids.id.pos[1] + self.ids.id.size[1] > touch.pos[1] and self.ids.id.pos[1] >= Window.height/5 and self.ids.id.pos[1] < 4*Window.height/5 - Window.height/12.7058823529 and id.spd > 0 and right_lane[id.index+1] == "x":
                self.ids.id.pos[1] += Window.height/12.7058823529
                id.spd -= 1
                (right_lane[id.index], right_lane[id.index+1]) = (right_lane[id.index+1], right_lane[id.index])
                id.index += 1
            # move down right
            if self.ids.id.pos[0] < touch.pos[0] and self.ids.id.pos[0] + self.ids.id.size[0] > touch.pos[0] and self.ids.id.pos[1] < touch.pos[1] and self.ids.id.pos[1] + self.ids.id.size[1]/2 > touch.pos[1] and self.ids.id.pos[1] >= Window.height/5 and self.ids.id.pos[1] > Window.height/5 + Window.height/12.7058823529 and id.spd > 0 and right_lane[id.index-1] == "x":
                self.ids.id.pos[1] -= Window.height/12.7058823529
                id.spd -= 1
                (right_lane[id.index], right_lane[id.index-1]) = (right_lane[id.index-1], right_lane[id.index])
                id.index -= 1

        elif self.ids.id.pos[0] < Window.width/2 - self.ids.id.size[0]:
            # move up left
            if self.ids.id.pos[0] < touch.pos[0] and self.ids.id.pos[0] + self.ids.id.size[0] > touch.pos[0] and self.ids.id.pos[1] + self.ids.id.size[1]/2 < touch.pos[1] and self.ids.id.pos[1] + self.ids.id.size[1] > touch.pos[1] and self.ids.id.pos[1] >= Window.height/5 and self.ids.id.pos[1] < 4*Window.height/5 - Window.height/12.7058823529 and id.spd > 0 and left_lane[id.index+1] == "x":
                self.ids.id.pos[1] += Window.height/12.7058823529
                id.spd -= 1
                (left_lane[id.index], left_lane[id.index+1]) = (left_lane[id.index+1], left_lane[id.index])
                id.index += 1
            # move down left
            if self.ids.id.pos[0] < touch.pos[0] and self.ids.id.pos[0] + self.ids.id.size[0] > touch.pos[0] and self.ids.id.pos[1] < touch.pos[1] and self.ids.id.pos[1] + self.ids.id.size[1]/2 > touch.pos[1] and self.ids.id.pos[1] >= Window.height/5 and self.ids.id.pos[1] > Window.height/5 + Window.height/12.7058823529 and id.spd > 0 and left_lane[id.index-1] == "x":
                self.ids.id.pos[1] -= Window.height/12.7058823529
                id.spd -= 1
                (left_lane[id.index], left_lane[id.index-1]) = (left_lane[id.index-1], left_lane[id.index])
                id.index -= 1
        else:
            # move up mid
            if self.ids.id.pos[0] < touch.pos[0] and self.ids.id.pos[0] + self.ids.id.size[0] > touch.pos[0] and self.ids.id.pos[1] + self.ids.id.size[1]/2 < touch.pos[1] and self.ids.id.pos[1] + self.ids.id.size[1] > touch.pos[1] and self.ids.id.pos[1] >= Window.height/5 and self.ids.id.pos[1] < 4*Window.height/5 - Window.height/12.7058823529 and id.spd > 0 and mid_lane[id.index+1] == "x":
                self.ids.id.pos[1] += Window.height/12.7058823529
                id.spd -= 1
                (mid_lane[id.index], mid_lane[id.index+1]) = (mid_lane[id.index+1], mid_lane[id.index])
                id.index += 1
            # move down mid
            if self.ids.id.pos[0] < touch.pos[0] and self.ids.id.pos[0] + self.ids.id.size[0] > touch.pos[0] and self.ids.id.pos[1] < touch.pos[1] and self.ids.id.pos[1] + self.ids.id.size[1]/2 > touch.pos[1] and self.ids.id.pos[1] >= Window.height/5 and self.ids.id.pos[1] > Window.height/5 + Window.height/12.7058823529 and id.spd > 0 and mid_lane[id.index-1] == "x":
                self.ids.id.pos[1] -= Window.height/12.7058823529
                id.spd -= 1
                (mid_lane[id.index], mid_lane[id.index-1]) = (mid_lane[id.index-1], mid_lane[id.index])
                id.index -= 1

            



    def on_touch_move(self, touch):
#########################################################################################################################################
# id
        if id_bool == True:
            self.ids.id.pos = touch.spos[0]*Window.width-self.ids.id.size[0]/2,touch.spos[1]*Window.height-self.ids.id.size[1]/2



    def on_touch_up(self, touch):
#########################################################################################################################################
# id
        global id_bool
        if id_bool == True:
            if p[0] < Window.width/2 and left_lane[1] == "x":
                self.ids.id.pos = (Window.width/5+3*Window.width/5/5)-Window.width/102.4, (Window.height/5+Window.height/45)+Window.height/16
                left_lane[1] = id
                id.lane = "left"
            elif p[0] > Window.width/2 and right_lane[1] == "x":
                self.ids.id.pos = (Window.width/5+3*Window.width/5/5*4)-Window.width/102.4, (Window.height/5+Window.height/45)+Window.height/16
                right_lane[1] = id 
                id.lane = "right"
            else:
                self.ids.id.pos = id_pos
        id_bool = False




