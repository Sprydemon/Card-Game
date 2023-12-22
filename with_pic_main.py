from kivy.app import App
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.label import Label

import random 

class Charecter:
    def __init__(self, atk, hp, spd, cd, team, source):
        self.atk = atk
        self.original_atk_stage_0 = atk
        self.hp = hp
        self.original_hp = hp
        self.original_hp_stage_0 = hp
        self.spd = spd
        self.original_spd = spd
        self.original_spd_stage_0 = spd
        self.cd = cd
        self.original_cd = cd
        self.original_cd_stage_0 = cd
        self.team = team
        self.index = 0
        self.lane = "none"
        self.alive = True
        self.did_change_lane = False
        self.source = source

    def cooldown(self):
        self.cd -= 1

    

    
    

attack = r"Images\+one attack.png"
attack2 = r"Images\+two attack.png"
attack3 = r"Images\+three attack.png"

health = r"Images\+one health.png"
health2 = r"Images\+two health.png"
health3 = r"Images\+three health.png"

speed = r"Images\+one speed.png"
speed2 = r"Images\+two speed.png" 

dec_cooldown = r"Images\-1 cooldown.png"
dec_cooldown2 = r"Images\-2 cooldown.png"
inc_cooldown = r"Images\+one cooldown.png"
inc_cooldown2 = r"Images\+two cooldown.png"

card_list = [attack, attack2, attack3, health, health2, health3, speed, speed2, attack, attack2, attack3, health, health2, health3, speed, speed2, dec_cooldown, inc_cooldown, dec_cooldown2, inc_cooldown2]
player_cards = card_list.copy()


class Hand:
    def __init__(self, deck):
        self.deck = deck
        self.stored = ["x","x","x","x"]

    def draw(self):
        for row in self.stored:
            if row == "x":
                index = self.stored.index(row)
                self.stored.remove("x")
                self.stored.insert(index, self.deck[0])
                self.deck.pop(0)
                break

    def start(self):
        self.shuffle()
        self.draw()
        self.draw()
        self.draw()
        self.draw()

    def use_card(self, used_card):
        self.deck.append(used_card)
        index = self.stored.index(used_card)
        self.stored.remove(used_card)
        self.stored.insert(index, "x")

    def shuffle(self):
        cards_num = len(self.deck) - 1
        deck_copy = self.deck.copy()
        self.deck.clear()
        while cards_num >= 0:
            rearrange = random.randint(0, cards_num)
            self.deck.append(deck_copy[rearrange])
            deck_copy.pop(rearrange)
            cards_num -= 1

player = Hand(player_cards)
player.shuffle()




global stage
stage = 1
global player_life
player_life = 3
global opponent_life
opponent_life = 3

global right_lane
right_lane = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"]
global mid_lane
mid_lane = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"]
global left_lane
left_lane = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"]

global core
core = ["x", "x", "x", "x"]
global O_core
O_core = ["x", "x", "x", "x"]
global hand1
hand1 = False
global hand2
hand2 = False
global hand3
hand3 = False
global hand4
hand4 = False
global draw_per_turn
draw_per_turn = 4
global damage_dealt
damage_dealt = 1
global damage_recived
damage_recived = 1

#########################################################################################################################################
swordman = Charecter(1, 1, 4, 0, "player", r"Images\Swords man.png")
global swordman_bool
swordman_bool = False
global swordman_battle
swordman_battle = False
global swordman_index
swordman_index = 9
#########################################################################################################################################
ion = Charecter(2, 2, 3, 1, "player", r"Images\ion.png")
global ion_bool
ion_bool = False
global ion_battle
ion_battle = False
global ion_index
ion_index = 9
#########################################################################################################################################
apex = Charecter(3, 3, 2, 2, "player", r"Images\Apex.png")
global apex_bool
apex_bool = False
global apex_battle
apex_battle = False
global apex_index
apex_index = 9
#########################################################################################################################################
blade = Charecter(4, 4, 2, 3, "player", r"Images\Blade.png")
global blade_bool
blade_bool = False
global blade_battle
blade_battle = False
global blade_index
blade_index = 9
#########################################################################################################################################
tank = Charecter(4, 4, 3, 4, "player", r"Images\tank.png")
global tank_bool
tank_bool = False
global tank_battle
tank_battle = False
global tank_index
tank_index = 9
#########################################################################################################################################
bomb = Charecter(6, 6, 1, 5, "player", r"Images\spike bomb.png")
global bomb_bool
bomb_bool = False
global bomb_batle
bomb_batle = False
global bomb_index
bomb_index = 9
#########################################################################################################################################
jolt = Charecter(5, 5, 4, 6, "player", r"Images\New jolt.png")
global jolt_bool
jolt_bool = False
global jolt_battle
jolt_battle = False
global jolt_index
jolt_index = 9

#########################################################################################################################################
O_swordman = Charecter(1, 1, 4, 1, "opponent", r"Images\Swords man.png")
global O_swordman_summon
O_swordman_summon = False
global O_swordman_index
O_swordman_index = 9
#########################################################################################################################################
O_ion = Charecter(2, 2, 3, 2, "opponent", r"Images\ion.png")
global O_ion_summon
O_ion_summon = False
global O_ion_index
O_ion_index = 9
#########################################################################################################################################
O_apex = Charecter(3, 3, 2, 3, "opponent", r"Images\Apex.png")
global O_apex_summon
O_apex_summon = False
global O_apex_index
O_apex_index = 9
#########################################################################################################################################
O_blade = Charecter(4, 4, 2, 4, "opponent", r"Images\Blade.png")
global O_blade_summon
O_blade_summon = False
global O_blade_index
O_blade_index = 9
#########################################################################################################################################
O_tank = Charecter(4, 4, 3, 5, "opponent", r"Images\tank.png")
global O_tank_summon
O_tank_summon = False
global O_tank_index
O_tank_index = 9
#########################################################################################################################################
O_bomb = Charecter(6, 6, 1, 6, "opponent", r"Images\spike bomb.png")
global O_bombn_summon
O_bomb_summon = False
global O_bomb_index
O_bomb_index = 9
#########################################################################################################################################
O_jolt = Charecter(5, 5, 4, 7, "opponent", r"Images\New jolt.png")
global O_jolt_summon
O_jolt_summon = False
global O_jolt_index
O_jolt_index = 9


global rest_spot
rest_spot = [swordman, ion, apex, blade, tank, bomb, jolt]
global O_rest_spot
O_rest_spot = [O_swordman, O_ion, O_apex, O_blade, O_tank, O_bomb, O_jolt]

global player_list
player_list = [swordman, ion, apex, blade, tank, bomb, jolt]
global opponent_list
opponent_list = [O_swordman, O_ion, O_apex, O_blade, O_tank, O_bomb, O_jolt]

class game_board(FloatLayout):


    def on_touch_down(self, touch):
        global opponent_life
        global draw_per_turn
        global damage_dealt


#########################################################################################################################################
# hand
        if touch.pos[0] > Window.width/5+3*Window.width/5-3*Window.width/5/6+3*Window.width/5/72 and touch.pos[0] < Window.width/5+3*Window.width/5-3*Window.width/5/6+3*Window.width/5/72 + 3*Window.width/5/6-3*Window.width/5/36 and touch.pos[1] > 0 and touch.pos[1] < Window.height/5-Window.height/Window.height/16 and draw_per_turn >= 1:
            player.draw()
            draw_per_turn -= 1
            if player.stored[0] != "x":
                self.ids.hand_one.source = player.stored[0]
            else:
                self.ids.hand_one.source = r"C:\Users\salam\OneDrive\Desktop\Visual studio\Images\card_sleeve.png"
            if player.stored[1] != "x":
                self.ids.hand_two.source = player.stored[1]
            else:
                self.ids.hand_two.source = r"C:\Users\salam\OneDrive\Desktop\Visual studio\Images\card_sleeve.png"
            if player.stored[2] != "x":
                self.ids.hand_three.source = player.stored[2]
            else:
                self.ids.hand_three.source = r"C:\Users\salam\OneDrive\Desktop\Visual studio\Images\card_sleeve.png"
            if player.stored[3] != "x":
                self.ids.hand_four.source = player.stored[3]
            else:
                self.ids.hand_four.source = r"C:\Users\salam\OneDrive\Desktop\Visual studio\Images\card_sleeve.png"

        if self.ids.hand_one.pos[0] < touch.pos[0] and self.ids.hand_one.pos[0] + self.ids.hand_one.size[0] > touch.pos[0] and self.ids.hand_one.pos[1] < touch.pos[1] and self.ids.hand_one.pos[1] + self.ids.hand_one.size[1] > touch.pos[1]:
            global hand1
            hand1 = True
        if self.ids.hand_two.pos[0] < touch.pos[0] and self.ids.hand_two.pos[0] + self.ids.hand_two.size[0] > touch.pos[0] and self.ids.hand_two.pos[1] < touch.pos[1] and self.ids.hand_two.pos[1] + self.ids.hand_two.size[1] > touch.pos[1]:
            global hand2
            hand2 = True
        if self.ids.hand_three.pos[0] < touch.pos[0] and self.ids.hand_three.pos[0] + self.ids.hand_three.size[0] > touch.pos[0] and self.ids.hand_three.pos[1] < touch.pos[1] and self.ids.hand_three.pos[1] + self.ids.hand_three.size[1] > touch.pos[1]:
            global hand3
            hand3 = True
        if self.ids.hand_four.pos[0] < touch.pos[0] and self.ids.hand_four.pos[0] + self.ids.hand_four.size[0] > touch.pos[0] and self.ids.hand_four.pos[1] < touch.pos[1] and self.ids.hand_four.pos[1] + self.ids.hand_four.size[1] > touch.pos[1]:
            global hand4
            hand4 = True

#########################################################################################################################################
# swordman

        if swordman.alive == True:
            # summon
            if self.ids.swordman.pos[0] < touch.pos[0] and self.ids.swordman.pos[0] + self.ids.swordman.size[0] > touch.pos[0] and self.ids.swordman.pos[1] < touch.pos[1] and self.ids.swordman.pos[1] + self.ids.swordman.size[1] > touch.pos[1] and self.ids.swordman.pos[1] <= Window.height/5 and swordman.cd <= 0:
                global swordman_battle
                global swordman_bool
                swordman_bool = True
                global swordman_pos
                swordman_pos = self.ids.swordman.pos[0], self.ids.swordman.pos[1]
                global swordman_index
                swordman_index = 1

            # change lane
            global swordman_change_lane
            swordman_change_lane = False
            if swordman.spd > 0:
                if swordman_index == 0 or swordman_index == 3 or swordman_index == 4 or swordman_index == 7:
                    if self.ids.swordman.pos[0] < touch.pos[0] - self.ids.swordman.size[0] and self.ids.swordman.pos[0] + self.ids.swordman.size[0]/2 > touch.pos[0] - self.ids.swordman.size[0] and self.ids.swordman.pos[1] < touch.pos[1] and self.ids.swordman.pos[1] + self.ids.swordman.size[1] > touch.pos[1]:
                        swordman.did_change_lane = True
                        if swordman.lane == "left" or swordman.lane == "mid":
                            if swordman.lane == "mid":
                                if right_lane[swordman_index] == "x":
                                    swordman_change_lane = True
                                    swordman.lane = "right"
                                    swordman.spd -= 1
                                    (right_lane[swordman_index], mid_lane[swordman_index]) = (mid_lane[swordman_index], right_lane[swordman_index])
                                else:
                                    if right_lane[swordman_index].team == "opponent":
                                        swordman_battle = True 
                                        swordman.hp -= right_lane[swordman_index].atk
                                        right_lane[swordman_index].hp -= swordman.atk
                            elif swordman.lane == "left":
                                if mid_lane[swordman_index] == "x":
                                    swordman_change_lane = True 
                                    swordman.lane = "mid"
                                    swordman.spd -= 1
                                    (left_lane[swordman_index], mid_lane[swordman_index]) = (mid_lane[swordman_index], left_lane[swordman_index])
                                else:
                                    if mid_lane[swordman_index].team == "opponent":
                                        swordman_battle = True 
                                        swordman.hp -= left_lane[swordman_index].atk
                                        left_lane[swordman_index].hp -= swordman.atk
                            if swordman_change_lane == True:
                                self.ids.swordman.pos[0] += ((Window.width/5+3*Window.width/5/2)-Window.width/1536) - ((Window.width/5+3*Window.width/5/5)-Window.width/1536)
                    
                    elif self.ids.swordman.pos[0] + self.ids.swordman.size[0]/2 < touch.pos[0] + self.ids.swordman.size[0] and self.ids.swordman.pos[0] + self.ids.swordman.size[0] > touch.pos[0] + self.ids.swordman.size[0] and self.ids.swordman.pos[1] < touch.pos[1] and self.ids.swordman.pos[1] + self.ids.swordman.size[1] > touch.pos[1]:
                        swordman.did_change_lane = True
                        if swordman.lane == "right" or swordman.lane == "mid":
                            if swordman.lane == "mid":
                                if left_lane[swordman_index] == "x":
                                    swordman_change_lane = True
                                    swordman.lane = "left"
                                    swordman.spd -= 1
                                    (left_lane[swordman_index], mid_lane[swordman_index]) = (mid_lane[swordman_index], left_lane[swordman_index])
                                else:
                                    if left_lane[swordman_index].team == "opponent":
                                        swordman_battle = True 
                                        swordman.hp -= left_lane[swordman_index].atk
                                        left_lane[swordman_index].hp -= swordman.atk
                            elif swordman.lane == "right":
                                if mid_lane[swordman_index] == "x":
                                    swordman_change_lane = True
                                    swordman.lane = "mid"
                                    swordman.spd -= 1
                                    (right_lane[swordman_index], mid_lane[swordman_index]) = (mid_lane[swordman_index], right_lane[swordman_index])
                                else:
                                    if mid_lane[swordman_index].team == "opponent":
                                        swordman_battle = True 
                                        swordman.hp -= right_lane[swordman_index].atk
                                        right_lane[swordman_index].hp -= swordman.atk
                            if swordman_change_lane == True:
                                self.ids.swordman.pos[0] -= ((Window.width/5+3*Window.width/5/2)-Window.width/1536) - ((Window.width/5+3*Window.width/5/5)-Window.width/1536)

            if self.ids.swordman.pos[0] > Window.width/2 + self.ids.swordman.size[0]:
                # move up right
                if self.ids.swordman.pos[0] < touch.pos[0] and self.ids.swordman.pos[0] + self.ids.swordman.size[0] > touch.pos[0] and self.ids.swordman.pos[1] + self.ids.swordman.size[1]/2 < touch.pos[1] and self.ids.swordman.pos[1] + self.ids.swordman.size[1] > touch.pos[1] and self.ids.swordman.pos[1] >= Window.height/5 and self.ids.swordman.pos[1] < 4*Window.height/5 - Window.height/12.7058823529 and swordman.spd > 0 and right_lane[swordman_index+1] == "x":
                    self.ids.swordman.pos[1] += Window.height/12.7058823529
                    swordman.spd -= 1
                    (right_lane[swordman_index], right_lane[swordman_index+1]) = (right_lane[swordman_index+1], right_lane[swordman_index])
                    swordman_index += 1
                else:
                    if right_lane[swordman_index+1] != "x" and right_lane[swordman_index+1].team == "opponent" and self.ids.swordman.pos[1] + self.ids.swordman.size[1]/2 < touch.pos[1] and self.ids.swordman.pos[1] + self.ids.swordman.size[1] > touch.pos[1]:
                        if swordman.did_change_lane == False:
                            swordman_battle = True 
                            swordman.hp -= right_lane[swordman_index+1].atk
                            right_lane[swordman_index+1].hp -= swordman.atk
                if self.ids.swordman.pos[0] < touch.pos[0] and self.ids.swordman.pos[0] + self.ids.swordman.size[0] > touch.pos[0] and self.ids.swordman.pos[1] + self.ids.swordman.size[1]/2 < touch.pos[1] and self.ids.swordman.pos[1] + self.ids.swordman.size[1] > touch.pos[1] and swordman_index == 7:
                    if damage_dealt == 1:
                        opponent_life -= 1
                        damage_dealt = 0

                # move down right
                if self.ids.swordman.pos[0] < touch.pos[0] and self.ids.swordman.pos[0] + self.ids.swordman.size[0] > touch.pos[0] and self.ids.swordman.pos[1] < touch.pos[1] and self.ids.swordman.pos[1] + self.ids.swordman.size[1]/2 > touch.pos[1] and self.ids.swordman.pos[1] >= Window.height/5 and self.ids.swordman.pos[1] > Window.height/5 + Window.height/12.7058823529 and swordman.spd > 0 and right_lane[swordman_index-1] == "x":
                    self.ids.swordman.pos[1] -= Window.height/12.7058823529
                    swordman.spd -= 1
                    (right_lane[swordman_index], right_lane[swordman_index-1]) = (right_lane[swordman_index-1], right_lane[swordman_index])
                    swordman_index -= 1
                else:
                    if right_lane[swordman_index-1] != "x" and right_lane[swordman_index-1].team == "opponent" and self.ids.swordman.pos[1] < touch.pos[1] and self.ids.swordman.pos[1] + self.ids.swordman.size[1]/2 > touch.pos[1]:
                        if swordman.did_change_lane == False:
                            swordman_battle = True 
                            swordman.hp -= right_lane[swordman_index-1].atk
                            right_lane[swordman_index-1].hp -= swordman.atk

            elif self.ids.swordman.pos[0] < Window.width/2 - self.ids.swordman.size[0]:
                # move up left
                if self.ids.swordman.pos[0] < touch.pos[0] and self.ids.swordman.pos[0] + self.ids.swordman.size[0] > touch.pos[0] and self.ids.swordman.pos[1] + self.ids.swordman.size[1]/2 < touch.pos[1] and self.ids.swordman.pos[1] + self.ids.swordman.size[1] > touch.pos[1] and self.ids.swordman.pos[1] >= Window.height/5 and self.ids.swordman.pos[1] < 4*Window.height/5 - Window.height/12.7058823529 and swordman.spd > 0 and left_lane[swordman_index+1] == "x":
                    self.ids.swordman.pos[1] += Window.height/12.7058823529
                    swordman.spd -= 1
                    (left_lane[swordman_index], left_lane[swordman_index+1]) = (left_lane[swordman_index+1], left_lane[swordman_index])
                    swordman_index += 1
                else:
                    if left_lane[swordman_index+1] != "x" and left_lane[swordman_index+1].team == "opponent" and self.ids.swordman.pos[1] + self.ids.swordman.size[1]/2 < touch.pos[1] and self.ids.swordman.pos[1] + self.ids.swordman.size[1] > touch.pos[1]:
                        if swordman.did_change_lane == False:
                            swordman_battle = True 
                            swordman.hp -= left_lane[swordman_index+1].atk
                            left_lane[swordman_index+1].hp -= swordman.atk
                if self.ids.swordman.pos[0] < touch.pos[0] and self.ids.swordman.pos[0] + self.ids.swordman.size[0] > touch.pos[0] and self.ids.swordman.pos[1] + self.ids.swordman.size[1]/2 < touch.pos[1] and self.ids.swordman.pos[1] + self.ids.swordman.size[1] > touch.pos[1] and swordman_index == 7:
                    if damage_dealt == 1:
                        opponent_life -= 1
                        damage_dealt = 0

                # move down left
                if self.ids.swordman.pos[0] < touch.pos[0] and self.ids.swordman.pos[0] + self.ids.swordman.size[0] > touch.pos[0] and self.ids.swordman.pos[1] < touch.pos[1] and self.ids.swordman.pos[1] + self.ids.swordman.size[1]/2 > touch.pos[1] and self.ids.swordman.pos[1] >= Window.height/5 and self.ids.swordman.pos[1] > Window.height/5 + Window.height/12.7058823529 and swordman.spd > 0 and left_lane[swordman_index-1] == "x":
                    self.ids.swordman.pos[1] -= Window.height/12.7058823529
                    swordman.spd -= 1
                    (left_lane[swordman_index], left_lane[swordman_index-1]) = (left_lane[swordman_index-1], left_lane[swordman_index])
                    swordman_index -= 1
                else:
                    if left_lane[swordman_index-1] != "x" and left_lane[swordman_index-1].team == "opponent" and self.ids.swordman.pos[1] < touch.pos[1] and self.ids.swordman.pos[1] + self.ids.swordman.size[1]/2 > touch.pos[1]:
                        if swordman.did_change_lane == False:
                            swordman_battle = True 
                            swordman.hp -= left_lane[swordman_index-1].atk
                            left_lane[swordman_index-1].hp -= swordman.atk

            else:
                # move up mid
                if self.ids.swordman.pos[0] < touch.pos[0] and self.ids.swordman.pos[0] + self.ids.swordman.size[0] > touch.pos[0] and self.ids.swordman.pos[1] + self.ids.swordman.size[1]/2 < touch.pos[1] and self.ids.swordman.pos[1] + self.ids.swordman.size[1] > touch.pos[1] and self.ids.swordman.pos[1] >= Window.height/5 and self.ids.swordman.pos[1] < 4*Window.height/5 - Window.height/12.7058823529 and swordman.spd > 0 and mid_lane[swordman_index+1] == "x":
                    self.ids.swordman.pos[1] += Window.height/12.7058823529
                    swordman.spd -= 1
                    (mid_lane[swordman_index], mid_lane[swordman_index+1]) = (mid_lane[swordman_index+1], mid_lane[swordman_index])
                    swordman_index += 1
                else:
                    if mid_lane[swordman_index+1] != "x" and mid_lane[swordman_index+1].team == "opponent" and self.ids.swordman.pos[1] + self.ids.swordman.size[1]/2 < touch.pos[1] and self.ids.swordman.pos[1] + self.ids.swordman.size[1] > touch.pos[1]:
                        if swordman.did_change_lane == False:
                            swordman_battle = True 
                            swordman.hp -= mid_lane[swordman_index+1].atk
                            mid_lane[swordman_index+1].hp -= swordman.atk
                # move down mid
                if self.ids.swordman.pos[0] < touch.pos[0] and self.ids.swordman.pos[0] + self.ids.swordman.size[0] > touch.pos[0] and self.ids.swordman.pos[1] < touch.pos[1] and self.ids.swordman.pos[1] + self.ids.swordman.size[1]/2 > touch.pos[1] and self.ids.swordman.pos[1] >= Window.height/5 and self.ids.swordman.pos[1] > Window.height/5 + Window.height/12.7058823529 and swordman.spd > 0 and mid_lane[swordman_index-1] == "x":
                    self.ids.swordman.pos[1] -= Window.height/12.7058823529
                    swordman.spd -= 1
                    (mid_lane[swordman_index], mid_lane[swordman_index-1]) = (mid_lane[swordman_index-1], mid_lane[swordman_index])
                    swordman_index -= 1
                else:
                    if mid_lane[swordman_index-1] != "x" and mid_lane[swordman_index-1].team == "opponent" and self.ids.swordman.pos[1] < touch.pos[1] and self.ids.swordman.pos[1] + self.ids.swordman.size[1]/2 > touch.pos[1]:
                        if swordman.did_change_lane == False:
                            swordman_battle = True 
                            swordman.hp -= mid_lane[swordman_index-1].atk
                            mid_lane[swordman_index-1].hp -= swordman.atk
