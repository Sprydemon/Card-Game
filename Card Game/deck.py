import random 

attack = "atk"
attack2 = "atk2"
attack3 = "atk3"

health = "hp"
health2 = "hp2"
health3 = "hp3"

speed = "spd"
speed2 = "spd2"

hop = "hop" 
dec_cooldown = "decrease cooldown"
inc_cooldown = "increase cooldown"
move = "move"

deck = [attack, attack2, attack3, health, health2, health3, speed, speed2, attack, attack2, attack3, health, health2, health3, speed, speed2, hop, dec_cooldown, inc_cooldown, move]
shuffled_deck = []
cards_num = len(deck) - 1

while cards_num > 0:
    print(cards_num)
    shuffle = random.randint(0, cards_num)
    shuffled_deck.append(deck[shuffle])
    deck.pop(shuffle)
    cards_num -= 1

class Hand:

    stored = []
    def __init__(self, shuffled_deck):
        self.shuffled_deck = shuffled_deck
        self.stored = []

    def draw(self):
        if len(self.stored) < 4:
            self.stored.append(self.shuffled_deck[0])
            self.shuffled_deck.pop(0)

    def start(self):
        self.draw()
        self.draw()
        self.draw()
        self.draw()

    def use_card(self, used_card):
        self.shuffled_deck.append(used_card)
        self.stored.remove(used_card)
        

player = Hand(shuffled_deck)

player.start()

print(player.shuffled_deck)
print(player.stored)