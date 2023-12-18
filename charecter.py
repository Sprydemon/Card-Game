class Charecter:
    def __init__(self, atk, hp, spd, cd, team, source):
        self.atk = atk
        self.hp = hp
        self.original_hp = hp
        self.spd = spd
        self.original_spd = spd
        self.cd = cd
        self.original_cd = cd
        self.team = team
        self.index = 0
        self.lane = "none"
        self.alive = True
        self.did_change_lane = False
        self.source = source

    def cooldown(self):
        self.cd -= 1

    

    
    