########################################################################################################################################
# ion

        if ion.alive == True:
            # summon
            if self.ids.ion.pos[0] < touch.pos[0] and self.ids.ion.pos[0] + self.ids.ion.size[0] > touch.pos[0] and self.ids.ion.pos[1] < touch.pos[1] and self.ids.ion.pos[1] + self.ids.ion.size[1] > touch.pos[1] and self.ids.ion.pos[1] <= Window.height/5 and ion.cd <= 0:
                global ion_battle
                global ion_bool
                ion_bool = True
                global ion_pos
                ion_pos = self.ids.ion.pos[0], self.ids.ion.pos[1]
                global ion_index
                ion_index = 1

            # change lane
            global ion_change_lane
            ion_change_lane = False
            if ion.spd > 0:
                if ion_index == 0 or ion_index == 3 or ion_index == 4 or ion_index == 7:
                    if self.ids.ion.pos[0] < touch.pos[0] - self.ids.ion.size[0] and self.ids.ion.pos[0] + self.ids.ion.size[0]/2 > touch.pos[0] - self.ids.ion.size[0] and self.ids.ion.pos[1] < touch.pos[1] and self.ids.ion.pos[1] + self.ids.ion.size[1] > touch.pos[1]:
                        ion.did_change_lane = True
                        if ion.lane == "left" or ion.lane == "mid":
                            if ion.lane == "mid":
                                if right_lane[ion_index] == "x":
                                    ion_change_lane = True
                                    ion.lane = "right"
                                    ion.spd -= 1
                                    (right_lane[ion_index], mid_lane[ion_index]) = (mid_lane[ion_index], right_lane[ion_index])
                                else:
                                    if right_lane[ion_index].team == "opponent":
                                        ion_battle = True 
                                        ion.hp -= right_lane[ion_index].atk
                                        right_lane[ion_index].hp -= ion.atk
                            elif ion.lane == "left":
                                if mid_lane[ion_index] == "x":
                                    ion_change_lane = True 
                                    ion.lane = "mid"
                                    ion.spd -= 1
                                    (left_lane[ion_index], mid_lane[ion_index]) = (mid_lane[ion_index], left_lane[ion_index])
                                else:
                                    if mid_lane[ion_index].team == "opponent":
                                        ion_battle = True 
                                        ion.hp -= left_lane[ion_index].atk
                                        left_lane[ion_index].hp -= ion.atk
                            if ion_change_lane == True:
                                self.ids.ion.pos[0] += ((Window.width/5+3*Window.width/5/2)-Window.width/1536) - ((Window.width/5+3*Window.width/5/5)-Window.width/1536)
                    
                    elif self.ids.ion.pos[0] + self.ids.ion.size[0]/2 < touch.pos[0] + self.ids.ion.size[0] and self.ids.ion.pos[0] + self.ids.ion.size[0] > touch.pos[0] + self.ids.ion.size[0] and self.ids.ion.pos[1] < touch.pos[1] and self.ids.ion.pos[1] + self.ids.ion.size[1] > touch.pos[1]:
                        ion.did_change_lane = True
                        if ion.lane == "right" or ion.lane == "mid":
                            if ion.lane == "mid":
                                if left_lane[ion_index] == "x":
                                    ion_change_lane = True
                                    ion.lane = "left"
                                    ion.spd -= 1
                                    (left_lane[ion_index], mid_lane[ion_index]) = (mid_lane[ion_index], left_lane[ion_index])
                                else:
                                    if left_lane[ion_index].team == "opponent":
                                        ion_battle = True 
                                        ion.hp -= left_lane[ion_index].atk
                                        left_lane[ion_index].hp -= ion.atk
                            elif ion.lane == "right":
                                if mid_lane[ion_index] == "x":
                                    ion_change_lane = True
                                    ion.lane = "mid"
                                    ion.spd -= 1
                                    (right_lane[ion_index], mid_lane[ion_index]) = (mid_lane[ion_index], right_lane[ion_index])
                                else:
                                    if mid_lane[ion_index].team == "opponent":
                                        ion_battle = True 
                                        ion.hp -= right_lane[ion_index].atk
                                        right_lane[ion_index].hp -= ion.atk
                            if ion_change_lane == True:
                                self.ids.ion.pos[0] -= ((Window.width/5+3*Window.width/5/2)-Window.width/1536) - ((Window.width/5+3*Window.width/5/5)-Window.width/1536)
            if self.ids.ion.pos[0] > Window.width/2 + self.ids.ion.size[0]:
                # move up right
                if self.ids.ion.pos[0] < touch.pos[0] and self.ids.ion.pos[0] + self.ids.ion.size[0] > touch.pos[0] and self.ids.ion.pos[1] + self.ids.ion.size[1]/2 < touch.pos[1] and self.ids.ion.pos[1] + self.ids.ion.size[1] > touch.pos[1] and self.ids.ion.pos[1] >= Window.height/5 and self.ids.ion.pos[1] < 4*Window.height/5 - Window.height/12.7058823529 and ion.spd > 0 and right_lane[ion_index+1] == "x":
                    self.ids.ion.pos[1] += Window.height/12.7058823529
                    ion.spd -= 1
                    (right_lane[ion_index], right_lane[ion_index+1]) = (right_lane[ion_index+1], right_lane[ion_index])
                    ion_index += 1
                else:
                    if right_lane[ion_index+1] != "x" and right_lane[ion_index+1].team == "opponent" and self.ids.ion.pos[1] + self.ids.ion.size[1]/2 < touch.pos[1] and self.ids.ion.pos[1] + self.ids.ion.size[1] > touch.pos[1]:
                        if ion.did_change_lane == False:
                            ion_battle = True 
                            ion.hp -= right_lane[ion_index+1].atk
                            right_lane[ion_index+1].hp -= ion.atk
                if self.ids.ion.pos[0] < touch.pos[0] and self.ids.ion.pos[0] + self.ids.ion.size[0] > touch.pos[0] and self.ids.ion.pos[1] + self.ids.ion.size[1]/2 < touch.pos[1] and self.ids.ion.pos[1] + self.ids.ion.size[1] > touch.pos[1] and ion_index == 7:
                    if damage_dealt == 1:
                        opponent_life -= 1
                        damage_dealt = 0

                # move down right
                if self.ids.ion.pos[0] < touch.pos[0] and self.ids.ion.pos[0] + self.ids.ion.size[0] > touch.pos[0] and self.ids.ion.pos[1] < touch.pos[1] and self.ids.ion.pos[1] + self.ids.ion.size[1]/2 > touch.pos[1] and self.ids.ion.pos[1] >= Window.height/5 and self.ids.ion.pos[1] > Window.height/5 + Window.height/12.7058823529 and ion.spd > 0 and right_lane[ion_index-1] == "x":
                    self.ids.ion.pos[1] -= Window.height/12.7058823529
                    ion.spd -= 1
                    (right_lane[ion_index], right_lane[ion_index-1]) = (right_lane[ion_index-1], right_lane[ion_index])
                    ion_index -= 1
                else:
                    if right_lane[ion_index-1] != "x" and right_lane[ion_index-1].team == "opponent" and self.ids.ion.pos[1] < touch.pos[1] and self.ids.ion.pos[1] + self.ids.ion.size[1]/2 > touch.pos[1]:
                        if ion.did_change_lane == False:
                            ion_battle = True 
                            ion.hp -= right_lane[ion_index-1].atk
                            right_lane[ion_index-1].hp -= ion.atk

            elif self.ids.ion.pos[0] < Window.width/2 - self.ids.ion.size[0]:
                # move up left
                if self.ids.ion.pos[0] < touch.pos[0] and self.ids.ion.pos[0] + self.ids.ion.size[0] > touch.pos[0] and self.ids.ion.pos[1] + self.ids.ion.size[1]/2 < touch.pos[1] and self.ids.ion.pos[1] + self.ids.ion.size[1] > touch.pos[1] and self.ids.ion.pos[1] >= Window.height/5 and self.ids.ion.pos[1] < 4*Window.height/5 - Window.height/12.7058823529 and ion.spd > 0 and left_lane[ion_index+1] == "x":
                    self.ids.ion.pos[1] += Window.height/12.7058823529
                    ion.spd -= 1
                    (left_lane[ion_index], left_lane[ion_index+1]) = (left_lane[ion_index+1], left_lane[ion_index])
                    ion_index += 1
                else:
                    if left_lane[ion_index+1] != "x" and left_lane[ion_index+1].team == "opponent" and self.ids.ion.pos[1] + self.ids.ion.size[1]/2 < touch.pos[1] and self.ids.ion.pos[1] + self.ids.ion.size[1] > touch.pos[1]:
                        if ion.did_change_lane == False:
                            ion_battle = True 
                            ion.hp -= left_lane[ion_index+1].atk
                            left_lane[ion_index+1].hp -= ion.atk
                if self.ids.ion.pos[0] < touch.pos[0] and self.ids.ion.pos[0] + self.ids.ion.size[0] > touch.pos[0] and self.ids.ion.pos[1] + self.ids.ion.size[1]/2 < touch.pos[1] and self.ids.ion.pos[1] + self.ids.ion.size[1] > touch.pos[1] and ion_index == 7:
                    if damage_dealt == 1:
                        opponent_life -= 1
                        damage_dealt = 0

                # move down left
                if self.ids.ion.pos[0] < touch.pos[0] and self.ids.ion.pos[0] + self.ids.ion.size[0] > touch.pos[0] and self.ids.ion.pos[1] < touch.pos[1] and self.ids.ion.pos[1] + self.ids.ion.size[1]/2 > touch.pos[1] and self.ids.ion.pos[1] >= Window.height/5 and self.ids.ion.pos[1] > Window.height/5 + Window.height/12.7058823529 and ion.spd > 0 and left_lane[ion_index-1] == "x":
                    self.ids.ion.pos[1] -= Window.height/12.7058823529
                    ion.spd -= 1
                    (left_lane[ion_index], left_lane[ion_index-1]) = (left_lane[ion_index-1], left_lane[ion_index])
                    ion_index -= 1
                else:
                    if left_lane[ion_index-1] != "x" and left_lane[ion_index-1].team == "opponent" and self.ids.ion.pos[1] < touch.pos[1] and self.ids.ion.pos[1] + self.ids.ion.size[1]/2 > touch.pos[1]:
                        if ion.did_change_lane == False:
                            ion_battle = True 
                            ion.hp -= left_lane[ion_index-1].atk
                            left_lane[ion_index-1].hp -= ion.atk

            else:
                # move up mid
                if self.ids.ion.pos[0] < touch.pos[0] and self.ids.ion.pos[0] + self.ids.ion.size[0] > touch.pos[0] and self.ids.ion.pos[1] + self.ids.ion.size[1]/2 < touch.pos[1] and self.ids.ion.pos[1] + self.ids.ion.size[1] > touch.pos[1] and self.ids.ion.pos[1] >= Window.height/5 and self.ids.ion.pos[1] < 4*Window.height/5 - Window.height/12.7058823529 and ion.spd > 0 and mid_lane[ion_index+1] == "x":
                    self.ids.ion.pos[1] += Window.height/12.7058823529
                    ion.spd -= 1
                    (mid_lane[ion_index], mid_lane[ion_index+1]) = (mid_lane[ion_index+1], mid_lane[ion_index])
                    ion_index += 1
                else:
                    if mid_lane[ion_index+1] != "x" and mid_lane[ion_index+1].team == "opponent" and self.ids.ion.pos[1] + self.ids.ion.size[1]/2 < touch.pos[1] and self.ids.ion.pos[1] + self.ids.ion.size[1] > touch.pos[1]:
                        if ion.did_change_lane == False:
                            ion_battle = True 
                            ion.hp -= mid_lane[ion_index+1].atk
                            mid_lane[ion_index+1].hp -= ion.atk
                # move down mid
                if self.ids.ion.pos[0] < touch.pos[0] and self.ids.ion.pos[0] + self.ids.ion.size[0] > touch.pos[0] and self.ids.ion.pos[1] < touch.pos[1] and self.ids.ion.pos[1] + self.ids.ion.size[1]/2 > touch.pos[1] and self.ids.ion.pos[1] >= Window.height/5 and self.ids.ion.pos[1] > Window.height/5 + Window.height/12.7058823529 and ion.spd > 0 and mid_lane[ion_index-1] == "x":
                    self.ids.ion.pos[1] -= Window.height/12.7058823529
                    ion.spd -= 1
                    (mid_lane[ion_index], mid_lane[ion_index-1]) = (mid_lane[ion_index-1], mid_lane[ion_index])
                    ion_index -= 1
                else:
                    if mid_lane[ion_index-1] != "x" and mid_lane[ion_index-1].team == "opponent" and self.ids.ion.pos[1] < touch.pos[1] and self.ids.ion.pos[1] + self.ids.ion.size[1]/2 > touch.pos[1]:
                        if ion.did_change_lane == False:
                            ion_battle = True 
                            ion.hp -= mid_lane[ion_index-1].atk
                            mid_lane[ion_index-1].hp -= ion.atk
#########################################################################################################################################
# apex

        if apex.alive == True:
            # summon
            if self.ids.apex.pos[0] < touch.pos[0] and self.ids.apex.pos[0] + self.ids.apex.size[0] > touch.pos[0] and self.ids.apex.pos[1] < touch.pos[1] and self.ids.apex.pos[1] + self.ids.apex.size[1] > touch.pos[1] and self.ids.apex.pos[1] <= Window.height/5 and apex.cd <= 0:
                global apex_battle
                global apex_bool
                apex_bool = True
                global apex_pos
                apex_pos = self.ids.apex.pos[0], self.ids.apex.pos[1]
                global apex_index
                apex_index = 1

            # change lane
            global apex_change_lane
            apex_change_lane = False
            if apex.spd > 0:
                if apex_index == 0 or apex_index == 3 or apex_index == 4 or apex_index == 7:
                    if self.ids.apex.pos[0] < touch.pos[0] - self.ids.apex.size[0] and self.ids.apex.pos[0] + self.ids.apex.size[0]/2 > touch.pos[0] - self.ids.apex.size[0] and self.ids.apex.pos[1] < touch.pos[1] and self.ids.apex.pos[1] + self.ids.apex.size[1] > touch.pos[1]:
                        apex.did_change_lane = True
                        if apex.lane == "left" or apex.lane == "mid":
                            if apex.lane == "mid":
                                if right_lane[apex_index] == "x":
                                    apex_change_lane = True
                                    apex.lane = "right"
                                    apex.spd -= 1
                                    (right_lane[apex_index], mid_lane[apex_index]) = (mid_lane[apex_index], right_lane[apex_index])
                                else:
                                    if right_lane[apex_index].team == "opponent":
                                        apex_battle = True 
                                        apex.hp -= right_lane[apex_index].atk
                                        right_lane[apex_index].hp -= apex.atk
                            elif apex.lane == "left":
                                if mid_lane[apex_index] == "x":
                                    apex_change_lane = True 
                                    apex.lane = "mid"
                                    apex.spd -= 1
                                    (left_lane[apex_index], mid_lane[apex_index]) = (mid_lane[apex_index], left_lane[apex_index])
                                else:
                                    if mid_lane[apex_index].team == "opponent":
                                        apex_battle = True 
                                        apex.hp -= left_lane[apex_index].atk
                                        left_lane[apex_index].hp -= apex.atk
                            if apex_change_lane == True:
                                self.ids.apex.pos[0] += ((Window.width/5+3*Window.width/5/2)-Window.width/1536) - ((Window.width/5+3*Window.width/5/5)-Window.width/1536)
                    
                    elif self.ids.apex.pos[0] + self.ids.apex.size[0]/2 < touch.pos[0] + self.ids.apex.size[0] and self.ids.apex.pos[0] + self.ids.apex.size[0] > touch.pos[0] + self.ids.apex.size[0] and self.ids.apex.pos[1] < touch.pos[1] and self.ids.apex.pos[1] + self.ids.apex.size[1] > touch.pos[1]:
                        apex.did_change_lane = True
                        if apex.lane == "right" or apex.lane == "mid":
                            if apex.lane == "mid":
                                if left_lane[apex_index] == "x":
                                    apex_change_lane = True
                                    apex.lane = "left"
                                    apex.spd -= 1
                                    (left_lane[apex_index], mid_lane[apex_index]) = (mid_lane[apex_index], left_lane[apex_index])
                                else:
                                    if left_lane[apex_index].team == "opponent":
                                        apex_battle = True 
                                        apex.hp -= left_lane[apex_index].atk
                                        left_lane[apex_index].hp -= apex.atk
                            elif apex.lane == "right":
                                if mid_lane[apex_index] == "x":
                                    apex_change_lane = True
                                    apex.lane = "mid"
                                    apex.spd -= 1
                                    (right_lane[apex_index], mid_lane[apex_index]) = (mid_lane[apex_index], right_lane[apex_index])
                                else:
                                    if mid_lane[apex_index].team == "opponent":
                                        apex_battle = True 
                                        apex.hp -= right_lane[apex_index].atk
                                        right_lane[apex_index].hp -= apex.atk
                            if apex_change_lane == True:
                                self.ids.apex.pos[0] -= ((Window.width/5+3*Window.width/5/2)-Window.width/1536) - ((Window.width/5+3*Window.width/5/5)-Window.width/1536)

            if self.ids.apex.pos[0] > Window.width/2 + self.ids.apex.size[0]:
                # move up right
                if self.ids.apex.pos[0] < touch.pos[0] and self.ids.apex.pos[0] + self.ids.apex.size[0] > touch.pos[0] and self.ids.apex.pos[1] + self.ids.apex.size[1]/2 < touch.pos[1] and self.ids.apex.pos[1] + self.ids.apex.size[1] > touch.pos[1] and self.ids.apex.pos[1] >= Window.height/5 and self.ids.apex.pos[1] < 4*Window.height/5 - Window.height/12.7058823529 and apex.spd > 0 and right_lane[apex_index+1] == "x":
                    self.ids.apex.pos[1] += Window.height/12.7058823529
                    apex.spd -= 1
                    (right_lane[apex_index], right_lane[apex_index+1]) = (right_lane[apex_index+1], right_lane[apex_index])
                    apex_index += 1
                else:
                    if right_lane[apex_index+1] != "x" and right_lane[apex_index+1].team == "opponent" and self.ids.apex.pos[1] + self.ids.apex.size[1]/2 < touch.pos[1] and self.ids.apex.pos[1] + self.ids.apex.size[1] > touch.pos[1]:
                        if apex.did_change_lane == False:
                            apex_battle = True 
                            apex.hp -= right_lane[apex_index+1].atk
                            right_lane[apex_index+1].hp -= apex.atk
                if self.ids.apex.pos[0] < touch.pos[0] and self.ids.apex.pos[0] + self.ids.apex.size[0] > touch.pos[0] and self.ids.apex.pos[1] + self.ids.apex.size[1]/2 < touch.pos[1] and self.ids.apex.pos[1] + self.ids.apex.size[1] > touch.pos[1] and apex_index == 7:
                    if damage_dealt == 1:
                        opponent_life -= 1
                        damage_dealt = 0

                # move down right
                if self.ids.apex.pos[0] < touch.pos[0] and self.ids.apex.pos[0] + self.ids.apex.size[0] > touch.pos[0] and self.ids.apex.pos[1] < touch.pos[1] and self.ids.apex.pos[1] + self.ids.apex.size[1]/2 > touch.pos[1] and self.ids.apex.pos[1] >= Window.height/5 and self.ids.apex.pos[1] > Window.height/5 + Window.height/12.7058823529 and apex.spd > 0 and right_lane[apex_index-1] == "x":
                    self.ids.apex.pos[1] -= Window.height/12.7058823529
                    apex.spd -= 1
                    (right_lane[apex_index], right_lane[apex_index-1]) = (right_lane[apex_index-1], right_lane[apex_index])
                    apex_index -= 1
                else:
                    if right_lane[apex_index-1] != "x" and right_lane[apex_index-1].team == "opponent" and self.ids.apex.pos[1] < touch.pos[1] and self.ids.apex.pos[1] + self.ids.apex.size[1]/2 > touch.pos[1]:
                        if apex.did_change_lane == False:
                            apex_battle = True 
                            apex.hp -= right_lane[apex_index-1].atk
                            right_lane[apex_index-1].hp -= apex.atk

            elif self.ids.apex.pos[0] < Window.width/2 - self.ids.apex.size[0]:
                # move up left
                if self.ids.apex.pos[0] < touch.pos[0] and self.ids.apex.pos[0] + self.ids.apex.size[0] > touch.pos[0] and self.ids.apex.pos[1] + self.ids.apex.size[1]/2 < touch.pos[1] and self.ids.apex.pos[1] + self.ids.apex.size[1] > touch.pos[1] and self.ids.apex.pos[1] >= Window.height/5 and self.ids.apex.pos[1] < 4*Window.height/5 - Window.height/12.7058823529 and apex.spd > 0 and left_lane[apex_index+1] == "x":
                    self.ids.apex.pos[1] += Window.height/12.7058823529
                    apex.spd -= 1
                    (left_lane[apex_index], left_lane[apex_index+1]) = (left_lane[apex_index+1], left_lane[apex_index])
                    apex_index += 1
                else:
                    if left_lane[apex_index+1] != "x" and left_lane[apex_index+1].team == "opponent" and self.ids.apex.pos[1] + self.ids.apex.size[1]/2 < touch.pos[1] and self.ids.apex.pos[1] + self.ids.apex.size[1] > touch.pos[1]:
                        if apex.did_change_lane == False:
                            apex_battle = True 
                            apex.hp -= left_lane[apex_index+1].atk
                            left_lane[apex_index+1].hp -= apex.atk
                if self.ids.apex.pos[0] < touch.pos[0] and self.ids.apex.pos[0] + self.ids.apex.size[0] > touch.pos[0] and self.ids.apex.pos[1] + self.ids.apex.size[1]/2 < touch.pos[1] and self.ids.apex.pos[1] + self.ids.apex.size[1] > touch.pos[1] and apex_index == 7:
                    if damage_dealt == 1:
                        opponent_life -= 1
                        damage_dealt = 0

                # move down left
                if self.ids.apex.pos[0] < touch.pos[0] and self.ids.apex.pos[0] + self.ids.apex.size[0] > touch.pos[0] and self.ids.apex.pos[1] < touch.pos[1] and self.ids.apex.pos[1] + self.ids.apex.size[1]/2 > touch.pos[1] and self.ids.apex.pos[1] >= Window.height/5 and self.ids.apex.pos[1] > Window.height/5 + Window.height/12.7058823529 and apex.spd > 0 and left_lane[apex_index-1] == "x":
                    self.ids.apex.pos[1] -= Window.height/12.7058823529
                    apex.spd -= 1
                    (left_lane[apex_index], left_lane[apex_index-1]) = (left_lane[apex_index-1], left_lane[apex_index])
                    apex_index -= 1
                else:
                    if left_lane[apex_index-1] != "x" and left_lane[apex_index-1].team == "opponent" and self.ids.apex.pos[1] < touch.pos[1] and self.ids.apex.pos[1] + self.ids.apex.size[1]/2 > touch.pos[1]:
                        if apex.did_change_lane == False:
                            apex_battle = True 
                            apex.hp -= left_lane[apex_index-1].atk
                            left_lane[apex_index-1].hp -= apex.atk

            else:
                # move up mid
                if self.ids.apex.pos[0] < touch.pos[0] and self.ids.apex.pos[0] + self.ids.apex.size[0] > touch.pos[0] and self.ids.apex.pos[1] + self.ids.apex.size[1]/2 < touch.pos[1] and self.ids.apex.pos[1] + self.ids.apex.size[1] > touch.pos[1] and self.ids.apex.pos[1] >= Window.height/5 and self.ids.apex.pos[1] < 4*Window.height/5 - Window.height/12.7058823529 and apex.spd > 0 and mid_lane[apex_index+1] == "x":
                    self.ids.apex.pos[1] += Window.height/12.7058823529
                    apex.spd -= 1
                    (mid_lane[apex_index], mid_lane[apex_index+1]) = (mid_lane[apex_index+1], mid_lane[apex_index])
                    apex_index += 1
                else:
                    if mid_lane[apex_index+1] != "x" and mid_lane[apex_index+1].team == "opponent" and self.ids.apex.pos[1] + self.ids.apex.size[1]/2 < touch.pos[1] and self.ids.apex.pos[1] + self.ids.apex.size[1] > touch.pos[1]:
                        if apex.did_change_lane == False:
                            apex_battle = True 
                            apex.hp -= mid_lane[apex_index+1].atk
                            mid_lane[apex_index+1].hp -= apex.atk
                # move down mid
                if self.ids.apex.pos[0] < touch.pos[0] and self.ids.apex.pos[0] + self.ids.apex.size[0] > touch.pos[0] and self.ids.apex.pos[1] < touch.pos[1] and self.ids.apex.pos[1] + self.ids.apex.size[1]/2 > touch.pos[1] and self.ids.apex.pos[1] >= Window.height/5 and self.ids.apex.pos[1] > Window.height/5 + Window.height/12.7058823529 and apex.spd > 0 and mid_lane[apex_index-1] == "x":
                    self.ids.apex.pos[1] -= Window.height/12.7058823529
                    apex.spd -= 1
                    (mid_lane[apex_index], mid_lane[apex_index-1]) = (mid_lane[apex_index-1], mid_lane[apex_index])
                    apex_index -= 1
                else:
                    if mid_lane[apex_index-1] != "x" and mid_lane[apex_index-1].team == "opponent" and self.ids.apex.pos[1] < touch.pos[1] and self.ids.apex.pos[1] + self.ids.apex.size[1]/2 > touch.pos[1]:
                        if apex.did_change_lane == False:
                            apex_battle = True 
                            apex.hp -= mid_lane[apex_index-1].atk
                            mid_lane[apex_index-1].hp -= apex.atk
