import random 
from PIL import Image

attack = r"Card Game\Images\+1 attack.png"
attack2 = r"Card Game\Images\+2 attack.png"
attack3 = r"Card Game\Images\+3 attack.png"

health = r"Card Game\Images\+1 health.png"
health2 = r"Card Game\Images\+2 health.png"
health3 = r"Card Game\Images\+3 health.png"

speed = r"Card Game\Images\+1 speed.png"
speed2 = r"Card Game\Images\+2 speed.png"

hop = r"Card Game\Images\hop over.png" 
dec_cooldown = r"Card Game\Images\-1 cooldown.png"
inc_cooldown = r"Card Game\Images\+1 cooldown.png"
move = r"Card Game\Images\move.png"

card_list = [attack, attack2, attack3, health, health2, health3, speed, speed2, attack, attack2, attack3, health, health2, health3, speed, speed2, hop, dec_cooldown, inc_cooldown, move]
player_deck = card_list.copy()


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

player = Hand(player_deck)
player.shuffle()


