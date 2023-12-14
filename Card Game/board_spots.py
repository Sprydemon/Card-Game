from PIL import Image
import deck

attack = "Card Game\Images\+1 attack.png"
attack2 = "Card Game\Images\+2 attack.png"
attack3 = "Card Game\Images\+3 attack.png"

health = "Card Game\Images\+1 health.png"
health2 = "Card Game\Images\+2 health.png"
health3 = "Card Game\Images\+3 health.png"

speed = "Card Game\Images\+1 speed.png"
speed2 = "Card Game\Images\+2 speed.png"

hop = "Card Game\Images\hop over.png" 
dec_cooldown = "Card Game\Images\-1 cooldown.png"
inc_cooldown = "Card Game\Images\+1 cooldown.png"
move = "Card Game\Images\move.png"

# Player spots

player_core_zone = ["x", "x", "x"]
player_character_zone = ["x", "x", "x", "x", "x", "x", "x"]

# opponent spots

oponent_core_zone = ["x", "x", "x"]
opponent_character_zone = ["x", "x", "x", "x", "x", "x", "x"]

# board spots

row_left = ["x", "x", "x", "x", "x", "x", "x", "x"]

row_mid = ["x", "x", "x", "x", "x", "x", "x", "x"]

row_right = ["x", "x", "x", "x", "x", "x", "x", "x"]

# hand

player_hand = ["x", "x", "x", "x"]
opponent_hand = ["x", "x", "x", "x"]

def core_zone(character_zone, core, added_card):
    if core[-1] == "x":
        core.pop(-1)
        core.insert(0, added_card)
    else:
        character_zone.append(core(-1))
        core.pop(-1)
        core.insert(0, added_card)

def display_card(array):
    for row in array:
        if row != "x":
            png = Image.open(row)
            png.show()