#########################################################################################################################################
# blade
 
        if blade.alive == True:
            # summon
            if self.ids.blade.pos[0] < touch.pos[0] and self.ids.blade.pos[0] + self.ids.blade.size[0] > touch.pos[0] and self.ids.blade.pos[1] < touch.pos[1] and self.ids.blade.pos[1] + self.ids.blade.size[1] > touch.pos[1] and self.ids.blade.pos[1] <= Window.height/5 and blade.cd <= 0:
                global blade_battle
                global blade_bool
                blade_bool = True
                global blade_pos
                blade_pos = self.ids.blade.pos[0], self.ids.blade.pos[1]
                global blade_index
                blade_index = 1

            # change lane
            global blade_change_lane
            blade_change_lane = False
            if blade.spd > 0:
                if blade_index == 0 or blade_index == 3 or blade_index == 4 or blade_index == 7:
                    if self.ids.blade.pos[0] < touch.pos[0] - self.ids.blade.size[0] and self.ids.blade.pos[0] + self.ids.blade.size[0]/2 > touch.pos[0] - self.ids.blade.size[0] and self.ids.blade.pos[1] < touch.pos[1] and self.ids.blade.pos[1] + self.ids.blade.size[1] > touch.pos[1]:
                        blade.did_change_lane = True
                        if blade.lane == "left" or blade.lane == "mid":
                            if blade.lane == "mid":
                                if right_lane[blade_index] == "x":
                                    blade_change_lane = True
                                    blade.lane = "right"
                                    blade.spd -= 1
                                    (right_lane[blade_index], mid_lane[blade_index]) = (mid_lane[blade_index], right_lane[blade_index])
                                else:
                                    if right_lane[blade_index].team == "opponent":
                                        blade_battle = True 
                                        blade.hp -= right_lane[blade_index].atk
                                        right_lane[blade_index].hp -= blade.atk
                            elif blade.lane == "left":
                                if mid_lane[blade_index] == "x":
                                    blade_change_lane = True 
                                    blade.lane = "mid"
                                    blade.spd -= 1
                                    (left_lane[blade_index], mid_lane[blade_index]) = (mid_lane[blade_index], left_lane[blade_index])
                                else:
                                    if mid_lane[blade_index].team == "opponent":
                                        blade_battle = True 
                                        blade.hp -= left_lane[blade_index].atk
                                        left_lane[blade_index].hp -= blade.atk
                            if blade_change_lane == True:
                                self.ids.blade.pos[0] += ((Window.width/5+3*Window.width/5/2)-Window.width/1536) - ((Window.width/5+3*Window.width/5/5)-Window.width/1536)
                    
                    elif self.ids.blade.pos[0] + self.ids.blade.size[0]/2 < touch.pos[0] + self.ids.blade.size[0] and self.ids.blade.pos[0] + self.ids.blade.size[0] > touch.pos[0] + self.ids.blade.size[0] and self.ids.blade.pos[1] < touch.pos[1] and self.ids.blade.pos[1] + self.ids.blade.size[1] > touch.pos[1]:
                        blade.did_change_lane = True
                        if blade.lane == "right" or blade.lane == "mid":
                            if blade.lane == "mid":
                                if left_lane[blade_index] == "x":
                                    blade_change_lane = True
                                    blade.lane = "left"
                                    blade.spd -= 1
                                    (left_lane[blade_index], mid_lane[blade_index]) = (mid_lane[blade_index], left_lane[blade_index])
                                else:
                                    if left_lane[blade_index].team == "opponent":
                                        blade_battle = True 
                                        blade.hp -= left_lane[blade_index].atk
                                        left_lane[blade_index].hp -= blade.atk
                            elif blade.lane == "right":
                                if mid_lane[blade_index] == "x":
                                    blade_change_lane = True
                                    blade.lane = "mid"
                                    blade.spd -= 1
                                    (right_lane[blade_index], mid_lane[blade_index]) = (mid_lane[blade_index], right_lane[blade_index])
                                else:
                                    if mid_lane[blade_index].team == "opponent":
                                        blade_battle = True 
                                        blade.hp -= right_lane[blade_index].atk
                                        right_lane[blade_index].hp -= blade.atk
                            if blade_change_lane == True:
                                self.ids.blade.pos[0] -= ((Window.width/5+3*Window.width/5/2)-Window.width/1536) - ((Window.width/5+3*Window.width/5/5)-Window.width/1536)

            if self.ids.blade.pos[0] > Window.width/2 + self.ids.blade.size[0]:
                # move up right
                if self.ids.blade.pos[0] < touch.pos[0] and self.ids.blade.pos[0] + self.ids.blade.size[0] > touch.pos[0] and self.ids.blade.pos[1] + self.ids.blade.size[1]/2 < touch.pos[1] and self.ids.blade.pos[1] + self.ids.blade.size[1] > touch.pos[1] and self.ids.blade.pos[1] >= Window.height/5 and self.ids.blade.pos[1] < 4*Window.height/5 - Window.height/12.7058823529 and blade.spd > 0 and right_lane[blade_index+1] == "x":
                    self.ids.blade.pos[1] += Window.height/12.7058823529
                    blade.spd -= 1
                    (right_lane[blade_index], right_lane[blade_index+1]) = (right_lane[blade_index+1], right_lane[blade_index])
                    blade_index += 1
                else:
                    if right_lane[blade_index+1] != "x" and right_lane[blade_index+1].team == "opponent" and self.ids.blade.pos[1] + self.ids.blade.size[1]/2 < touch.pos[1] and self.ids.blade.pos[1] + self.ids.blade.size[1] > touch.pos[1]:
                        if blade.did_change_lane == False:
                            blade_battle = True 
                            blade.hp -= right_lane[blade_index+1].atk
                            right_lane[blade_index+1].hp -= blade.atk
                if self.ids.blade.pos[0] < touch.pos[0] and self.ids.blade.pos[0] + self.ids.blade.size[0] > touch.pos[0] and self.ids.blade.pos[1] + self.ids.blade.size[1]/2 < touch.pos[1] and self.ids.blade.pos[1] + self.ids.blade.size[1] > touch.pos[1] and blade_index == 7:
                    if damage_dealt == 1:
                        opponent_life -= 1
                        damage_dealt = 0

                # move down right
                if self.ids.blade.pos[0] < touch.pos[0] and self.ids.blade.pos[0] + self.ids.blade.size[0] > touch.pos[0] and self.ids.blade.pos[1] < touch.pos[1] and self.ids.blade.pos[1] + self.ids.blade.size[1]/2 > touch.pos[1] and self.ids.blade.pos[1] >= Window.height/5 and self.ids.blade.pos[1] > Window.height/5 + Window.height/12.7058823529 and blade.spd > 0 and right_lane[blade_index-1] == "x":
                    self.ids.blade.pos[1] -= Window.height/12.7058823529
                    blade.spd -= 1
                    (right_lane[blade_index], right_lane[blade_index-1]) = (right_lane[blade_index-1], right_lane[blade_index])
                    blade_index -= 1
                else:
                    if right_lane[blade_index-1] != "x" and right_lane[blade_index-1].team == "opponent" and self.ids.blade.pos[1] < touch.pos[1] and self.ids.blade.pos[1] + self.ids.blade.size[1]/2 > touch.pos[1]:
                        if blade.did_change_lane == False:
                            blade_battle = True 
                            blade.hp -= right_lane[blade_index-1].atk
                            right_lane[blade_index-1].hp -= blade.atk

            elif self.ids.blade.pos[0] < Window.width/2 - self.ids.blade.size[0]:
                # move up left
                if self.ids.blade.pos[0] < touch.pos[0] and self.ids.blade.pos[0] + self.ids.blade.size[0] > touch.pos[0] and self.ids.blade.pos[1] + self.ids.blade.size[1]/2 < touch.pos[1] and self.ids.blade.pos[1] + self.ids.blade.size[1] > touch.pos[1] and self.ids.blade.pos[1] >= Window.height/5 and self.ids.blade.pos[1] < 4*Window.height/5 - Window.height/12.7058823529 and blade.spd > 0 and left_lane[blade_index+1] == "x":
                    self.ids.blade.pos[1] += Window.height/12.7058823529
                    blade.spd -= 1
                    (left_lane[blade_index], left_lane[blade_index+1]) = (left_lane[blade_index+1], left_lane[blade_index])
                    blade_index += 1
                else:
                    if left_lane[blade_index+1] != "x" and left_lane[blade_index+1].team == "opponent" and self.ids.blade.pos[1] + self.ids.blade.size[1]/2 < touch.pos[1] and self.ids.blade.pos[1] + self.ids.blade.size[1] > touch.pos[1]:
                        if blade.did_change_lane == False:
                            blade_battle = True 
                            blade.hp -= left_lane[blade_index+1].atk
                            left_lane[blade_index+1].hp -= blade.atk
                if self.ids.blade.pos[0] < touch.pos[0] and self.ids.blade.pos[0] + self.ids.blade.size[0] > touch.pos[0] and self.ids.blade.pos[1] + self.ids.blade.size[1]/2 < touch.pos[1] and self.ids.blade.pos[1] + self.ids.blade.size[1] > touch.pos[1] and blade_index == 7:
                    if damage_dealt == 1:
                        opponent_life -= 1
                        damage_dealt = 0

                # move down left
                if self.ids.blade.pos[0] < touch.pos[0] and self.ids.blade.pos[0] + self.ids.blade.size[0] > touch.pos[0] and self.ids.blade.pos[1] < touch.pos[1] and self.ids.blade.pos[1] + self.ids.blade.size[1]/2 > touch.pos[1] and self.ids.blade.pos[1] >= Window.height/5 and self.ids.blade.pos[1] > Window.height/5 + Window.height/12.7058823529 and blade.spd > 0 and left_lane[blade_index-1] == "x":
                    self.ids.blade.pos[1] -= Window.height/12.7058823529
                    blade.spd -= 1
                    (left_lane[blade_index], left_lane[blade_index-1]) = (left_lane[blade_index-1], left_lane[blade_index])
                    blade_index -= 1
                else:
                    if left_lane[blade_index-1] != "x" and left_lane[blade_index-1].team == "opponent" and self.ids.blade.pos[1] < touch.pos[1] and self.ids.blade.pos[1] + self.ids.blade.size[1]/2 > touch.pos[1]:
                        if blade.did_change_lane == False:
                            blade_battle = True 
                            blade.hp -= left_lane[blade_index-1].atk
                            left_lane[blade_index-1].hp -= blade.atk

            else:
                # move up mid
                if self.ids.blade.pos[0] < touch.pos[0] and self.ids.blade.pos[0] + self.ids.blade.size[0] > touch.pos[0] and self.ids.blade.pos[1] + self.ids.blade.size[1]/2 < touch.pos[1] and self.ids.blade.pos[1] + self.ids.blade.size[1] > touch.pos[1] and self.ids.blade.pos[1] >= Window.height/5 and self.ids.blade.pos[1] < 4*Window.height/5 - Window.height/12.7058823529 and blade.spd > 0 and mid_lane[blade_index+1] == "x":
                    self.ids.blade.pos[1] += Window.height/12.7058823529
                    blade.spd -= 1
                    (mid_lane[blade_index], mid_lane[blade_index+1]) = (mid_lane[blade_index+1], mid_lane[blade_index])
                    blade_index += 1
                else:
                    if mid_lane[blade_index+1] != "x" and mid_lane[blade_index+1].team == "opponent" and self.ids.blade.pos[1] + self.ids.blade.size[1]/2 < touch.pos[1] and self.ids.blade.pos[1] + self.ids.blade.size[1] > touch.pos[1]:
                        if blade.did_change_lane == False:
                            blade_battle = True 
                            blade.hp -= mid_lane[blade_index+1].atk
                            mid_lane[blade_index+1].hp -= blade.atk
                # move down mid
                if self.ids.blade.pos[0] < touch.pos[0] and self.ids.blade.pos[0] + self.ids.blade.size[0] > touch.pos[0] and self.ids.blade.pos[1] < touch.pos[1] and self.ids.blade.pos[1] + self.ids.blade.size[1]/2 > touch.pos[1] and self.ids.blade.pos[1] >= Window.height/5 and self.ids.blade.pos[1] > Window.height/5 + Window.height/12.7058823529 and blade.spd > 0 and mid_lane[blade_index-1] == "x":
                    self.ids.blade.pos[1] -= Window.height/12.7058823529
                    blade.spd -= 1
                    (mid_lane[blade_index], mid_lane[blade_index-1]) = (mid_lane[blade_index-1], mid_lane[blade_index])
                    blade_index -= 1
                else:
                    if mid_lane[blade_index-1] != "x" and mid_lane[blade_index-1].team == "opponent" and self.ids.blade.pos[1] < touch.pos[1] and self.ids.blade.pos[1] + self.ids.blade.size[1]/2 > touch.pos[1]:
                        if blade.did_change_lane == False:
                            blade_battle = True 
                            blade.hp -= mid_lane[blade_index-1].atk
                            mid_lane[blade_index-1].hp -= blade.atk
