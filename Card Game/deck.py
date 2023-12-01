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
player_deck = []



class Hand:
    stored = []
    def __init__(self, deck):
        self.deck = deck
        self.stored = []

    def draw(self):
        if len(self.stored) < 4:
            self.stored.append(self.deck[0])
            self.deck.pop(0)

    def start(self):
        self.draw()
        self.draw()
        self.draw()
        self.draw()

    def use_card(self, used_card):
        self.deck.append(used_card)
        self.stored.remove(used_card)

    def shuffle(self):
        cards_num = len(deck) - 1
        deck_copy = deck.copy()
        while cards_num >= 0:
            rearrange = random.randint(0, cards_num)
            self.deck.append(deck_copy[rearrange])
            deck_copy.pop(rearrange)
            cards_num -= 1

player = Hand(player_deck)

print(player.shuffle)
print(player.start)

