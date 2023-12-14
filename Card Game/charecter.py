class Charecter:
    def __init__(self, atk, hp, spd, cd, team):
        self.atk = atk
        self.hp = hp
        self.spd = spd
        self.cd = cd
        self.team = team
        self.index = 1
        self.lane = "none"

    def cooldown(self):
        self.cd -= 1

    

    
    