#########################################################################################################################################
# tank

        if tank.alive == True:
            # summon
            if self.ids.tank.pos[0] < touch.pos[0] and self.ids.tank.pos[0] + self.ids.tank.size[0] > touch.pos[0] and self.ids.tank.pos[1] < touch.pos[1] and self.ids.tank.pos[1] + self.ids.tank.size[1] > touch.pos[1] and self.ids.tank.pos[1] <= Window.height/5 and tank.cd <= 0:
                global tank_battle
                global tank_bool
                tank_bool = True
                global tank_pos
                tank_pos = self.ids.tank.pos[0], self.ids.tank.pos[1]
                global tank_index
                tank_index = 1

            # change lane
            global tank_change_lane
            tank_change_lane = False
            if tank.spd > 0:
                if tank_index == 0 or tank_index == 3 or tank_index == 4 or tank_index == 7:
                    if self.ids.tank.pos[0] < touch.pos[0] - self.ids.tank.size[0] and self.ids.tank.pos[0] + self.ids.tank.size[0]/2 > touch.pos[0] - self.ids.tank.size[0] and self.ids.tank.pos[1] < touch.pos[1] and self.ids.tank.pos[1] + self.ids.tank.size[1] > touch.pos[1]:
                        tank.did_change_lane = True
                        if tank.lane == "left" or tank.lane == "mid":
                            if tank.lane == "mid":
                                if right_lane[tank_index] == "x":
                                    tank_change_lane = True
                                    tank.lane = "right"
                                    tank.spd -= 1
                                    (right_lane[tank_index], mid_lane[tank_index]) = (mid_lane[tank_index], right_lane[tank_index])
                                else:
                                    if right_lane[tank_index].team == "opponent":
                                        tank_battle = True 
                                        tank.hp -= right_lane[tank_index].atk
                                        right_lane[tank_index].hp -= tank.atk
                            elif tank.lane == "left":
                                if mid_lane[tank_index] == "x":
                                    tank_change_lane = True 
                                    tank.lane = "mid"
                                    tank.spd -= 1
                                    (left_lane[tank_index], mid_lane[tank_index]) = (mid_lane[tank_index], left_lane[tank_index])
                                else:
                                    if mid_lane[tank_index].team == "opponent":
                                        tank_battle = True 
                                        tank.hp -= left_lane[tank_index].atk
                                        left_lane[tank_index].hp -= tank.atk
                            if tank_change_lane == True:
                                self.ids.tank.pos[0] += ((Window.width/5+3*Window.width/5/2)-Window.width/1536) - ((Window.width/5+3*Window.width/5/5)-Window.width/1536)
                    
                    elif self.ids.tank.pos[0] + self.ids.tank.size[0]/2 < touch.pos[0] + self.ids.tank.size[0] and self.ids.tank.pos[0] + self.ids.tank.size[0] > touch.pos[0] + self.ids.tank.size[0] and self.ids.tank.pos[1] < touch.pos[1] and self.ids.tank.pos[1] + self.ids.tank.size[1] > touch.pos[1]:
                        tank.did_change_lane = True
                        if tank.lane == "right" or tank.lane == "mid":
                            if tank.lane == "mid":
                                if left_lane[tank_index] == "x":
                                    tank_change_lane = True
                                    tank.spd -= 1
                                    tank.lane = "left"
                                    (left_lane[tank_index], mid_lane[tank_index]) = (mid_lane[tank_index], left_lane[tank_index])
                                else:
                                    if left_lane[tank_index].team == "opponent":
                                        tank_battle = True 
                                        tank.hp -= left_lane[tank_index].atk
                                        left_lane[tank_index].hp -= tank.atk
                            elif tank.lane == "right":
                                if mid_lane[tank_index] == "x":
                                    tank_change_lane = True
                                    tank.lane = "mid"
                                    tank.spd -= 1
                                    (right_lane[tank_index], mid_lane[tank_index]) = (mid_lane[tank_index], right_lane[tank_index])
                                else:
                                    if mid_lane[tank_index].team == "opponent":
                                        tank_battle = True 
                                        tank.hp -= right_lane[tank_index].atk
                                        right_lane[tank_index].hp -= tank.atk
                            if tank_change_lane == True:
                                self.ids.tank.pos[0] -= ((Window.width/5+3*Window.width/5/2)-Window.width/1536) - ((Window.width/5+3*Window.width/5/5)-Window.width/1536)

            if self.ids.tank.pos[0] > Window.width/2 + self.ids.tank.size[0]:
                # move up right
                if self.ids.tank.pos[0] < touch.pos[0] and self.ids.tank.pos[0] + self.ids.tank.size[0] > touch.pos[0] and self.ids.tank.pos[1] + self.ids.tank.size[1]/2 < touch.pos[1] and self.ids.tank.pos[1] + self.ids.tank.size[1] > touch.pos[1] and self.ids.tank.pos[1] >= Window.height/5 and self.ids.tank.pos[1] < 4*Window.height/5 - Window.height/12.7058823529 and tank.spd > 0 and right_lane[tank_index+1] == "x":
                    self.ids.tank.pos[1] += Window.height/12.7058823529
                    tank.spd -= 1
                    (right_lane[tank_index], right_lane[tank_index+1]) = (right_lane[tank_index+1], right_lane[tank_index])
                    tank_index += 1
                else:
                    if right_lane[tank_index+1] != "x" and right_lane[tank_index+1].team == "opponent" and self.ids.tank.pos[1] + self.ids.tank.size[1]/2 < touch.pos[1] and self.ids.tank.pos[1] + self.ids.tank.size[1] > touch.pos[1]:
                        if tank.did_change_lane == False:
                            tank_battle = True 
                            tank.hp -= right_lane[tank_index+1].atk
                            right_lane[tank_index+1].hp -= tank.atk
                if self.ids.tank.pos[0] < touch.pos[0] and self.ids.tank.pos[0] + self.ids.tank.size[0] > touch.pos[0] and self.ids.tank.pos[1] + self.ids.tank.size[1]/2 < touch.pos[1] and self.ids.tank.pos[1] + self.ids.tank.size[1] > touch.pos[1] and tank_index == 7:
                    if damage_dealt == 1:
                        opponent_life -= 1
                        damage_dealt = 0

                # move down right
                if self.ids.tank.pos[0] < touch.pos[0] and self.ids.tank.pos[0] + self.ids.tank.size[0] > touch.pos[0] and self.ids.tank.pos[1] < touch.pos[1] and self.ids.tank.pos[1] + self.ids.tank.size[1]/2 > touch.pos[1] and self.ids.tank.pos[1] >= Window.height/5 and self.ids.tank.pos[1] > Window.height/5 + Window.height/12.7058823529 and tank.spd > 0 and right_lane[tank_index-1] == "x":
                    self.ids.tank.pos[1] -= Window.height/12.7058823529
                    tank.spd -= 1
                    (right_lane[tank_index], right_lane[tank_index-1]) = (right_lane[tank_index-1], right_lane[tank_index])
                    tank_index -= 1
                else:
                    if right_lane[tank_index-1] != "x" and right_lane[tank_index-1].team == "opponent" and self.ids.tank.pos[1] < touch.pos[1] and self.ids.tank.pos[1] + self.ids.tank.size[1]/2 > touch.pos[1]:
                        if tank.did_change_lane == False:
                            tank_battle = True 
                            tank.hp -= right_lane[tank_index-1].atk
                            right_lane[tank_index-1].hp -= tank.atk

            elif self.ids.tank.pos[0] < Window.width/2 - self.ids.tank.size[0]:
                # move up left
                if self.ids.tank.pos[0] < touch.pos[0] and self.ids.tank.pos[0] + self.ids.tank.size[0] > touch.pos[0] and self.ids.tank.pos[1] + self.ids.tank.size[1]/2 < touch.pos[1] and self.ids.tank.pos[1] + self.ids.tank.size[1] > touch.pos[1] and self.ids.tank.pos[1] >= Window.height/5 and self.ids.tank.pos[1] < 4*Window.height/5 - Window.height/12.7058823529 and tank.spd > 0 and left_lane[tank_index+1] == "x":
                    self.ids.tank.pos[1] += Window.height/12.7058823529
                    tank.spd -= 1
                    (left_lane[tank_index], left_lane[tank_index+1]) = (left_lane[tank_index+1], left_lane[tank_index])
                    tank_index += 1
                else:
                    if left_lane[tank_index+1] != "x" and left_lane[tank_index+1].team == "opponent" and self.ids.tank.pos[1] + self.ids.tank.size[1]/2 < touch.pos[1] and self.ids.tank.pos[1] + self.ids.tank.size[1] > touch.pos[1]:
                        if tank.did_change_lane == False:
                            tank_battle = True 
                            tank.hp -= left_lane[tank_index+1].atk
                            left_lane[tank_index+1].hp -= tank.atk
                if self.ids.tank.pos[0] < touch.pos[0] and self.ids.tank.pos[0] + self.ids.tank.size[0] > touch.pos[0] and self.ids.tank.pos[1] + self.ids.tank.size[1]/2 < touch.pos[1] and self.ids.tank.pos[1] + self.ids.tank.size[1] > touch.pos[1] and tank_index == 7:
                    if damage_dealt == 1:
                        opponent_life -= 1
                        damage_dealt = 0

                # move down left
                if self.ids.tank.pos[0] < touch.pos[0] and self.ids.tank.pos[0] + self.ids.tank.size[0] > touch.pos[0] and self.ids.tank.pos[1] < touch.pos[1] and self.ids.tank.pos[1] + self.ids.tank.size[1]/2 > touch.pos[1] and self.ids.tank.pos[1] >= Window.height/5 and self.ids.tank.pos[1] > Window.height/5 + Window.height/12.7058823529 and tank.spd > 0 and left_lane[tank_index-1] == "x":
                    self.ids.tank.pos[1] -= Window.height/12.7058823529
                    tank.spd -= 1
                    (left_lane[tank_index], left_lane[tank_index-1]) = (left_lane[tank_index-1], left_lane[tank_index])
                    tank_index -= 1
                else:
                    if left_lane[tank_index-1] != "x" and left_lane[tank_index-1].team == "opponent" and self.ids.tank.pos[1] < touch.pos[1] and self.ids.tank.pos[1] + self.ids.tank.size[1]/2 > touch.pos[1]:
                        if tank.did_change_lane == False:
                            tank_battle = True 
                            tank.hp -= left_lane[tank_index-1].atk
                            left_lane[tank_index-1].hp -= tank.atk

            else:
                # move up mid
                if self.ids.tank.pos[0] < touch.pos[0] and self.ids.tank.pos[0] + self.ids.tank.size[0] > touch.pos[0] and self.ids.tank.pos[1] + self.ids.tank.size[1]/2 < touch.pos[1] and self.ids.tank.pos[1] + self.ids.tank.size[1] > touch.pos[1] and self.ids.tank.pos[1] >= Window.height/5 and self.ids.tank.pos[1] < 4*Window.height/5 - Window.height/12.7058823529 and tank.spd > 0 and mid_lane[tank_index+1] == "x":
                    self.ids.tank.pos[1] += Window.height/12.7058823529
                    tank.spd -= 1
                    (mid_lane[tank_index], mid_lane[tank_index+1]) = (mid_lane[tank_index+1], mid_lane[tank_index])
                    tank_index += 1
                else:
                    if mid_lane[tank_index+1] != "x" and mid_lane[tank_index+1].team == "opponent" and self.ids.tank.pos[1] + self.ids.tank.size[1]/2 < touch.pos[1] and self.ids.tank.pos[1] + self.ids.tank.size[1] > touch.pos[1]:
                        if tank.did_change_lane == False:
                            tank_battle = True 
                            tank.hp -= mid_lane[tank_index+1].atk
                            mid_lane[tank_index+1].hp -= tank.atk
                # move down mid
                if self.ids.tank.pos[0] < touch.pos[0] and self.ids.tank.pos[0] + self.ids.tank.size[0] > touch.pos[0] and self.ids.tank.pos[1] < touch.pos[1] and self.ids.tank.pos[1] + self.ids.tank.size[1]/2 > touch.pos[1] and self.ids.tank.pos[1] >= Window.height/5 and self.ids.tank.pos[1] > Window.height/5 + Window.height/12.7058823529 and tank.spd > 0 and mid_lane[tank_index-1] == "x":
                    self.ids.tank.pos[1] -= Window.height/12.7058823529
                    tank.spd -= 1
                    (mid_lane[tank_index], mid_lane[tank_index-1]) = (mid_lane[tank_index-1], mid_lane[tank_index])
                    tank_index -= 1
                else:
                    if mid_lane[tank_index-1] != "x" and mid_lane[tank_index-1].team == "opponent" and self.ids.tank.pos[1] < touch.pos[1] and self.ids.tank.pos[1] + self.ids.tank.size[1]/2 > touch.pos[1]:
                        if tank.did_change_lane == False:
                            tank_battle = True 
                            tank.hp -= mid_lane[tank_index-1].atk
                            mid_lane[tank_index-1].hp -= tank.atk
#########################################################################################################################################
# bomb

        if bomb.alive == True:
            # summon
            if self.ids.bomb.pos[0] < touch.pos[0] and self.ids.bomb.pos[0] + self.ids.bomb.size[0] > touch.pos[0] and self.ids.bomb.pos[1] < touch.pos[1] and self.ids.bomb.pos[1] + self.ids.bomb.size[1] > touch.pos[1] and self.ids.bomb.pos[1] <= Window.height/5 and bomb.cd <= 0:
                global bomb_batle
                global bomb_bool
                bomb_bool = True
                global bomb_pos
                bomb_pos = self.ids.bomb.pos[0], self.ids.bomb.pos[1]
                global bomb_index
                bomb_index = 1

            # change lane
            global bomb_change_lane
            bomb_change_lane = False
            if bomb.spd > 0:
                if bomb_index == 0 or bomb_index == 3 or bomb_index == 4 or bomb_index == 7:
                    if self.ids.bomb.pos[0] < touch.pos[0] - self.ids.bomb.size[0] and self.ids.bomb.pos[0] + self.ids.bomb.size[0]/2 > touch.pos[0] - self.ids.bomb.size[0] and self.ids.bomb.pos[1] < touch.pos[1] and self.ids.bomb.pos[1] + self.ids.bomb.size[1] > touch.pos[1]:
                        bomb.did_change_lane = True
                        if bomb.lane == "left" or bomb.lane == "mid":
                            if bomb.lane == "mid":
                                if right_lane[bomb_index] == "x":
                                    bomb_change_lane = True
                                    bomb.lane = "right"
                                    bomb.spd -= 1
                                    (right_lane[bomb_index], mid_lane[bomb_index]) = (mid_lane[bomb_index], right_lane[bomb_index])
                                else:
                                    if right_lane[bomb_index].team == "opponent":
                                        bomb_batle = True 
                                        bomb.hp -= right_lane[bomb_index].atk
                                        right_lane[bomb_index].hp -= bomb.atk
                            elif bomb.lane == "left":
                                if mid_lane[bomb_index] == "x":
                                    bomb_change_lane = True 
                                    bomb.lane = "mid"
                                    bomb.spd -= 1
                                    (left_lane[bomb_index], mid_lane[bomb_index]) = (mid_lane[bomb_index], left_lane[bomb_index])
                                else:
                                    if mid_lane[bomb_index].team == "opponent":
                                        bomb_batle = True 
                                        bomb.hp -= left_lane[bomb_index].atk
                                        left_lane[bomb_index].hp -= bomb.atk
                            if bomb_change_lane == True:
                                self.ids.bomb.pos[0] += ((Window.width/5+3*Window.width/5/2)-Window.width/1536) - ((Window.width/5+3*Window.width/5/5)-Window.width/1536)
                    
                    elif self.ids.bomb.pos[0] + self.ids.bomb.size[0]/2 < touch.pos[0] + self.ids.bomb.size[0] and self.ids.bomb.pos[0] + self.ids.bomb.size[0] > touch.pos[0] + self.ids.bomb.size[0] and self.ids.bomb.pos[1] < touch.pos[1] and self.ids.bomb.pos[1] + self.ids.bomb.size[1] > touch.pos[1]:
                        bomb.did_change_lane = True
                        if bomb.lane == "right" or bomb.lane == "mid":
                            if bomb.lane == "mid":
                                if left_lane[bomb_index] == "x":
                                    bomb_change_lane = True
                                    bomb.lane = "left"
                                    bomb.spd -= 1
                                    (left_lane[bomb_index], mid_lane[bomb_index]) = (mid_lane[bomb_index], left_lane[bomb_index])
                                else:
                                    if left_lane[bomb_index].team == "opponent":
                                        bomb_batle = True 
                                        bomb.hp -= left_lane[bomb_index].atk
                                        left_lane[bomb_index].hp -= bomb.atk
                            elif bomb.lane == "right":
                                if mid_lane[bomb_index] == "x":
                                    bomb_change_lane = True
                                    bomb.lane = "mid"
                                    bomb.spd -= 1
                                    (right_lane[bomb_index], mid_lane[bomb_index]) = (mid_lane[bomb_index], right_lane[bomb_index])
                                else:
                                    if mid_lane[bomb_index].team == "opponent":
                                        bomb_batle = True 
                                        bomb.hp -= right_lane[bomb_index].atk
                                        right_lane[bomb_index].hp -= bomb.atk
                            if bomb_change_lane == True:
                                self.ids.bomb.pos[0] -= ((Window.width/5+3*Window.width/5/2)-Window.width/1536) - ((Window.width/5+3*Window.width/5/5)-Window.width/1536)

            if self.ids.bomb.pos[0] > Window.width/2 + self.ids.bomb.size[0]:
                # move up right
                if self.ids.bomb.pos[0] < touch.pos[0] and self.ids.bomb.pos[0] + self.ids.bomb.size[0] > touch.pos[0] and self.ids.bomb.pos[1] + self.ids.bomb.size[1]/2 < touch.pos[1] and self.ids.bomb.pos[1] + self.ids.bomb.size[1] > touch.pos[1] and self.ids.bomb.pos[1] >= Window.height/5 and self.ids.bomb.pos[1] < 4*Window.height/5 - Window.height/12.7058823529 and bomb.spd > 0 and right_lane[bomb_index+1] == "x":
                    self.ids.bomb.pos[1] += Window.height/12.7058823529
                    bomb.spd -= 1
                    (right_lane[bomb_index], right_lane[bomb_index+1]) = (right_lane[bomb_index+1], right_lane[bomb_index])
                    bomb_index += 1
                else:
                    if right_lane[bomb_index+1] != "x" and right_lane[bomb_index+1].team == "opponent" and self.ids.bomb.pos[1] + self.ids.bomb.size[1]/2 < touch.pos[1] and self.ids.bomb.pos[1] + self.ids.bomb.size[1] > touch.pos[1]:
                        if bomb.did_change_lane == False:
                            bomb_batle = True 
                            bomb.hp -= right_lane[bomb_index+1].atk
                            right_lane[bomb_index+1].hp -= bomb.atk
                if self.ids.bomb.pos[0] < touch.pos[0] and self.ids.bomb.pos[0] + self.ids.bomb.size[0] > touch.pos[0] and self.ids.bomb.pos[1] + self.ids.bomb.size[1]/2 < touch.pos[1] and self.ids.bomb.pos[1] + self.ids.bomb.size[1] > touch.pos[1] and bomb_index == 7:
                    if damage_dealt == 1:
                        opponent_life -= 1
                        damage_dealt = 0

                # move down right
                if self.ids.bomb.pos[0] < touch.pos[0] and self.ids.bomb.pos[0] + self.ids.bomb.size[0] > touch.pos[0] and self.ids.bomb.pos[1] < touch.pos[1] and self.ids.bomb.pos[1] + self.ids.bomb.size[1]/2 > touch.pos[1] and self.ids.bomb.pos[1] >= Window.height/5 and self.ids.bomb.pos[1] > Window.height/5 + Window.height/12.7058823529 and bomb.spd > 0 and right_lane[bomb_index-1] == "x":
                    self.ids.bomb.pos[1] -= Window.height/12.7058823529
                    bomb.spd -= 1
                    (right_lane[bomb_index], right_lane[bomb_index-1]) = (right_lane[bomb_index-1], right_lane[bomb_index])
                    bomb_index -= 1
                else:
                    if right_lane[bomb_index-1] != "x" and right_lane[bomb_index-1].team == "opponent" and self.ids.bomb.pos[1] < touch.pos[1] and self.ids.bomb.pos[1] + self.ids.bomb.size[1]/2 > touch.pos[1]:
                        if bomb.did_change_lane == False:
                            bomb_batle = True 
                            bomb.hp -= right_lane[bomb_index-1].atk
                            right_lane[bomb_index-1].hp -= bomb.atk

            elif self.ids.bomb.pos[0] < Window.width/2 - self.ids.bomb.size[0]:
                # move up left
                if self.ids.bomb.pos[0] < touch.pos[0] and self.ids.bomb.pos[0] + self.ids.bomb.size[0] > touch.pos[0] and self.ids.bomb.pos[1] + self.ids.bomb.size[1]/2 < touch.pos[1] and self.ids.bomb.pos[1] + self.ids.bomb.size[1] > touch.pos[1] and self.ids.bomb.pos[1] >= Window.height/5 and self.ids.bomb.pos[1] < 4*Window.height/5 - Window.height/12.7058823529 and bomb.spd > 0 and left_lane[bomb_index+1] == "x":
                    self.ids.bomb.pos[1] += Window.height/12.7058823529
                    bomb.spd -= 1
                    (left_lane[bomb_index], left_lane[bomb_index+1]) = (left_lane[bomb_index+1], left_lane[bomb_index])
                    bomb_index += 1
                else:
                    if left_lane[bomb_index+1] != "x" and left_lane[bomb_index+1].team == "opponent" and self.ids.bomb.pos[1] + self.ids.bomb.size[1]/2 < touch.pos[1] and self.ids.bomb.pos[1] + self.ids.bomb.size[1] > touch.pos[1]:
                        if bomb.did_change_lane == False:
                            bomb_batle = True 
                            bomb.hp -= left_lane[bomb_index+1].atk
                            left_lane[bomb_index+1].hp -= bomb.atk
                if self.ids.bomb.pos[0] < touch.pos[0] and self.ids.bomb.pos[0] + self.ids.bomb.size[0] > touch.pos[0] and self.ids.bomb.pos[1] + self.ids.bomb.size[1]/2 < touch.pos[1] and self.ids.bomb.pos[1] + self.ids.bomb.size[1] > touch.pos[1] and bomb_index == 7:
                    if damage_dealt == 1:
                        opponent_life -= 1
                        damage_dealt = 0

                # move down left
                if self.ids.bomb.pos[0] < touch.pos[0] and self.ids.bomb.pos[0] + self.ids.bomb.size[0] > touch.pos[0] and self.ids.bomb.pos[1] < touch.pos[1] and self.ids.bomb.pos[1] + self.ids.bomb.size[1]/2 > touch.pos[1] and self.ids.bomb.pos[1] >= Window.height/5 and self.ids.bomb.pos[1] > Window.height/5 + Window.height/12.7058823529 and bomb.spd > 0 and left_lane[bomb_index-1] == "x":
                    self.ids.bomb.pos[1] -= Window.height/12.7058823529
                    bomb.spd -= 1
                    (left_lane[bomb_index], left_lane[bomb_index-1]) = (left_lane[bomb_index-1], left_lane[bomb_index])
                    bomb_index -= 1
                else:
                    if left_lane[bomb_index-1] != "x" and left_lane[bomb_index-1].team == "opponent" and self.ids.bomb.pos[1] < touch.pos[1] and self.ids.bomb.pos[1] + self.ids.bomb.size[1]/2 > touch.pos[1]:
                        if bomb.did_change_lane == False:
                            bomb_batle = True 
                            bomb.hp -= left_lane[bomb_index-1].atk
                            left_lane[bomb_index-1].hp -= bomb.atk

            else:
                # move up mid
                if self.ids.bomb.pos[0] < touch.pos[0] and self.ids.bomb.pos[0] + self.ids.bomb.size[0] > touch.pos[0] and self.ids.bomb.pos[1] + self.ids.bomb.size[1]/2 < touch.pos[1] and self.ids.bomb.pos[1] + self.ids.bomb.size[1] > touch.pos[1] and self.ids.bomb.pos[1] >= Window.height/5 and self.ids.bomb.pos[1] < 4*Window.height/5 - Window.height/12.7058823529 and bomb.spd > 0 and mid_lane[bomb_index+1] == "x":
                    self.ids.bomb.pos[1] += Window.height/12.7058823529
                    bomb.spd -= 1
                    (mid_lane[bomb_index], mid_lane[bomb_index+1]) = (mid_lane[bomb_index+1], mid_lane[bomb_index])
                    bomb_index += 1
                else:
                    if mid_lane[bomb_index+1] != "x" and mid_lane[bomb_index+1].team == "opponent" and self.ids.bomb.pos[1] + self.ids.bomb.size[1]/2 < touch.pos[1] and self.ids.bomb.pos[1] + self.ids.bomb.size[1] > touch.pos[1]:
                        if bomb.did_change_lane == False:
                            bomb_batle = True 
                            bomb.hp -= mid_lane[bomb_index+1].atk
                            mid_lane[bomb_index+1].hp -= bomb.atk
                # move down mid
                if self.ids.bomb.pos[0] < touch.pos[0] and self.ids.bomb.pos[0] + self.ids.bomb.size[0] > touch.pos[0] and self.ids.bomb.pos[1] < touch.pos[1] and self.ids.bomb.pos[1] + self.ids.bomb.size[1]/2 > touch.pos[1] and self.ids.bomb.pos[1] >= Window.height/5 and self.ids.bomb.pos[1] > Window.height/5 + Window.height/12.7058823529 and bomb.spd > 0 and mid_lane[bomb_index-1] == "x":
                    self.ids.bomb.pos[1] -= Window.height/12.7058823529
                    bomb.spd -= 1
                    (mid_lane[bomb_index], mid_lane[bomb_index-1]) = (mid_lane[bomb_index-1], mid_lane[bomb_index])
                    bomb_index -= 1
                else:
                    if mid_lane[bomb_index-1] != "x" and mid_lane[bomb_index-1].team == "opponent" and self.ids.bomb.pos[1] < touch.pos[1] and self.ids.bomb.pos[1] + self.ids.bomb.size[1]/2 > touch.pos[1]:
                        if bomb.did_change_lane == False:
                            bomb_batle = True 
                            bomb.hp -= mid_lane[bomb_index-1].atk
                            mid_lane[bomb_index-1].hp -= bomb.atk
#########################################################################################################################################
# jolt

        if jolt.alive == True:
            # summon
            if self.ids.jolt.pos[0] < touch.pos[0] and self.ids.jolt.pos[0] + self.ids.jolt.size[0] > touch.pos[0] and self.ids.jolt.pos[1] < touch.pos[1] and self.ids.jolt.pos[1] + self.ids.jolt.size[1] > touch.pos[1] and self.ids.jolt.pos[1] <= Window.height/5 and jolt.cd <= 0:
                global jolt_battle
                global jolt_bool
                jolt_bool = True
                global jolt_pos
                jolt_pos = self.ids.jolt.pos[0], self.ids.jolt.pos[1]
                global jolt_index
                jolt_index = 1

            # change lane
            global jolt_change_lane
            jolt_change_lane = False
            if jolt.spd > 0:
                if jolt_index == 0 or jolt_index == 3 or jolt_index == 4 or jolt_index == 7:
                    if self.ids.jolt.pos[0] < touch.pos[0] - self.ids.jolt.size[0] and self.ids.jolt.pos[0] + self.ids.jolt.size[0]/2 > touch.pos[0] - self.ids.jolt.size[0] and self.ids.jolt.pos[1] < touch.pos[1] and self.ids.jolt.pos[1] + self.ids.jolt.size[1] > touch.pos[1]:
                        jolt.did_change_lane = True
                        if jolt.lane == "left" or jolt.lane == "mid":
                            if jolt.lane == "mid":
                                if right_lane[jolt_index] == "x":
                                    jolt_change_lane = True
                                    jolt.lane = "right"
                                    jolt.spd -= 1
                                    (right_lane[jolt_index], mid_lane[jolt_index]) = (mid_lane[jolt_index], right_lane[jolt_index])
                                else:
                                    if right_lane[jolt_index].team == "opponent":
                                        jolt_battle = True 
                                        jolt.hp -= right_lane[jolt_index].atk
                                        right_lane[jolt_index].hp -= jolt.atk
                            elif jolt.lane == "left":
                                if mid_lane[jolt_index] == "x":
                                    jolt_change_lane = True 
                                    jolt.lane = "mid"
                                    jolt.spd -= 1
                                    (left_lane[jolt_index], mid_lane[jolt_index]) = (mid_lane[jolt_index], left_lane[jolt_index])
                                else:
                                    if mid_lane[jolt_index].team == "opponent":
                                        jolt_battle = True 
                                        jolt.hp -= left_lane[jolt_index].atk
                                        left_lane[jolt_index].hp -= jolt.atk
                            if jolt_change_lane == True:
                                self.ids.jolt.pos[0] += ((Window.width/5+3*Window.width/5/2)-Window.width/1536) - ((Window.width/5+3*Window.width/5/5)-Window.width/1536)
                    
                    elif self.ids.jolt.pos[0] + self.ids.jolt.size[0]/2 < touch.pos[0] + self.ids.jolt.size[0] and self.ids.jolt.pos[0] + self.ids.jolt.size[0] > touch.pos[0] + self.ids.jolt.size[0] and self.ids.jolt.pos[1] < touch.pos[1] and self.ids.jolt.pos[1] + self.ids.jolt.size[1] > touch.pos[1]:
                        jolt.did_change_lane = True
                        if jolt.lane == "right" or jolt.lane == "mid":
                            if jolt.lane == "mid":
                                if left_lane[jolt_index] == "x":
                                    jolt_change_lane = True
                                    jolt.lane = "left"
                                    jolt.spd -= 1
                                    (left_lane[jolt_index], mid_lane[jolt_index]) = (mid_lane[jolt_index], left_lane[jolt_index])
                                else:
                                    if left_lane[jolt_index].team == "opponent":
                                        jolt_battle = True 
                                        jolt.hp -= left_lane[jolt_index].atk
                                        left_lane[jolt_index].hp -= jolt.atk
                            elif jolt.lane == "right":
                                if mid_lane[jolt_index] == "x":
                                    jolt_change_lane = True
                                    jolt.lane = "mid"
                                    jolt.spd -= 1
                                    (right_lane[jolt_index], mid_lane[jolt_index]) = (mid_lane[jolt_index], right_lane[jolt_index])
                                else:
                                    if mid_lane[jolt_index].team == "opponent":
                                        jolt_battle = True 
                                        jolt.hp -= right_lane[jolt_index].atk
                                        right_lane[jolt_index].hp -= jolt.atk
                            if jolt_change_lane == True:
                                self.ids.jolt.pos[0] -= ((Window.width/5+3*Window.width/5/2)-Window.width/1536) - ((Window.width/5+3*Window.width/5/5)-Window.width/1536)

            if self.ids.jolt.pos[0] > Window.width/2 + self.ids.jolt.size[0]:
                # move up right
                if self.ids.jolt.pos[0] < touch.pos[0] and self.ids.jolt.pos[0] + self.ids.jolt.size[0] > touch.pos[0] and self.ids.jolt.pos[1] + self.ids.jolt.size[1]/2 < touch.pos[1] and self.ids.jolt.pos[1] + self.ids.jolt.size[1] > touch.pos[1] and self.ids.jolt.pos[1] >= Window.height/5 and self.ids.jolt.pos[1] < 4*Window.height/5 - Window.height/12.7058823529 and jolt.spd > 0 and right_lane[jolt_index+1] == "x":
                    self.ids.jolt.pos[1] += Window.height/12.7058823529
                    jolt.spd -= 1
                    (right_lane[jolt_index], right_lane[jolt_index+1]) = (right_lane[jolt_index+1], right_lane[jolt_index])
                    jolt_index += 1
                else:
                    if right_lane[jolt_index+1] != "x" and right_lane[jolt_index+1].team == "opponent" and self.ids.jolt.pos[1] + self.ids.jolt.size[1]/2 < touch.pos[1] and self.ids.jolt.pos[1] + self.ids.jolt.size[1] > touch.pos[1]:
                        if jolt.did_change_lane == False:
                            jolt_battle = True 
                            jolt.hp -= right_lane[jolt_index+1].atk
                            right_lane[jolt_index+1].hp -= jolt.atk
                if self.ids.jolt.pos[0] < touch.pos[0] and self.ids.jolt.pos[0] + self.ids.jolt.size[0] > touch.pos[0] and self.ids.jolt.pos[1] + self.ids.jolt.size[1]/2 < touch.pos[1] and self.ids.jolt.pos[1] + self.ids.jolt.size[1] > touch.pos[1] and jolt_index == 7:
                    if damage_dealt == 1:
                        opponent_life -= 1
                        damage_dealt = 0

                # move down right
                if self.ids.jolt.pos[0] < touch.pos[0] and self.ids.jolt.pos[0] + self.ids.jolt.size[0] > touch.pos[0] and self.ids.jolt.pos[1] < touch.pos[1] and self.ids.jolt.pos[1] + self.ids.jolt.size[1]/2 > touch.pos[1] and self.ids.jolt.pos[1] >= Window.height/5 and self.ids.jolt.pos[1] > Window.height/5 + Window.height/12.7058823529 and jolt.spd > 0 and right_lane[jolt_index-1] == "x":
                    self.ids.jolt.pos[1] -= Window.height/12.7058823529
                    jolt.spd -= 1
                    (right_lane[jolt_index], right_lane[jolt_index-1]) = (right_lane[jolt_index-1], right_lane[jolt_index])
                    jolt_index -= 1
                else:
                    if right_lane[jolt_index-1] != "x" and right_lane[jolt_index-1].team == "opponent" and self.ids.jolt.pos[1] < touch.pos[1] and self.ids.jolt.pos[1] + self.ids.jolt.size[1]/2 > touch.pos[1]:
                        if jolt.did_change_lane == False:
                            jolt_battle = True 
                            jolt.hp -= right_lane[jolt_index-1].atk
                            right_lane[jolt_index-1].hp -= jolt.atk

            elif self.ids.jolt.pos[0] < Window.width/2 - self.ids.jolt.size[0]:
                # move up left
                if self.ids.jolt.pos[0] < touch.pos[0] and self.ids.jolt.pos[0] + self.ids.jolt.size[0] > touch.pos[0] and self.ids.jolt.pos[1] + self.ids.jolt.size[1]/2 < touch.pos[1] and self.ids.jolt.pos[1] + self.ids.jolt.size[1] > touch.pos[1] and self.ids.jolt.pos[1] >= Window.height/5 and self.ids.jolt.pos[1] < 4*Window.height/5 - Window.height/12.7058823529 and jolt.spd > 0 and left_lane[jolt_index+1] == "x":
                    self.ids.jolt.pos[1] += Window.height/12.7058823529
                    jolt.spd -= 1
                    (left_lane[jolt_index], left_lane[jolt_index+1]) = (left_lane[jolt_index+1], left_lane[jolt_index])
                    jolt_index += 1
                else:
                    if left_lane[jolt_index+1] != "x" and left_lane[jolt_index+1].team == "opponent" and self.ids.jolt.pos[1] + self.ids.jolt.size[1]/2 < touch.pos[1] and self.ids.jolt.pos[1] + self.ids.jolt.size[1] > touch.pos[1]:
                        if jolt.did_change_lane == False:
                            jolt_battle = True 
                            jolt.hp -= left_lane[jolt_index+1].atk
                            left_lane[jolt_index+1].hp -= jolt.atk
                if self.ids.jolt.pos[0] < touch.pos[0] and self.ids.jolt.pos[0] + self.ids.jolt.size[0] > touch.pos[0] and self.ids.jolt.pos[1] + self.ids.jolt.size[1]/2 < touch.pos[1] and self.ids.jolt.pos[1] + self.ids.jolt.size[1] > touch.pos[1] and jolt_index == 7:
                    if damage_dealt == 1:
                        opponent_life -= 1
                        damage_dealt = 0

                # move down left
                if self.ids.jolt.pos[0] < touch.pos[0] and self.ids.jolt.pos[0] + self.ids.jolt.size[0] > touch.pos[0] and self.ids.jolt.pos[1] < touch.pos[1] and self.ids.jolt.pos[1] + self.ids.jolt.size[1]/2 > touch.pos[1] and self.ids.jolt.pos[1] >= Window.height/5 and self.ids.jolt.pos[1] > Window.height/5 + Window.height/12.7058823529 and jolt.spd > 0 and left_lane[jolt_index-1] == "x":
                    self.ids.jolt.pos[1] -= Window.height/12.7058823529
                    jolt.spd -= 1
                    (left_lane[jolt_index], left_lane[jolt_index-1]) = (left_lane[jolt_index-1], left_lane[jolt_index])
                    jolt_index -= 1
                else:
                    if left_lane[jolt_index-1] != "x" and left_lane[jolt_index-1].team == "opponent" and self.ids.jolt.pos[1] < touch.pos[1] and self.ids.jolt.pos[1] + self.ids.jolt.size[1]/2 > touch.pos[1]:
                        if jolt.did_change_lane == False:
                            jolt_battle = True 
                            jolt.hp -= left_lane[jolt_index-1].atk
                            left_lane[jolt_index-1].hp -= jolt.atk

            else:
                # move up mid
                if self.ids.jolt.pos[0] < touch.pos[0] and self.ids.jolt.pos[0] + self.ids.jolt.size[0] > touch.pos[0] and self.ids.jolt.pos[1] + self.ids.jolt.size[1]/2 < touch.pos[1] and self.ids.jolt.pos[1] + self.ids.jolt.size[1] > touch.pos[1] and self.ids.jolt.pos[1] >= Window.height/5 and self.ids.jolt.pos[1] < 4*Window.height/5 - Window.height/12.7058823529 and jolt.spd > 0 and mid_lane[jolt_index+1] == "x":
                    self.ids.jolt.pos[1] += Window.height/12.7058823529
                    jolt.spd -= 1
                    (mid_lane[jolt_index], mid_lane[jolt_index+1]) = (mid_lane[jolt_index+1], mid_lane[jolt_index])
                    jolt_index += 1
                else:
                    if mid_lane[jolt_index+1] != "x" and mid_lane[jolt_index+1].team == "opponent" and self.ids.jolt.pos[1] + self.ids.jolt.size[1]/2 < touch.pos[1] and self.ids.jolt.pos[1] + self.ids.jolt.size[1] > touch.pos[1]:
                        if jolt.did_change_lane == False:
                            jolt_battle = True 
                            jolt.hp -= mid_lane[jolt_index+1].atk
                            mid_lane[jolt_index+1].hp -= jolt.atk
                # move down mid
                if self.ids.jolt.pos[0] < touch.pos[0] and self.ids.jolt.pos[0] + self.ids.jolt.size[0] > touch.pos[0] and self.ids.jolt.pos[1] < touch.pos[1] and self.ids.jolt.pos[1] + self.ids.jolt.size[1]/2 > touch.pos[1] and self.ids.jolt.pos[1] >= Window.height/5 and self.ids.jolt.pos[1] > Window.height/5 + Window.height/12.7058823529 and jolt.spd > 0 and mid_lane[jolt_index-1] == "x":
                    self.ids.jolt.pos[1] -= Window.height/12.7058823529
                    jolt.spd -= 1
                    (mid_lane[jolt_index], mid_lane[jolt_index-1]) = (mid_lane[jolt_index-1], mid_lane[jolt_index])
                    jolt_index -= 1
                else:
                    if mid_lane[jolt_index-1] != "x" and mid_lane[jolt_index-1].team == "opponent" and self.ids.jolt.pos[1] < touch.pos[1] and self.ids.jolt.pos[1] + self.ids.jolt.size[1]/2 > touch.pos[1]:
                        if jolt.did_change_lane == False:
                            jolt_battle = True 
                            jolt.hp -= mid_lane[jolt_index-1].atk
                            mid_lane[jolt_index-1].hp -= jolt.atk




    def on_touch_move(self, touch):
#########################################################################################################################################
# swordman
        if swordman_bool == True:
            self.ids.swordman.pos = touch.spos[0]*Window.width-self.ids.swordman.size[0]/2,touch.spos[1]*Window.height-self.ids.swordman.size[1]/2
#########################################################################################################################################
# ion
        if ion_bool == True:
            self.ids.ion.pos = touch.spos[0]*Window.width-self.ids.ion.size[0]/2,touch.spos[1]*Window.height-self.ids.ion.size[1]/2
#########################################################################################################################################
# apex
        if apex_bool == True:
            self.ids.apex.pos = touch.spos[0]*Window.width-self.ids.apex.size[0]/2,touch.spos[1]*Window.height-self.ids.apex.size[1]/2
#########################################################################################################################################
# blade
        if blade_bool == True:
            self.ids.blade.pos = touch.spos[0]*Window.width-self.ids.blade.size[0]/2,touch.spos[1]*Window.height-self.ids.blade.size[1]/2
#########################################################################################################################################
# tank
        if tank_bool == True:
            self.ids.tank.pos = touch.spos[0]*Window.width-self.ids.tank.size[0]/2,touch.spos[1]*Window.height-self.ids.tank.size[1]/2
#########################################################################################################################################
# bomb
        if bomb_bool == True:
            self.ids.bomb.pos = touch.spos[0]*Window.width-self.ids.bomb.size[0]/2,touch.spos[1]*Window.height-self.ids.bomb.size[1]/2
#########################################################################################################################################
# jolt
        if jolt_bool == True:
            self.ids.jolt.pos = touch.spos[0]*Window.width-self.ids.jolt.size[0]/2,touch.spos[1]*Window.height-self.ids.jolt.size[1]/2




    def on_touch_up(self, touch):

#########################################################################################################################################
# hand
        touch_lane = ""
        touch_index = 999

        if touch.pos[1] > (Window.height/5+Window.height/45)+Window.height/16 + Window.height/12.7058823529*-1 and touch.pos[1] < (Window.height/5+Window.height/45)+Window.height/16 + Window.height/27 + Window.height/12.7058823529*-1:
            touch_index = 0
        if touch.pos[1] > (Window.height/5+Window.height/45)+Window.height/16 and touch.pos[1] < (Window.height/5+Window.height/45)+Window.height/16 + Window.height/27:
            touch_index = 1
        if touch.pos[1] > (Window.height/5+Window.height/45)+Window.height/16 + Window.height/12.7058823529 and touch.pos[1] < (Window.height/5+Window.height/45)+Window.height/16 + Window.height/27 + Window.height/12.7058823529:
            touch_index = 2
        if touch.pos[1] > (Window.height/5+Window.height/45)+Window.height/16 + Window.height/12.7058823529*2 and touch.pos[1] < (Window.height/5+Window.height/45)+Window.height/16 + Window.height/27 + Window.height/12.7058823529*2:
            touch_index = 3
        if touch.pos[1] > (Window.height/5+Window.height/45)+Window.height/16 + Window.height/12.7058823529*3 and touch.pos[1] < (Window.height/5+Window.height/45)+Window.height/16 + Window.height/27 + Window.height/12.7058823529*3:
            touch_index = 4
        if touch.pos[1] > (Window.height/5+Window.height/45)+Window.height/16 + Window.height/12.7058823529*4 and touch.pos[1] < (Window.height/5+Window.height/45)+Window.height/16 + Window.height/27 + Window.height/12.7058823529*4:
            touch_index = 5
        if touch.pos[1] > (Window.height/5+Window.height/45)+Window.height/16 + Window.height/12.7058823529*5 and touch.pos[1] < (Window.height/5+Window.height/45)+Window.height/16 + Window.height/27 + Window.height/12.7058823529*5:
            touch_index = 6
        if touch.pos[1] > (Window.height/5+Window.height/45)+Window.height/16 + Window.height/12.7058823529*6 and touch.pos[1] < (Window.height/5+Window.height/45)+Window.height/16 + Window.height/27 + Window.height/12.7058823529*6:
            touch_index = 7

        global hand1
        global hand2
        global hand3
        global hand4
        atk_inc = 0
        hp_inc = 0
        spd_inc = 0

        if hand1 == True:
            if player.stored[0] == r"Images\+one attack.png":
                atk_inc = 1
            if player.stored[0] == r"Images\+two attack.png":
                atk_inc = 2
            if player.stored[0] == r"Images\+three attack.png":
                atk_inc = 3

            if player.stored[0] == r"Images\+one health.png":
                hp_inc = 1
            if player.stored[0] == r"Images\+two health.png":
                hp_inc = 2
            if player.stored[0] == r"Images\+three health.png":
                hp_inc = 3
            
            if player.stored[0] == r"Images\+one speed.png":
                spd_inc = 1
            if player.stored[0] == r"Images\+two speed.png":
                spd_inc = 2

            if player.stored[0] == r"Images\-1 cooldown.png":
                for row in rest_spot:
                    if row.cd > 0:
                        row.cd -= 1
            if player.stored[0] == r"Images\-2 cooldown.png":
                for row in rest_spot:
                    if row.cd > 0:
                        row.cd -= 1
                for row in rest_spot:
                    if row.cd > 0:
                        row.cd -= 1
                
            if player.stored[0] == r"Images\+one cooldown.png":
                for row in O_rest_spot:
                    row.cd += 1
            if player.stored[0] == r"Images\+two cooldown.png":
                for row in O_rest_spot:
                    row.cd += 2

            player.use_card(player.stored[0])
            self.ids.hand_one.source = r"C:\Users\salam\OneDrive\Desktop\Visual studio\Images\card_sleeve.png"
            hand1 = False
        if hand2 == True:
            if player.stored[1] == r"Images\+one attack.png":
                atk_inc = 1
            if player.stored[1] == r"Images\+two attack.png":
                atk_inc = 2
            if player.stored[1] == r"Images\+three attack.png":
                atk_inc = 3

            if player.stored[1] == r"Images\+one health.png":
                hp_inc = 1
            if player.stored[1] == r"Images\+two health.png":
                hp_inc = 2
            if player.stored[1] == r"Images\+three health.png":
                hp_inc = 3
            
            if player.stored[1] == r"Images\+one speed.png":
                spd_inc = 1
            if player.stored[1] == r"Images\+two speed.png":
                spd_inc = 2

            if player.stored[1] == r"Images\-1 cooldown.png":
                for row in rest_spot:
                    if row.cd > 0:
                        row.cd -= 1
            if player.stored[1] == r"Images\-2 cooldown.png":
                for row in rest_spot:
                    if row.cd > 0:
                        row.cd -= 1
                for row in rest_spot:
                    if row.cd > 0:
                        row.cd -= 1
                
            if player.stored[1] == r"Images\+one cooldown.png":
                for row in O_rest_spot:
                    row.cd += 1
            if player.stored[1] == r"Images\+two cooldown.png":
                for row in O_rest_spot:
                    row.cd += 2
    
            player.use_card(player.stored[1])
            self.ids.hand_two.source = r"C:\Users\salam\OneDrive\Desktop\Visual studio\Images\card_sleeve.png"
            hand2 = False
        if hand3 == True:
            if player.stored[2] == r"Images\+one attack.png":
                atk_inc = 1
            if player.stored[2] == r"Images\+two attack.png":
                atk_inc = 2
            if player.stored[2] == r"Images\+three attack.png":
                atk_inc = 3

            if player.stored[2] == r"Images\+one health.png":
                hp_inc = 1
            if player.stored[2] == r"Images\+two health.png":
                hp_inc = 2
            if player.stored[2] == r"Images\+three health.png":
                hp_inc = 3
            
            if player.stored[2] == r"Images\+one speed.png":
                spd_inc = 1
            if player.stored[2] == r"Images\+two speed.png":
                spd_inc = 2

            if player.stored[2] == r"Images\-1 cooldown.png":
                for row in rest_spot:
                    if row.cd > 0:
                        row.cd -= 1
            if player.stored[2] == r"Images\-2 cooldown.png":
                for row in rest_spot:
                    if row.cd > 0:
                        row.cd -= 1
                for row in rest_spot:
                    if row.cd > 0:
                        row.cd -= 1
                
            if player.stored[2] == r"Images\+one cooldown.png":
                for row in O_rest_spot:
                    row.cd += 1
            if player.stored[2] == r"Images\+two cooldown.png":
                for row in O_rest_spot:
                    row.cd += 2

            player.use_card(player.stored[2])
            self.ids.hand_three.source = r"C:\Users\salam\OneDrive\Desktop\Visual studio\Images\card_sleeve.png"
            hand3 = False
        if hand4 == True:
            if player.stored[3] == r"Images\+one attack.png":
                atk_inc = 1
            if player.stored[3] == r"Images\+two attack.png":
                atk_inc = 2
            if player.stored[3] == r"Images\+three attack.png":
                atk_inc = 3

            if player.stored[3] == r"Images\+one health.png":
                hp_inc = 1
            if player.stored[3] == r"Images\+two health.png":
                hp_inc = 2
            if player.stored[3] == r"Images\+three health.png":
                hp_inc = 3
            
            if player.stored[3] == r"Images\+one speed.png":
                spd_inc = 1
            if player.stored[3] == r"Images\+two speed.png":
                spd_inc = 2

            if player.stored[3] == r"Images\-1 cooldown.png":
                for row in rest_spot:
                    if row.cd > 0:
                        row.cd -= 1
            if player.stored[3] == r"Images\-2 cooldown.png":
                for row in rest_spot:
                    if row.cd > 0:
                        row.cd -= 1
                for row in rest_spot:
                    if row.cd > 0:
                        row.cd -= 1
                
            if player.stored[3] == r"Images\+one cooldown.png":
                for row in O_rest_spot:
                    row.cd += 1
            if player.stored[3] == r"Images\+two cooldown.png":
                for row in O_rest_spot:
                    row.cd += 2

            player.use_card(player.stored[3])
            self.ids.hand_four.source = r"C:\Users\salam\OneDrive\Desktop\Visual studio\Images\card_sleeve.png"
            hand4 = False

        if swordman.cd >= 0:
            self.ids.swordmanCD.text = str(swordman.cd)
        if ion.cd >= 0:
            self.ids.ionCD.text = str(ion.cd)
        if apex.cd >= 0:
            self.ids.apexCD.text = str(apex.cd)
        if blade.cd >= 0:
            self.ids.bladeCD.text = str(blade.cd)
        if tank.cd >= 0:
            self.ids.tankCD.text = str(tank.cd)
        if bomb.cd >= 0:
            self.ids.bombCD.text = str(bomb.cd)
        if jolt.cd >= 0:
            self.ids.joltCD.text = str(jolt.cd)

        if O_swordman.cd >= 0:
            self.ids.O_swordmanCD.text = str(O_swordman.cd)
        if O_ion.cd >= 0:
            self.ids.O_ionCD.text = str(O_ion.cd)
        if O_apex.cd >= 0:
            self.ids.O_apexCD.text = str(O_apex.cd)
        if O_blade.cd >= 0:
            self.ids.O_bladeCD.text = str(O_blade.cd)
        if O_tank.cd >= 0:
            self.ids.O_tankCD.text = str(O_tank.cd)
        if O_bomb.cd >= 0:
            self.ids.O_bombCD.text = str(O_bomb.cd)
        if O_jolt.cd >= 0:
            self.ids.O_joltCD.text = str(O_jolt.cd)
            
        if touch_index != 999:
            if touch.pos[0] < Window.width/2 - 3*Window.width/5/27: # left
                if left_lane[touch_index] != "x":
                    left_lane[touch_index].atk += atk_inc
                    left_lane[touch_index].hp += hp_inc
                    left_lane[touch_index].spd += spd_inc
            elif touch.pos[0] > Window.width/2 + 3*Window.width/5/27: #right
                if right_lane[touch_index] != "x":
                    right_lane[touch_index].atk += atk_inc
                    right_lane[touch_index].hp += hp_inc
                    right_lane[touch_index].spd += spd_inc
            else: # mid
                if mid_lane[touch_index] != "x":
                    mid_lane[touch_index].atk += atk_inc
                    mid_lane[touch_index].hp += hp_inc
                    mid_lane[touch_index].spd += spd_inc
#########################################################################################################################################
# end turn
        if self.ids.end_turn.pos[0] < touch.pos[0] and self.ids.end_turn.pos[0] + Window.width/5 > touch.pos[0] and self.ids.end_turn.pos[1] < touch.pos[1] and self.ids.end_turn.pos[1] + Window.width/24 > touch.pos[1]:
            global damage_dealt
            global damage_recived
            damage_dealt = 1
            damage_recived = 1
            swordman.spd = swordman.original_spd
            ion.spd = ion.original_spd
            apex.spd = apex.original_spd
            blade.spd = blade.original_spd
            tank.spd = tank.original_spd
            bomb.spd = bomb.original_spd
            jolt.spd = jolt.original_spd
            global draw_per_turn
            draw_per_turn = 1
            for row in rest_spot:
                row.cd -= 1
            for row in O_rest_spot:
                row.cd -= 1
            
            if swordman.cd >= 0:
                self.ids.swordmanCD.text = str(swordman.cd)
            if ion.cd >= 0:
                self.ids.ionCD.text = str(ion.cd)
            if apex.cd >= 0:
                self.ids.apexCD.text = str(apex.cd)
            if blade.cd >= 0:
                self.ids.bladeCD.text = str(blade.cd)
            if tank.cd >= 0:
                self.ids.tankCD.text = str(tank.cd)
            if bomb.cd >= 0:
                self.ids.bombCD.text = str(bomb.cd)
            if jolt.cd >= 0:
                self.ids.joltCD.text = str(jolt.cd)
                   
            if O_swordman.cd >= 0:
                self.ids.O_swordmanCD.text = str(O_swordman.cd)
            if O_ion.cd >= 0:
                self.ids.O_ionCD.text = str(O_ion.cd)
            if O_apex.cd >= 0:
                self.ids.O_apexCD.text = str(O_apex.cd)
            if O_blade.cd >= 0:
                self.ids.O_bladeCD.text = str(O_blade.cd)
            if O_tank.cd >= 0:
                self.ids.O_tankCD.text = str(O_tank.cd)
            if O_bomb.cd >= 0:
                self.ids.O_bombCD.text = str(O_bomb.cd)
            if O_jolt.cd >= 0:
                self.ids.O_joltCD.text = str(O_jolt.cd)
            
            global summon_right
            summon_right = False
            for row in left_lane:
                if row != "x":
                    if row.team == "opponent":
                        summon_right = True
#########################################################################################################################################
# O_swordman
            global O_swordman_summon
            global O_swordman_index
            O_swordman.spd = O_swordman.original_spd
            if O_swordman.cd <= 0:
                for row in left_lane:
                    if row != "x":
                        if row.team == "opponent":
                            summon_right = True
                if O_swordman_summon == False and summon_right == True and O_swordman.alive == True:
                    if right_lane[6] == "x":
                        O_swordman_index = 6
                        O_swordman.lane = "right"
                        self.ids.O_swordman.pos = (Window.width/5+3*Window.width/5/5*4)-Window.width/102.4, (Window.height/5+Window.height/45)+Window.height/16 + Window.height/12.7058823529*5
                        O_rest_spot.remove(O_swordman)
                        right_lane[6] = O_swordman
                        O_swordman_summon = True
                        summon_right = False
                if O_swordman_summon == False and O_swordman.alive == True:
                    if left_lane[6] == "x":
                        O_swordman_index = 6
                        O_swordman.lane = "left"
                        self.ids.O_swordman.pos = (Window.width/5+3*Window.width/5/5)-Window.width/102.4, (Window.height/5+Window.height/45)+Window.height/16 + Window.height/12.7058823529*5
                        O_rest_spot.remove(O_swordman)
                        left_lane[6] = O_swordman
                        O_swordman_summon = True

                while O_swordman.spd > 0 and O_swordman.alive == True and O_swordman_index > 0 and O_swordman_summon == True and swordman.hp > 0:
                    if O_swordman.lane == "left":
                        if left_lane[O_swordman_index-1] == "x":
                            (left_lane[O_swordman_index-1],left_lane[O_swordman_index]) = (left_lane[O_swordman_index], left_lane[O_swordman_index-1]) 
                            O_swordman.spd -= 1
                            O_swordman_index -= 1
                            self.ids.O_swordman.pos[1] -= Window.height/12.7058823529
                        elif left_lane[O_swordman_index-1].team == "player":          
                            O_swordman.hp -= left_lane[O_swordman_index-1].atk
                            left_lane[O_swordman_index-1].hp -= O_swordman.atk
                        else:
                            break
                                    
                    if O_swordman.lane == "right":
                        if right_lane[O_swordman_index-1] == "x":
                            (right_lane[O_swordman_index-1],right_lane[O_swordman_index]) = (right_lane[O_swordman_index], left_lane[O_swordman_index-1]) 
                            O_swordman.spd -= 1
                            O_swordman_index -= 1
                            self.ids.O_swordman.pos[1] -= Window.height/12.7058823529
                        elif right_lane[O_swordman_index-1].team == "player":                        
                            O_swordman.hp -= right_lane[O_swordman_index-1].atk
                            right_lane[O_swordman_index-1].hp -= O_swordman.atk
                        else:
                            break

                    if O_swordman.hp <= 0:
                        O_swordman_summon = False
                        O_swordman.alive = False
                        if O_swordman.lane == "left":
                            left_lane[O_swordman_index] = "x"
                        if O_swordman.lane == "right":
                            right_lane[O_swordman_index] = "x"

                        O_core.insert(0, O_swordman)
                        self.ids.O_swordman.pos = -self.ids.O_swordman.size[0],-self.ids.O_swordman.size[1]
                        if O_core[2] == "x":
                            O_core.pop()
                        O_swordman.hp = O_swordman.original_hp

#########################################################################################################################################
# O_ion
            global O_ion_summon
            global O_ion_index
            # print(O_ion_index)
            O_ion.spd = O_ion.original_spd
            if O_ion.cd <= 0:
                for row in left_lane:
                    if row != "x":
                        if row.team == "opponent":
                            summon_right = True
                if O_ion_summon == False and summon_right == True and O_ion.alive == True:
                    if right_lane[6] == "x":
                        O_ion_index = 6
                        O_ion.lane = "right"
                        self.ids.O_ion.pos = (Window.width/5+3*Window.width/5/5*4)-Window.width/102.4, (Window.height/5+Window.height/45)+Window.height/16 + Window.height/12.7058823529*5
                        O_rest_spot.remove(O_ion)
                        right_lane[6] = O_ion
                        O_ion_summon = True
                        summon_right = False
                        
                if O_ion_summon == False and O_ion.alive == True:
                    if left_lane[6] == "x":
                        O_ion_index = 6
                        O_ion.lane = "left"
                        self.ids.O_ion.pos = (Window.width/5+3*Window.width/5/5)-Window.width/102.4, (Window.height/5+Window.height/45)+Window.height/16 + Window.height/12.7058823529*5
                        O_rest_spot.remove(O_ion)
                        left_lane[6] = O_ion
                        O_ion_summon = True

                while O_ion.spd > 0 and O_ion.alive == True and O_ion_index > 0 and O_ion_summon == True and swordman.hp > 0:
                    if O_ion.lane == "left":
                        if left_lane[O_ion_index-1] == "x":
                            (left_lane[O_ion_index-1],left_lane[O_ion_index]) = (left_lane[O_ion_index], left_lane[O_ion_index-1]) 
                            O_ion.spd -= 1
                            O_ion_index -= 1
                            self.ids.O_ion.pos[1] -= Window.height/12.7058823529
                        elif left_lane[O_ion_index-1].team == "player":          
                            O_ion.hp -= left_lane[O_ion_index-1].atk
                            left_lane[O_ion_index-1].hp -= O_ion.atk
                        else:
                            break
                                    
                    if O_ion.lane == "right":
                        if right_lane[O_ion_index-1] == "x":
                            (right_lane[O_ion_index-1],right_lane[O_ion_index]) = (right_lane[O_ion_index], left_lane[O_ion_index-1]) 
                            O_ion.spd -= 1
                            O_ion_index -= 1
                            self.ids.O_ion.pos[1] -= Window.height/12.7058823529
                        elif right_lane[O_ion_index-1].team == "player":                        
                            O_ion.hp -= right_lane[O_ion_index-1].atk
                            right_lane[O_ion_index-1].hp -= O_ion.atk
                        else:
                            break

                    if O_ion.hp <= 0:
                        O_ion_summon = False
                        O_ion.alive = False
                        if O_ion.lane == "left":
                            left_lane[O_ion_index] = "x"
                        if O_ion.lane == "right":
                            right_lane[O_ion_index] = "x"

                        O_core.insert(0, O_ion)
                        self.ids.O_ion.pos = -self.ids.O_ion.size[0],-self.ids.O_ion.size[1]
                        if O_core[2] == "x":
                            O_core.pop()
                        O_ion.hp = O_ion.original_hp

#########################################################################################################################################
# O_apex
            global O_apex_summon
            global O_apex_index
            O_apex.spd = O_apex.original_spd
            if O_apex.cd <= 0:
                for row in left_lane:
                    if row != "x":
                        if row.team == "opponent":
                            summon_right = True
                if O_apex_summon == False and summon_right == True and O_apex.alive == True:
                    if right_lane[6] == "x":
                        O_apex_index = 6
                        O_apex.lane = "right"
                        self.ids.O_apex.pos = (Window.width/5+3*Window.width/5/5*4)-Window.width/102.4, (Window.height/5+Window.height/45)+Window.height/16 + Window.height/12.7058823529*5
                        O_rest_spot.remove(O_apex)
                        right_lane[6] = O_apex
                        O_apex_summon = True
                        summon_right = False
                        
                if O_apex_summon == False and O_apex.alive == True:
                    if left_lane[6] == "x":
                        O_apex_index = 6
                        O_apex.lane = "left"
                        self.ids.O_apex.pos = (Window.width/5+3*Window.width/5/5)-Window.width/102.4, (Window.height/5+Window.height/45)+Window.height/16 + Window.height/12.7058823529*5
                        O_rest_spot.remove(O_apex)
                        left_lane[6] = O_apex
                        O_apex_summon = True

                while O_apex.spd > 0 and O_apex.alive == True and O_apex_index > 0 and O_apex_summon == True and swordman.hp > 0:
                    if O_apex.lane == "left":
                        if left_lane[O_apex_index-1] == "x":
                            (left_lane[O_apex_index-1],left_lane[O_apex_index]) = (left_lane[O_apex_index], left_lane[O_apex_index-1]) 
                            O_apex.spd -= 1
                            O_apex_index -= 1
                            self.ids.O_apex.pos[1] -= Window.height/12.7058823529
                        elif left_lane[O_apex_index-1].team == "player":          
                            O_apex.hp -= left_lane[O_apex_index-1].atk
                            left_lane[O_apex_index-1].hp -= O_apex.atk
                        else:
                            break
                                    
                    if O_apex.lane == "right":
                        if right_lane[O_apex_index-1] == "x":
                            (right_lane[O_apex_index-1],right_lane[O_apex_index]) = (right_lane[O_apex_index], left_lane[O_apex_index-1]) 
                            O_apex.spd -= 1
                            O_apex_index -= 1
                            self.ids.O_apex.pos[1] -= Window.height/12.7058823529
                        elif right_lane[O_apex_index-1].team == "player":                        
                            O_apex.hp -= right_lane[O_apex_index-1].atk
                            right_lane[O_apex_index-1].hp -= O_apex.atk
                        else:
                            break

                    if O_apex.hp <= 0:
                        O_apex_summon = False
                        O_apex.alive = False
                        if O_apex.lane == "left":
                            left_lane[O_apex_index] = "x"
                        if O_apex.lane == "right":
                            right_lane[O_apex_index] = "x"

                        O_core.insert(0, O_apex)
                        self.ids.O_apex.pos = -self.ids.O_apex.size[0],-self.ids.O_apex.size[1]
                        if O_core[2] == "x":
                            O_core.pop()
                        O_apex.hp = O_apex.original_hp

#########################################################################################################################################
# O_blade
            global O_blade_summon
            global O_blade_index
            O_blade.spd = O_blade.original_spd
            if O_blade.cd <= 0:
                for row in left_lane:
                    if row != "x":
                        if row.team == "opponent":
                            summon_right = True
                if O_blade_summon == False and summon_right == True and O_blade.alive == True:
                    if right_lane[6] == "x":
                        O_blade_index = 6
                        O_blade.lane = "right"
                        self.ids.O_blade.pos = (Window.width/5+3*Window.width/5/5*4)-Window.width/102.4, (Window.height/5+Window.height/45)+Window.height/16 + Window.height/12.7058823529*5
                        O_rest_spot.remove(O_blade)
                        right_lane[6] = O_blade
                        O_blade_summon = True
                        summon_right = False
                        
                if O_blade_summon == False and O_blade.alive == True:
                    if left_lane[6] == "x":
                        O_blade_index = 6
                        O_blade.lane = "left"
                        self.ids.O_blade.pos = (Window.width/5+3*Window.width/5/5)-Window.width/102.4, (Window.height/5+Window.height/45)+Window.height/16 + Window.height/12.7058823529*5
                        O_rest_spot.remove(O_blade)
                        left_lane[6] = O_blade
                        O_blade_summon = True

                while O_blade.spd > 0 and O_blade.alive == True and O_blade_index > 0 and O_blade_summon == True and swordman.hp > 0:
                    if O_blade.lane == "left":
                        if left_lane[O_blade_index-1] == "x":
                            (left_lane[O_blade_index-1],left_lane[O_blade_index]) = (left_lane[O_blade_index], left_lane[O_blade_index-1]) 
                            O_blade.spd -= 1
                            O_blade_index -= 1
                            self.ids.O_blade.pos[1] -= Window.height/12.7058823529
                        elif left_lane[O_blade_index-1].team == "player":          
                            O_blade.hp -= left_lane[O_blade_index-1].atk
                            left_lane[O_blade_index-1].hp -= O_blade.atk
                        else:
                            break
                                    
                    if O_blade.lane == "right":
                        if right_lane[O_blade_index-1] == "x":
                            (right_lane[O_blade_index-1],right_lane[O_blade_index]) = (right_lane[O_blade_index], left_lane[O_blade_index-1]) 
                            O_blade.spd -= 1
                            O_blade_index -= 1
                            self.ids.O_blade.pos[1] -= Window.height/12.7058823529
                        elif right_lane[O_blade_index-1].team == "player":                        
                            O_blade.hp -= right_lane[O_blade_index-1].atk
                            right_lane[O_blade_index-1].hp -= O_blade.atk
                        else:
                            break

                    if O_blade.hp <= 0:
                        O_blade_summon = False
                        O_blade.alive = False
                        if O_blade.lane == "left":
                            left_lane[O_blade_index] = "x"
                        if O_blade.lane == "right":
                            right_lane[O_blade_index] = "x"

                        O_core.insert(0, O_blade)
                        self.ids.O_blade.pos = -self.ids.O_blade.size[0],-self.ids.O_blade.size[1]
                        if O_core[2] == "x":
                            O_core.pop()
                        O_blade.hp = O_blade.original_hp

#########################################################################################################################################
# O_tank
            global O_tank_summon
            global O_tank_index
            O_tank.spd = O_tank.original_spd
            if O_tank.cd <= 0:
                for row in left_lane:
                    if row != "x":
                        if row.team == "opponent":
                            summon_right = True
                if O_tank_summon == False and summon_right == True and O_tank.alive == True:
                    if right_lane[6] == "x":
                        O_tank_index = 6
                        O_tank.lane = "right"
                        self.ids.O_tank.pos = (Window.width/5+3*Window.width/5/5*4)-Window.width/102.4, (Window.height/5+Window.height/45)+Window.height/16 + Window.height/12.7058823529*5
                        O_rest_spot.remove(O_tank)
                        right_lane[6] = O_tank
                        O_tank_summon = True
                        summon_right = False
                        
                if O_tank_summon == False and O_tank.alive == True:
                    if left_lane[6] == "x":
                        O_tank_index = 6
                        O_tank.lane = "left"
                        self.ids.O_tank.pos = (Window.width/5+3*Window.width/5/5)-Window.width/102.4, (Window.height/5+Window.height/45)+Window.height/16 + Window.height/12.7058823529*5
                        O_rest_spot.remove(O_tank)
                        left_lane[6] = O_tank
                        O_tank_summon = True

                while O_tank.spd > 0 and O_tank.alive == True and O_tank_index > 0 and O_tank_summon == True and swordman.hp > 0:
                    if O_tank.lane == "left":
                        if left_lane[O_tank_index-1] == "x":
                            (left_lane[O_tank_index-1],left_lane[O_tank_index]) = (left_lane[O_tank_index], left_lane[O_tank_index-1]) 
                            O_tank.spd -= 1
                            O_tank_index -= 1
                            self.ids.O_tank.pos[1] -= Window.height/12.7058823529
                        elif left_lane[O_tank_index-1].team == "player":          
                            O_tank.hp -= left_lane[O_tank_index-1].atk
                            left_lane[O_tank_index-1].hp -= O_tank.atk
                        else:
                            break
                                    
                    if O_tank.lane == "right":
                        if right_lane[O_tank_index-1] == "x":
                            (right_lane[O_tank_index-1],right_lane[O_tank_index]) = (right_lane[O_tank_index], left_lane[O_tank_index-1]) 
                            O_tank.spd -= 1
                            O_tank_index -= 1
                            self.ids.O_tank.pos[1] -= Window.height/12.7058823529
                        elif right_lane[O_tank_index-1].team == "player":                        
                            O_tank.hp -= right_lane[O_tank_index-1].atk
                            right_lane[O_tank_index-1].hp -= O_tank.atk
                        else:
                            break

                    if O_tank.hp <= 0:
                        O_tank_summon = False
                        O_tank.alive = False
                        if O_tank.lane == "left":
                            left_lane[O_tank_index] = "x"
                        if O_tank.lane == "right":
                            right_lane[O_tank_index] = "x"

                        O_core.insert(0, O_tank)
                        self.ids.O_tank.pos = -self.ids.O_tank.size[0],-self.ids.O_tank.size[1]
                        if O_core[2] == "x":
                            O_core.pop()
                        O_tank.hp = O_tank.original_hp

#########################################################################################################################################
# O_bomb
            global O_bomb_summon
            global O_bomb_index
            O_bomb.spd = O_bomb.original_spd
            if O_bomb.cd <= 0:
                for row in left_lane:
                    if row != "x":
                        if row.team == "opponent":
                            summon_right = True
                if O_bomb_summon == False and summon_right == True and O_bomb.alive == True:
                    if right_lane[6] == "x":
                        O_bomb_index = 6
                        O_bomb.lane = "right"
                        self.ids.O_bomb.pos = (Window.width/5+3*Window.width/5/5*4)-Window.width/102.4, (Window.height/5+Window.height/45)+Window.height/16 + Window.height/12.7058823529*5
                        O_rest_spot.remove(O_bomb)
                        right_lane[6] = O_bomb
                        O_bomb_summon = True
                        summon_right = False
                        
                if O_bomb_summon == False and O_bomb.alive == True:
                    if left_lane[6] == "x":
                        O_bomb_index = 6
                        O_bomb.lane = "left"
                        self.ids.O_bomb.pos = (Window.width/5+3*Window.width/5/5)-Window.width/102.4, (Window.height/5+Window.height/45)+Window.height/16 + Window.height/12.7058823529*5
                        O_rest_spot.remove(O_bomb)
                        left_lane[6] = O_bomb
                        O_bomb_summon = True

                while O_bomb.spd > 0 and O_bomb.alive == True and O_bomb_index > 0 and O_bomb_summon == True and swordman.hp > 0:
                    if O_bomb.lane == "left":
                        if left_lane[O_bomb_index-1] == "x":
                            (left_lane[O_bomb_index-1],left_lane[O_bomb_index]) = (left_lane[O_bomb_index], left_lane[O_bomb_index-1]) 
                            O_bomb.spd -= 1
                            O_bomb_index -= 1
                            self.ids.O_bomb.pos[1] -= Window.height/12.7058823529
                        elif left_lane[O_bomb_index-1].team == "player":          
                            O_bomb.hp -= left_lane[O_bomb_index-1].atk
                            left_lane[O_bomb_index-1].hp -= O_bomb.atk
                        else:
                            break
                                    
                    if O_bomb.lane == "right":
                        if right_lane[O_bomb_index-1] == "x":
                            (right_lane[O_bomb_index-1],right_lane[O_bomb_index]) = (right_lane[O_bomb_index], left_lane[O_bomb_index-1]) 
                            O_bomb.spd -= 1
                            O_bomb_index -= 1
                            self.ids.O_bomb.pos[1] -= Window.height/12.7058823529
                        elif right_lane[O_bomb_index-1].team == "player":                        
                            O_bomb.hp -= right_lane[O_bomb_index-1].atk
                            right_lane[O_bomb_index-1].hp -= O_bomb.atk
                        else:
                            break

                    if O_bomb.hp <= 0:
                        O_bomb_summon = False
                        O_bomb.alive = False
                        if O_bomb.lane == "left":
                            left_lane[O_bomb_index] = "x"
                        if O_bomb.lane == "right":
                            right_lane[O_bomb_index] = "x"

                        O_core.insert(0, O_bomb)
                        self.ids.O_bomb.pos = -self.ids.O_bomb.size[0],-self.ids.O_bomb.size[1]
                        if O_core[2] == "x":
                            O_core.pop()
                        O_core.hp = O_core.original_hp

#########################################################################################################################################
# O_jolt
            global O_jolt_summon
            global O_jolt_index
            O_jolt.spd = O_jolt.original_spd
            if O_jolt.cd <= 0:
                for row in left_lane:
                    if row != "x":
                        if row.team == "opponent":
                            summon_right = True
                if O_jolt_summon == False and summon_right == True and O_jolt.alive == True:
                    if right_lane[6] == "x":
                        O_jolt_index = 6
                        O_jolt.lane = "right"
                        self.ids.O_jolt.pos = (Window.width/5+3*Window.width/5/5*4)-Window.width/102.4, (Window.height/5+Window.height/45)+Window.height/16 + Window.height/12.7058823529*5
                        O_rest_spot.remove(O_jolt)
                        right_lane[6] = O_jolt
                        O_jolt_summon = True
                        summon_right = False
                        
                if O_jolt_summon == False and O_jolt.alive == True:
                    if left_lane[6] == "x":
                        O_jolt_index = 6
                        O_jolt.lane = "left"
                        self.ids.O_jolt.pos = (Window.width/5+3*Window.width/5/5)-Window.width/102.4, (Window.height/5+Window.height/45)+Window.height/16 + Window.height/12.7058823529*5
                        O_rest_spot.remove(O_jolt)
                        left_lane[6] = O_jolt
                        O_jolt_summon = True

                while O_jolt.spd > 0 and O_jolt.alive == True and O_jolt_index > 0 and O_jolt_summon == True and swordman.hp > 0:
                    if O_jolt.lane == "left":
                        if left_lane[O_jolt_index-1] == "x":
                            (left_lane[O_jolt_index-1],left_lane[O_jolt_index]) = (left_lane[O_jolt_index], left_lane[O_jolt_index-1]) 
                            O_jolt.spd -= 1
                            O_jolt_index -= 1
                            self.ids.O_jolt.pos[1] -= Window.height/12.7058823529
                        elif left_lane[O_jolt_index-1].team == "player":          
                            O_jolt.hp -= left_lane[O_jolt_index-1].atk
                            left_lane[O_jolt_index-1].hp -= O_jolt.atk
                        else:
                            break
                                    
                    if O_jolt.lane == "right":
                        if right_lane[O_jolt_index-1] == "x":
                            (right_lane[O_jolt_index-1],right_lane[O_jolt_index]) = (right_lane[O_jolt_index], left_lane[O_jolt_index-1]) 
                            O_jolt.spd -= 1
                            O_jolt_index -= 1
                            self.ids.O_jolt.pos[1] -= Window.height/12.7058823529
                        elif right_lane[O_jolt_index-1].team == "player":                        
                            O_jolt.hp -= right_lane[O_jolt_index-1].atk
                            right_lane[O_jolt_index-1].hp -= O_jolt.atk
                        else:
                            break

                    if O_jolt.hp <= 0:
                        O_jolt_summon = False
                        O_jolt.alive = False
                        if O_jolt.lane == "left":
                            left_lane[O_jolt_index] = "x"
                        if O_jolt.lane == "right":
                            right_lane[O_jolt_index] = "x"

                        O_core.insert(0, O_jolt)
                        self.ids.O_jolt.pos = -self.ids.O_jolt.size[0],-self.ids.O_jolt.size[1]
                        if O_core[2] == "x":
                            O_core.pop()
                        O_jolt.hp = O_jolt.original_hp
  

#########################################################################################################################################
# O_swordman killed on player turn
        if O_swordman.alive == True:
            if O_swordman.hp <= 0:
                O_swordman_summon = False
                O_swordman.alive = False
                if O_swordman.lane == "left":
                    left_lane[O_swordman_index] = "x"
                if O_swordman.lane == "right":
                    right_lane[O_swordman_index] = "x"

                O_core.insert(0, O_swordman)
                self.ids.O_swordman.pos = -self.ids.O_swordman.size[0],-self.ids.O_swordman.size[1]
                if O_core[2] == "x":
                    O_core.pop()
#########################################################################################################################################
# O_ion killed on player turn
        if O_ion.alive == True:
            if O_ion.hp <= 0:
                O_ion_summon = False
                O_ion.alive = False
                if O_ion.lane == "left":
                    left_lane[O_ion_index] = "x"
                if O_ion.lane == "right":
                    right_lane[O_ion_index] = "x"

                O_core.insert(0, O_ion)
                self.ids.O_ion.pos = -self.ids.O_ion.size[0],-self.ids.O_ion.size[1]
                if O_core[2] == "x":
                    O_core.pop()
#########################################################################################################################################
# O_apex killed on player turn
        if O_apex.alive == True:
            if O_apex.hp <= 0:
                O_apex_summon = False
                O_apex.alive = False
                if O_apex.lane == "left":
                    left_lane[O_apex_index] = "x"
                if O_apex.lane == "right":
                    right_lane[O_apex_index] = "x"

                O_core.insert(0, O_apex)
                self.ids.O_apex.pos = -self.ids.O_apex.size[0],-self.ids.O_apex.size[1]
                if O_core[2] == "x":
                    O_core.pop()
#########################################################################################################################################
# O_blade killed on player turn
        if O_blade.alive == True:
            if O_blade.hp <= 0:
                O_blade_summon = False
                O_blade.alive = False
                if O_blade.lane == "left":
                    left_lane[O_blade_index] = "x"
                if O_blade.lane == "right":
                    right_lane[O_blade_index] = "x"

                O_core.insert(0, O_blade)
                self.ids.O_blade.pos = -self.ids.O_blade.size[0],-self.ids.O_blade.size[1]
                if O_core[2] == "x":
                    O_core.pop()
#########################################################################################################################################
# O_tank killed on player turn
        if O_tank.alive == True:
            if O_tank.hp <= 0:
                O_tank_summon = False
                O_tank.alive = False
                if O_tank.lane == "left":
                    left_lane[O_tank_index] = "x"
                if O_tank.lane == "right":
                    right_lane[O_tank_index] = "x"

                O_core.insert(0, O_tank)
                self.ids.O_tank.pos = -self.ids.O_tank.size[0],-self.ids.O_tank.size[1]
                if O_core[2] == "x":
                    O_core.pop()
#########################################################################################################################################
# O_bomb killed on player turn
        if O_bomb.alive == True:
            if O_bomb.hp <= 0:
                O_bomb_summon = False
                O_bomb.alive = False
                if O_bomb.lane == "left":
                    left_lane[O_bomb_index] = "x"
                if O_bomb.lane == "right":
                    right_lane[O_bomb_index] = "x"

                O_core.insert(0, O_bomb)
                self.ids.O_bomb.pos = -self.ids.O_bomb.size[0],-self.ids.O_bomb.size[1]
                if O_core[2] == "x":
                    O_core.pop()
#########################################################################################################################################
# O_jolt killed on player turn
        if O_jolt.alive == True:
            if O_jolt.hp <= 0:
                O_jolt_summon = False
                O_jolt.alive = False
                if O_jolt.lane == "left":
                    left_lane[O_jolt_index] = "x"
                if O_jolt.lane == "right":
                    right_lane[O_jolt_index] = "x"

                O_core.insert(0, O_jolt)
                self.ids.O_jolt.pos = -self.ids.O_jolt.size[0],-self.ids.O_jolt.size[1]
                if O_core[2] == "x":
                    O_core.pop()

#########################################################################################################################################
# swordman
        global swordman_bool
        global swordman_index
        if swordman_bool == True:
            if touch.pos[0] < Window.width/2 and left_lane[1] == "x":
                self.ids.swordman.pos = (Window.width/5+3*Window.width/5/5)-Window.width/102.4, (Window.height/5+Window.height/45)+Window.height/16
                left_lane[1] = swordman
                swordman.lane = "left"
            elif touch.pos[0] > Window.width/2 and right_lane[1] == "x":
                self.ids.swordman.pos = (Window.width/5+3*Window.width/5/5*4)-Window.width/102.4, (Window.height/5+Window.height/45)+Window.height/16
                right_lane[1] = swordman 
                swordman.lane = "right"
            else:
                self.ids.swordman.pos = swordman_pos
            rest_spot.remove(swordman)
        swordman_bool = False
        swordman.did_change_lane = False
        if swordman.hp <= 0:
            swordman.alive = False

            if swordman.lane == "left":
                left_lane[swordman_index] = "x"
            elif swordman.lane == "mid":
                mid_lane[swordman_index] = "x"   
            elif swordman.lane == "right":
                right_lane[swordman_index] = "x" 

            core.insert(0, swordman)
            self.ids.swordman.pos = -self.ids.swordman.size[0],-self.ids.swordman.size[1]
            if core[2] == "x":
                core.pop()
            swordman.hp = swordman.original_hp

#########################################################################################################################################
# ion
        global ion_bool
        global ion_index
        if ion_bool == True:
            if touch.pos[0] < Window.width/2 and left_lane[1] == "x":
                self.ids.ion.pos = (Window.width/5+3*Window.width/5/5)-Window.width/102.4, (Window.height/5+Window.height/45)+Window.height/16
                left_lane[1] = ion
                ion.lane = "left"
            elif touch.pos[0] > Window.width/2 and right_lane[1] == "x":
                self.ids.ion.pos = (Window.width/5+3*Window.width/5/5*4)-Window.width/102.4, (Window.height/5+Window.height/45)+Window.height/16
                right_lane[1] = ion 
                ion.lane = "right"
            else:
                self.ids.ion.pos = ion_pos
            rest_spot.remove(ion)
        ion_bool = False
        ion.did_change_lane = False
        if ion.hp <= 0:
            ion.alive = False
            if ion.lane == "left":
                left_lane[ion_index] = "x"
            elif ion.lane == "mid":
                mid_lane[ion_index] = "x"   
            elif ion.lane == "right":
                right_lane[ion_index] = "x" 

            core.insert(0, ion)
            self.ids.ion.pos = -self.ids.ion.size[0],-self.ids.ion.size[1]
            if core[3] == "x":
                core.pop()
            ion.hp = ion.original_hp

#########################################################################################################################################
# apex
        global apex_bool
        global apex_index
        if apex_bool == True:
            if touch.pos[0] < Window.width/2 and left_lane[1] == "x":
                self.ids.apex.pos = (Window.width/5+3*Window.width/5/5)-Window.width/102.4, (Window.height/5+Window.height/45)+Window.height/16
                left_lane[1] = apex
                apex.lane = "left"
            elif touch.pos[0] > Window.width/2 and right_lane[1] == "x":
                self.ids.apex.pos = (Window.width/5+3*Window.width/5/5*4)-Window.width/102.4, (Window.height/5+Window.height/45)+Window.height/16
                right_lane[1] = apex 
                apex.lane = "right"
            else:
                self.ids.apex.pos = apex_pos
            rest_spot.remove(apex)
        apex_bool = False
        apex.did_change_lane = False
        if apex.hp <= 0:
            apex.alive = False
            if apex.lane == "left":
                left_lane[apex_index] = "x"
            elif apex.lane == "mid":
                mid_lane[apex_index] = "x"   
            elif apex.lane == "right":
                right_lane[apex_index] = "x" 

            core.insert(0, apex)
            self.ids.apex.pos = -self.ids.apex.size[0],-self.ids.apex.size[1]
            if core[2] == "x":
                core.pop()
            apex.hp = apex.original_hp

#########################################################################################################################################
# blade
        global blade_bool
        global blade_index
        if blade_bool == True:
            if touch.pos[0] < Window.width/2 and left_lane[1] == "x":
                self.ids.blade.pos = (Window.width/5+3*Window.width/5/5)-Window.width/102.4, (Window.height/5+Window.height/45)+Window.height/16
                left_lane[1] = blade
                blade.lane = "left"
            elif touch.pos[0] > Window.width/2 and right_lane[1] == "x":
                self.ids.blade.pos = (Window.width/5+3*Window.width/5/5*4)-Window.width/102.4, (Window.height/5+Window.height/45)+Window.height/16
                right_lane[1] = blade 
                blade.lane = "right"
            else:
                self.ids.blade.pos = blade_pos
            rest_spot.remove(blade)
        blade_bool = False
        blade.did_change_lane = False
        if blade.hp <= 0:
            blade.alive = False
            if blade.lane == "left":
                left_lane[blade_index] = "x"
            elif blade.lane == "mid":
                mid_lane[blade_index] = "x"   
            elif blade.lane == "right":
                right_lane[blade_index] = "x" 

            core.insert(0, blade)
            self.ids.blade.pos = -self.ids.blade.size[0],-self.ids.blade.size[1]
            if core[2] == "x":
                core.pop()
            blade.hp = blade.original_hp


#########################################################################################################################################
# tank
        global tank_bool
        global tank_index
        if tank_bool == True:
            if touch.pos[0] < Window.width/2 and left_lane[1] == "x":
                self.ids.tank.pos = (Window.width/5+3*Window.width/5/5)-Window.width/102.4, (Window.height/5+Window.height/45)+Window.height/16
                left_lane[1] = tank
                tank.lane = "left"
            elif touch.pos[0] > Window.width/2 and right_lane[1] == "x":
                self.ids.tank.pos = (Window.width/5+3*Window.width/5/5*4)-Window.width/102.4, (Window.height/5+Window.height/45)+Window.height/16
                right_lane[1] = tank 
                tank.lane = "right"
            else:
                self.ids.tank.pos = tank_pos
            rest_spot.remove(tank)
        tank_bool = False
        tank.did_change_lane = False
        if tank.hp <= 0:
            tank.alive = False
            if tank.lane == "left":
                left_lane[tank_index] = "x"
            elif tank.lane == "mid":
                mid_lane[tank_index] = "x"   
            elif tank.lane == "right":
                right_lane[tank_index] = "x" 

            core.insert(0, tank)
            self.ids.tank.pos = -self.ids.tank.size[0],-self.ids.tank.size[1]
            if core[2] == "x":
                core.pop()
            tank.hp = tank.original_hp


#########################################################################################################################################
# bomb
        global bomb_bool
        global bomb_index
        if bomb_bool == True:
            if touch.pos[0] < Window.width/2 and left_lane[1] == "x":
                self.ids.bomb.pos = (Window.width/5+3*Window.width/5/5)-Window.width/102.4, (Window.height/5+Window.height/45)+Window.height/16
                left_lane[1] = bomb
                bomb.lane = "left"
            elif touch.pos[0] > Window.width/2 and right_lane[1] == "x":
                self.ids.bomb.pos = (Window.width/5+3*Window.width/5/5*4)-Window.width/102.4, (Window.height/5+Window.height/45)+Window.height/16
                right_lane[1] = bomb 
                bomb.lane = "right"
            else:
                self.ids.bomb.pos = bomb_pos
            rest_spot.remove(bomb)
        bomb_bool = False
        bomb.did_change_lane = False
        if bomb.hp <= 0:
            bomb.alive = False
            if bomb.lane == "left":
                left_lane[bomb_index] = "x"
            elif bomb.lane == "mid":
                mid_lane[bomb_index] = "x"   
            elif bomb.lane == "right":
                right_lane[bomb_index] = "x" 

            core.insert(0, bomb)
            self.ids.bomb.pos = -self.ids.bomb.size[0],-self.ids.bomb.size[1]
            if core[2] == "x":
                core.pop()
            bomb.hp = bomb.original_hp


#########################################################################################################################################
# jolt
        global jolt_bool
        global jolt_index
        if jolt_bool == True:
            if touch.pos[0] < Window.width/2 and left_lane[1] == "x":
                self.ids.jolt.pos = (Window.width/5+3*Window.width/5/5)-Window.width/102.4, (Window.height/5+Window.height/45)+Window.height/16
                left_lane[1] = jolt
                jolt.lane = "left"
            elif touch.pos[0] > Window.width/2 and right_lane[1] == "x":
                self.ids.jolt.pos = (Window.width/5+3*Window.width/5/5*4)-Window.width/102.4, (Window.height/5+Window.height/45)+Window.height/16
                right_lane[1] = jolt 
                jolt.lane = "right"
            else:
                self.ids.jolt.pos = jolt_pos
            rest_spot.remove(jolt)
        jolt_bool = False
        jolt.did_change_lane = False
        if jolt.hp <= 0:
            jolt.alive = False
            if jolt.lane == "left":
                left_lane[jolt_index] = "x"
            elif jolt.lane == "mid":
                mid_lane[jolt_index] = "x"   
            elif jolt.lane == "right":
                right_lane[jolt_index] = "x" 

            core.insert(0, jolt)
            self.ids.jolt.pos = -self.ids.jolt.size[0],-self.ids.jolt.size[1]
            if core[2] == "x":
                core.pop()
            jolt.hp = jolt.original_hp


#########################################################################################################################################
#revive
        if core[3] == swordman:
            core.pop(3)
            self.ids.swordman.pos = (Window.width/5+3*Window.width/5/3)+3*Window.width/5/15.88 , Window.height/8.5
            swordman.alive = True
            core.append("x")
            swordman.hp = swordman.original_hp
            swordman.spd = swordman.original_spd
            swordman.cd = swordman.original_cd
            rest_spot.append(swordman)
            self.ids.swordmanCD.text = str(swordman.cd)
        
        
#########################################################################################################################################
#revive
        if core[3] == ion:
            core.pop(3)
            self.ids.ion.pos = (Window.width/5+3*Window.width/5/3)+3*Window.width/5/5.8 , Window.height/8.5
            ion.alive = True
            core.append("x")
            ion.hp = ion.original_hp
            ion.spd = ion.original_spd
            ion.cd = ion.original_cd
            rest_spot.append(ion)
            self.ids.ionCD.text = str(ion.cd)
        
        
#########################################################################################################################################
#revive
        if core[3] == apex:
            core.pop(3)
            self.ids.apex.pos = (Window.width/5+3*Window.width/5/3)+3*Window.width/5/3.55 , Window.height/8.5
            apex.alive = True
            core.append("x")
            apex.hp = apex.original_hp
            apex.spd = apex.original_spd
            apex.cd = apex.original_cd
            rest_spot.append(apex)
            self.ids.apexCD.text = str(apex.cd)
        
        
#########################################################################################################################################
#revive
        if core[3] == blade:
            core.pop(3)
            self.ids.blade.pos = (Window.width/5+3*Window.width/5/3)+3*Window.width/5/2.559 , Window.height/8.5      
            blade.alive = True
            core.append("x")
            blade.hp = blade.original_hp
            blade.spd = blade.original_spd
            blade.cd = blade.original_cd
            rest_spot.append(blade)
            self.ids.bladeCD.text = str(blade.cd)
        
        
#########################################################################################################################################
#revive
        if core[3] == tank:
            core.pop(3)
            self.ids.tank.pos = (Window.width/5+3*Window.width/5/3)+3*Window.width/5/11 , Window.height/27.69
            tank.alive = True
            core.append("x")
            tank.hp = tank.original_hp
            tank.spd = tank.original_spd
            tank.cd = tank.original_cd
            rest_spot.append(tank)
            self.ids.tankCD.text = str(tank.cd)

        
#########################################################################################################################################
#revive
        if core[3] == bomb:
            core.pop(3)
            self.ids.bomb.pos = (Window.width/5+3*Window.width/5/3)+3*Window.width/5/4.4 , Window.height/27.69
            bomb.alive = True
            core.append("x")
            bomb.hp = bomb.original_hp
            bomb.spd = bomb.original_spd
            bomb.cd = bomb.original_cd
            rest_spot.append(bomb)
            self.ids.bombCD.text = str(bomb.cd)

        
#########################################################################################################################################
#revive
        if core[3] == jolt:
            core.pop(3)
            self.ids.jolt.pos = (Window.width/5+3*Window.width/5/3)+3*Window.width/5/2.75 , Window.height/27.69
            jolt.alive = True
            core.append("x")
            jolt.hp = jolt.original_hp
            jolt.spd = jolt.original_spd
            jolt.cd = jolt.original_cd
            rest_spot.append(jolt)
            self.ids.joltCD.text = str(jolt.cd)


#########################################################################################################################################
#revive opponent
        if O_core[3] == O_swordman:
            O_core.pop(3)
            self.ids.O_swordman.pos = (Window.width/5+3*Window.width/5/6)+Window.width/28.2352941176 , Window.height-Window.height/6.1       
            O_swordman.alive = True
            O_core.append("x")
            O_swordman.hp = O_swordman.original_hp
            O_swordman.spd = O_swordman.original_spd
            O_swordman.cd = O_swordman.original_cd
            O_rest_spot.append(O_swordman)
            self.ids.O_swordmanCD.text = str(O_swordman.cd)
#########################################################################################################################################
#revive opponent
        if O_core[3] == O_ion:
            O_core.pop(3)
            self.ids.O_ion.pos = (Window.width/5+3*Window.width/5/6)+Window.width/10.3225806452 , Window.height-Window.height/6.1
            O_ion.alive = True
            O_core.append("x")
            O_ion.hp = O_ion.original_hp
            O_ion.spd = O_ion.original_spd
            O_ion.cd = O_ion.original_cd
            O_rest_spot.append(O_ion)
            self.ids.O_ionCD.text = str(O_ion.cd)
#########################################################################################################################################
#revive opponent
        if O_core[3] == O_apex:
            O_core.pop(3)
            self.ids.O_apex.pos = (Window.width/5+3*Window.width/5/6)+Window.width/6.31578947368 , Window.height-Window.height/6.1
            O_apex.alive = True
            O_core.append("x")
            O_apex.hp = O_apex.original_hp
            O_apex.spd = O_apex.original_spd
            O_apex.cd = O_apex.original_cd
            O_rest_spot.append(O_apex)
            self.ids.O_apexCD.text = str(O_apex.cd)
#########################################################################################################################################
#revive opponent
        if O_core[3] == O_blade:
            O_core.pop(3)
            self.ids.O_blade.pos = (Window.width/5+3*Window.width/5/6)+Window.width/4.54976303318 , Window.height-Window.height/6.1
            O_blade.alive = True
            O_core.append("x")
            O_blade.hp = O_blade.original_hp
            O_blade.spd = O_blade.original_spd
            O_blade.cd = O_blade.original_cd
            O_rest_spot.append(O_blade)
            self.ids.O_bladeCD.text = str(O_blade.cd)
#########################################################################################################################################
#revive opponent
        if O_core[3] == O_tank:
            O_core.pop(3)
            self.ids.O_tank.pos = (Window.width/5+3*Window.width/5/6)+Window.width/19.6923076923 , Window.height-Window.height/12.1
            O_tank.alive = True
            O_core.append("x")
            O_tank.hp = O_tank.original_hp
            O_tank.spd = O_tank.original_spd
            O_tank.cd = O_tank.original_cd
            O_rest_spot.append(O_tank)
            self.ids.O_tankCD.text = str(O_tank.cd)
#########################################################################################################################################
#revive opponent
        if O_core[3] == O_bomb:
            O_core.pop(3)
            self.ids.O_bomb.pos = (Window.width/5+3*Window.width/5/6)+Window.width/7.83673469388 , Window.height-Window.height/12.1
            O_core.append("x")
            O_bomb.hp = O_bomb.original_hp
            O_bomb.spd = O_bomb.original_spd
            O_bomb.cd = O_bomb.original_cd
            O_rest_spot.append(O_bomb)
            self.ids.O_bombCD.text = str(O_bomb.cd)
#########################################################################################################################################
#revive opponent
        if O_core[3] == O_jolt:
            O_core.pop(3)
            self.ids.O_jolt.pos = (Window.width/5+3*Window.width/5/6)+Window.width/4.89171974522 , Window.height-Window.height/12.1
            O_jolt.alive = True
            O_core.append("x")
            O_jolt.hp = O_jolt.original_hp
            O_jolt.spd = O_jolt.original_spd
            O_jolt.cd = O_jolt.original_cd
            O_rest_spot.append(O_jolt)
            self.ids.O_joltCD.text = str(O_jolt.cd)


#########################################################################################################################################
# show cards in core
        if core[0] != "x":
            self.ids.core1.source = core[0].source
        else:
            self.ids.core1.source = r"C:\Users\salam\OneDrive\Desktop\Visual studio\Images\card_sleeve.png"
        if core[1] != "x":
            self.ids.core2.source = core[1].source
        else:
            self.ids.core2.source = r"C:\Users\salam\OneDrive\Desktop\Visual studio\Images\card_sleeve.png"
        if core[2] != "x":
            self.ids.core3.source = core[2].source
        else:
            self.ids.core3.source = r"C:\Users\salam\OneDrive\Desktop\Visual studio\Images\card_sleeve.png"

#########################################################################################################################################
# show enemy cards in core
        if O_core[0] != "x":
            self.ids.O_core1.source = O_core[0].source
        else:
            self.ids.O_core1.source = r"C:\Users\salam\OneDrive\Desktop\Visual studio\Images\card_sleeve.png"
        if O_core[1] != "x":
            self.ids.O_core2.source = O_core[1].source
        else:
            self.ids.O_core2.source = r"C:\Users\salam\OneDrive\Desktop\Visual studio\Images\card_sleeve.png"
        if O_core[2] != "x":
            self.ids.O_core3.source = O_core[2].source
        else:
            self.ids.O_core3.source = r"C:\Users\salam\OneDrive\Desktop\Visual studio\Images\card_sleeve.png"
                    

# lose
        global player_life
        if left_lane[0] != "x":
            if left_lane[0].team == "opponent" and damage_recived == 1:
                player_life -= 1
                damage_recived = 0
        if damage_recived == 1:
            if right_lane[0] != "x":
                if right_lane[0].team == "opponent":
                    player_life -= 1
        if player_life == 2:
            self.ids.H1.pos = -self.ids.H1.size[0],-self.ids.H1.size[1]
        elif player_life == 1:
            self.ids.H2.pos = -self.ids.H2.size[0],-self.ids.H2.size[1]
        elif player_life <= 0:
            player_life == 3
            self.ids.O_H1.pos = Window.width/1.09756097561 - self.ids.O_H1.size[0], Window.height - self.ids.O_H1.size[1] 
            self.ids.O_H2.pos = Window.width/1.09756097561 - self.ids.O_H2.size[0], Window.height - 2*self.ids.O_H2.size[1] 
            player_life = 3
            self.ids.H1.pos = Window.width/1.09756097561 - self.ids.H1.size[0], 2*self.ids.H1.size[1] 
            self.ids.H2.pos = Window.width/1.09756097561 - self.ids.H2.size[0], self.ids.H2.size[1] 
            global stage
            stage = 0
            for row in opponent_list:
                row.atk = row.original_atk_stage_0 
                row.hp = row.original_hp_stage_0 
                row.spd = row.original_spd_stage_0 
                row.cd = row.original_cd_stage_0 
            draw_per_turn = 4
            rest_spot.clear()         
            for row in player_list:
                rest_spot.append(row)
            O_rest_spot.clear()
            for row in opponent_list:
                O_rest_spot.append(row)
            for row in right_lane:
                if row != "x":
                    right_lane.insert(right_lane.index(row), "x")
                    right_lane.remove(row)
            for row in mid_lane:
                if row != "x":
                    mid_lane.insert(mid_lane.index(row), "x")
                    mid_lane.remove(row)
            for row in left_lane:
                if row != "x":
                    left_lane.insert(left_lane.index(row), "x")
                    left_lane.remove(row)
            for row in core:
                if row != "x":
                    core.insert(core.index(row), "x")
                    core.remove(row)
            for row in O_core:
                if row != "x":
                    O_core.insert(O_core.index(row), "x")
                    O_core.remove(row)
            if player.stored[0] != "x":
                player.use_card(player.stored[0])
            if player.stored[1] != "x":
                player.use_card(player.stored[1])
            if player.stored[2] != "x":
                player.use_card(player.stored[2])
            if player.stored[3] != "x":
                player.use_card(player.stored[3])
            player.shuffle()
            self.ids.hand_one.source = r"C:\Users\salam\OneDrive\Desktop\Visual studio\Images\card_sleeve.png"
            self.ids.hand_two.source = r"C:\Users\salam\OneDrive\Desktop\Visual studio\Images\card_sleeve.png"
            self.ids.hand_three.source = r"C:\Users\salam\OneDrive\Desktop\Visual studio\Images\card_sleeve.png"
            self.ids.hand_four.source = r"C:\Users\salam\OneDrive\Desktop\Visual studio\Images\card_sleeve.png"

            swordman_bool = False
            swordman_index = 9
            self.ids.swordman.pos = (Window.width/5+3*Window.width/5/3)+3*Window.width/5/15.88 , Window.height/8.5

            ion_bool = False
            ion_index = 9
            self.ids.ion.pos = (Window.width/5+3*Window.width/5/3)+3*Window.width/5/5.8 , Window.height/8.5
        
            apex_bool = False
            apex_index = 9
            self.ids.apex.pos = (Window.width/5+3*Window.width/5/3)+3*Window.width/5/3.55 , Window.height/8.5

            blade_bool = False
            blade_index = 9
            self.ids.blade.pos = (Window.width/5+3*Window.width/5/3)+3*Window.width/5/2.559 , Window.height/8.5   

            tank_bool = False
            tank_index = 9
            self.ids.tank.pos = (Window.width/5+3*Window.width/5/3)+3*Window.width/5/11 , Window.height/27.69

            bomb_bool = False
            bomb_index = 9
            self.ids.bomb.pos = (Window.width/5+3*Window.width/5/3)+3*Window.width/5/4.4 , Window.height/27.69

            jolt_bool = False
            jolt_index = 9
            self.ids.jolt.pos = (Window.width/5+3*Window.width/5/3)+3*Window.width/5/2.75 , Window.height/27.69

            swordman.cd = swordman.original_cd
            ion.cd = ion.original_cd
            apex.cd = apex.original_cd
            blade.cd = blade.original_cd
            tank.cd = tank.original_cd
            bomb.cd = bomb.original_cd
            jolt.cd = jolt.original_cd

            self.ids.swordmanCD.text = str(swordman.cd)
            self.ids.ionCD.text = str(ion.cd)
            self.ids.apexCD.text = str(apex.cd)
            self.ids.bladeCD.text = str(blade.cd)
            self.ids.tankCD.text = str(tank.cd)
            self.ids.bombCD.text = str(bomb.cd)
            self.ids.joltCD.text = str(jolt.cd)
             
            
            O_swordman_summon = False
            O_swordman_index = 9
            self.ids.O_swordman.pos = (Window.width/5+3*Window.width/5/6)+Window.width/28.2352941176 , Window.height-Window.height/6.1 

            O_ion_summon = False
            O_ion_index = 9
            self.ids.O_ion.pos = (Window.width/5+3*Window.width/5/6)+Window.width/10.3225806452 , Window.height-Window.height/6.1

            O_apex_summon = False
            O_apex_index = 9
            self.ids.O_apex.pos = (Window.width/5+3*Window.width/5/6)+Window.width/6.31578947368 , Window.height-Window.height/6.1

            O_blade_summon = False
            O_blade_index = 9
            self.ids.O_blade.pos = (Window.width/5+3*Window.width/5/6)+Window.width/4.54976303318 , Window.height-Window.height/6.1

            O_tank_summon = False
            O_tank_index = 9
            self.ids.O_tank.pos = (Window.width/5+3*Window.width/5/6)+Window.width/19.6923076923 , Window.height-Window.height/12.1

            O_bomb_summon = False
            O_bomb_index = 9
            self.ids.O_bomb.pos = (Window.width/5+3*Window.width/5/6)+Window.width/7.83673469388 , Window.height-Window.height/12.1

            O_jolt_summon = False
            O_jolt_index =  9 
            self.ids.O_jolt.pos = (Window.width/5+3*Window.width/5/6)+Window.width/4.89171974522 , Window.height-Window.height/12.1

            self.ids.core1.source = r"C:\Users\salam\OneDrive\Desktop\Visual studio\Images\card_sleeve.png"
            self.ids.core2.source = r"C:\Users\salam\OneDrive\Desktop\Visual studio\Images\card_sleeve.png"
            self.ids.core3.source = r"C:\Users\salam\OneDrive\Desktop\Visual studio\Images\card_sleeve.png"

            self.ids.O_core1.source = r"C:\Users\salam\OneDrive\Desktop\Visual studio\Images\card_sleeve.png"
            self.ids.O_core2.source = r"C:\Users\salam\OneDrive\Desktop\Visual studio\Images\card_sleeve.png"
            self.ids.O_core3.source = r"C:\Users\salam\OneDrive\Desktop\Visual studio\Images\card_sleeve.png"

            Game_Over = Label(text="[b][color=ff3333]Game Over[/color][/b]", font_size=Window.width/10, markup = True)
            Game_Over.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
            self.add_widget(Game_Over)


            for row in opponent_list:
                row.alive = True
            for row in player_list:
                row.alive = True
            Clock.schedule_once(lambda dt: self.remove_widget(Game_Over), 3)
            Clock.schedule_once(lambda dt: App.get_running_app().stop(), 3)

# win 
        global opponent_life
        if opponent_life == 2:
            self.ids.O_H1.pos = -self.ids.O_H1.size[0],-self.ids.O_H1.size[1]
        elif opponent_life == 1:
            self.ids.O_H2.pos = -self.ids.O_H2.size[0],-self.ids.O_H2.size[1]
        elif opponent_life <= 0:
            opponent_life = 3
            self.ids.O_H1.pos = Window.width/1.09756097561 - self.ids.O_H1.size[0], Window.height - self.ids.O_H1.size[1] 
            self.ids.O_H2.pos = Window.width/1.09756097561 - self.ids.O_H2.size[0], Window.height - 2*self.ids.O_H2.size[1] 
            player_life = 3
            self.ids.H1.pos = Window.width/1.09756097561 - self.ids.H1.size[0], 2*self.ids.H1.size[1] 
            self.ids.H2.pos = Window.width/1.09756097561 - self.ids.H2.size[0], self.ids.H2.size[1] 
            stage += 1
            self.ids.stage_counter.text = str(stage)
            for row in opponent_list:
                row.atk = row.original_atk_stage_0 + stage
                row.hp = row.original_hp_stage_0 + stage
                row.spd = row.original_spd_stage_0 + int(stage/3)
                if row.original_cd_stage_0 > 1:
                    row.cd = row.original_cd_stage_0 - int(stage/5)
                else:
                    row.cd += 1
            draw_per_turn = 4
            rest_spot.clear()         
            for row in player_list:
                rest_spot.append(row)
            O_rest_spot.clear()
            for row in opponent_list:
                O_rest_spot.append(row)
            for row in right_lane:
                if row != "x":
                    right_lane.insert(right_lane.index(row), "x")
                    right_lane.remove(row)
            for row in mid_lane:
                if row != "x":
                    mid_lane.insert(mid_lane.index(row), "x")
                    mid_lane.remove(row)
            for row in left_lane:
                if row != "x":
                    left_lane.insert(left_lane.index(row), "x")
                    left_lane.remove(row)
            for row in core:
                if row != "x":
                    core.insert(core.index(row), "x")
                    core.remove(row)
            for row in O_core:
                if row != "x":
                    O_core.insert(O_core.index(row), "x")
                    O_core.remove(row)
            if player.stored[0] != "x":
                player.use_card(player.stored[0])
            if player.stored[1] != "x":
                player.use_card(player.stored[1])
            if player.stored[2] != "x":
                player.use_card(player.stored[2])
            if player.stored[3] != "x":
                player.use_card(player.stored[3])
            player.shuffle()
            self.ids.hand_one.source = r"C:\Users\salam\OneDrive\Desktop\Visual studio\Images\card_sleeve.png"
            self.ids.hand_two.source = r"C:\Users\salam\OneDrive\Desktop\Visual studio\Images\card_sleeve.png"
            self.ids.hand_three.source = r"C:\Users\salam\OneDrive\Desktop\Visual studio\Images\card_sleeve.png"
            self.ids.hand_four.source = r"C:\Users\salam\OneDrive\Desktop\Visual studio\Images\card_sleeve.png"



            swordman_bool = False
            swordman_index = 9
            self.ids.swordman.pos = (Window.width/5+3*Window.width/5/3)+3*Window.width/5/15.88 , Window.height/8.5

            ion_bool = False
            ion_index = 9
            self.ids.ion.pos = (Window.width/5+3*Window.width/5/3)+3*Window.width/5/5.8 , Window.height/8.5
        
            apex_bool = False
            apex_index = 9
            self.ids.apex.pos = (Window.width/5+3*Window.width/5/3)+3*Window.width/5/3.55 , Window.height/8.5

            blade_bool = False
            blade_index = 9
            self.ids.blade.pos = (Window.width/5+3*Window.width/5/3)+3*Window.width/5/2.559 , Window.height/8.5   

            tank_bool = False
            tank_index = 9
            self.ids.tank.pos = (Window.width/5+3*Window.width/5/3)+3*Window.width/5/11 , Window.height/27.69

            bomb_bool = False
            bomb_index = 9
            self.ids.bomb.pos = (Window.width/5+3*Window.width/5/3)+3*Window.width/5/4.4 , Window.height/27.69

            jolt_bool = False
            jolt_index = 9
            self.ids.jolt.pos = (Window.width/5+3*Window.width/5/3)+3*Window.width/5/2.75 , Window.height/27.69

            swordman.cd = swordman.original_cd
            ion.cd = ion.original_cd
            apex.cd = apex.original_cd
            blade.cd = blade.original_cd
            tank.cd = tank.original_cd
            bomb.cd = bomb.original_cd
            jolt.cd = jolt.original_cd

            self.ids.swordmanCD.text = str(swordman.cd)
            self.ids.ionCD.text = str(ion.cd)
            self.ids.apexCD.text = str(apex.cd)
            self.ids.bladeCD.text = str(blade.cd)
            self.ids.tankCD.text = str(tank.cd)
            self.ids.bombCD.text = str(bomb.cd)
            self.ids.joltCD.text = str(jolt.cd)
             
            
            O_swordman_summon = False
            O_swordman_index = 9
            self.ids.O_swordman.pos = (Window.width/5+3*Window.width/5/6)+Window.width/28.2352941176 , Window.height-Window.height/6.1 

            O_ion_summon = False
            O_ion_index = 9
            self.ids.O_ion.pos = (Window.width/5+3*Window.width/5/6)+Window.width/10.3225806452 , Window.height-Window.height/6.1

            O_apex_summon = False
            O_apex_index = 9
            self.ids.O_apex.pos = (Window.width/5+3*Window.width/5/6)+Window.width/6.31578947368 , Window.height-Window.height/6.1

            O_blade_summon = False
            O_blade_index = 9
            self.ids.O_blade.pos = (Window.width/5+3*Window.width/5/6)+Window.width/4.54976303318 , Window.height-Window.height/6.1

            O_tank_summon = False
            O_tank_index = 9
            self.ids.O_tank.pos = (Window.width/5+3*Window.width/5/6)+Window.width/19.6923076923 , Window.height-Window.height/12.1

            O_bomb_summon = False
            O_bomb_index = 9
            self.ids.O_bomb.pos = (Window.width/5+3*Window.width/5/6)+Window.width/7.83673469388 , Window.height-Window.height/12.1

            O_jolt_summon = False
            O_jolt_index = 9
            self.ids.O_jolt.pos = (Window.width/5+3*Window.width/5/6)+Window.width/4.89171974522 , Window.height-Window.height/12.1

            self.ids.core1.source = r"C:\Users\salam\OneDrive\Desktop\Visual studio\Images\card_sleeve.png"
            self.ids.core2.source = r"C:\Users\salam\OneDrive\Desktop\Visual studio\Images\card_sleeve.png"
            self.ids.core3.source = r"C:\Users\salam\OneDrive\Desktop\Visual studio\Images\card_sleeve.png"

            self.ids.O_core1.source = r"C:\Users\salam\OneDrive\Desktop\Visual studio\Images\card_sleeve.png"
            self.ids.O_core2.source = r"C:\Users\salam\OneDrive\Desktop\Visual studio\Images\card_sleeve.png"
            self.ids.O_core3.source = r"C:\Users\salam\OneDrive\Desktop\Visual studio\Images\card_sleeve.png"

            

#########################################################################################################################################
# show updated stats of player
        self.ids.swordmanATK.text = str(swordman.atk)
        self.ids.swordmanHP.text = str(swordman.hp)
        self.ids.swordmanSPD.text = str(swordman.spd)
        self.ids.ionATK.text = str(ion.atk)
        self.ids.ionHP.text = str(ion.hp)
        self.ids.ionSPD.text = str(ion.spd)
        self.ids.apexATK.text = str(apex.atk)
        self.ids.apexHP.text = str(apex.hp)
        self.ids.apexSPD.text = str(apex.spd)
        self.ids.bladeATK.text = str(blade.atk)
        self.ids.bladeHP.text = str(blade.hp)
        self.ids.bladeSPD.text = str(blade.spd)
        self.ids.tankATK.text = str(tank.atk)
        self.ids.tankHP.text = str(tank.hp)
        self.ids.tankSPD.text = str(tank.spd)
        self.ids.bombATK.text = str(bomb.atk)
        self.ids.bombHP.text = str(bomb.hp)
        self.ids.bombSPD.text = str(bomb.spd)
        self.ids.joltATK.text = str(jolt.atk)
        self.ids.joltHP.text = str(jolt.hp)
        self.ids.joltSPD.text = str(jolt.spd)
#########################################################################################################################################
# show updated stats of opponent
        self.ids.O_swordmanATK.text = str(O_swordman.atk)
        self.ids.O_swordmanHP.text = str(O_swordman.hp)
        self.ids.O_swordmanSPD.text = str(O_swordman.spd)
        self.ids.O_swordmanCD.text = str(O_swordman.cd)
        self.ids.O_ionATK.text = str(O_ion.atk)
        self.ids.O_ionHP.text = str(O_ion.hp)
        self.ids.O_ionSPD.text = str(O_ion.spd)
        self.ids.O_ionCD.text = str(O_ion.cd)
        self.ids.O_apexATK.text = str(O_apex.atk)
        self.ids.O_apexHP.text = str(O_apex.hp)
        self.ids.O_apexSPD.text = str(O_apex.spd)
        self.ids.O_apexCD.text = str(O_apex.cd)
        self.ids.O_bladeATK.text = str(O_blade.atk)
        self.ids.O_bladeHP.text = str(O_blade.hp)
        self.ids.O_bladeSPD.text = str(O_blade.spd)
        self.ids.O_bladeCD.text = str(O_blade.cd)
        self.ids.O_tankATK.text = str(O_tank.atk)
        self.ids.O_tankHP.text = str(O_tank.hp)
        self.ids.O_tankSPD.text = str(O_tank.spd)
        self.ids.O_tankCD.text = str(O_tank.cd)
        self.ids.O_bombATK.text = str(O_bomb.atk)
        self.ids.O_bombHP.text = str(O_bomb.hp)
        self.ids.O_bombSPD.text = str(O_bomb.spd)
        self.ids.O_bombCD.text = str(O_bomb.cd)
        self.ids.O_joltATK.text = str(O_jolt.atk)
        self.ids.O_joltHP.text = str(O_jolt.hp)
        self.ids.O_joltSPD.text = str(O_jolt.spd)
        self.ids.O_joltCD.text = str(O_jolt.cd)
#########################################################################################################################################



class with_pic_mainApp(App):
    def build(self):
        self.width = Window.width
        self.height = Window.height
        return game_board()

if __name__ == '__main__':
    with_pic_mainApp().run()


