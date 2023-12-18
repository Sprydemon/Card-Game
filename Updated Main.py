from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.button import Button
from TitleScreen import TitleScreen
from InstructionsScreen import InstructionsScreen
from OptionsScreen import OptionsScreen

class Card:
    def __init__(self, Attack, Health, Movement):
        self.Attack = Attack
        self.Health = Health
        self.max_health = Health
        self.Movement = Movement
        self.is_alive = True
        self.current_position = (0, 0)  #start position of card on the game board

    def move(self, new_position, other_card):
        #check to see if the movement is within the allowed range based on grid distance.
        if self.determine_position(new_position) <= self.Movement and self.is_valid_position(new_position):
            if not self.is_occupied(new_position, other_card):
                self.current_position = new_position
                self.Movement -= self.determine_position(new_position)  #Reduce movements left
            else:
                #If the position is occupied, perform an attack on the occupying card
                enemy_card = self.get_occupied_card(new_position, other_card)
                if enemy_card:
                    self.attack_enemy(enemy_card)

    def attack_enemy(self, enemy_card):
     #Check if the enemy card is within attack range
        if self.determine_position(enemy_card.current_position) <= self.attack_range:
            #Deal damage to the enemy card
            enemy_card.receive_damage(self.Attack)

    def receive_damage(self, damage, core_zone):
        #Reduce health points based on the damage received
        self.Health -= damage
        if self.Health <= 0:
            #Handle card death (move to cor zone)
            self.is_alive = False
            self.move_to_core_zone(core_zone)

    def move_to_core_zone(self, core_zone):
        core_zone.push_card(self)

    def revive(self):
        #Reviving card
        self.Health = self.max_health
        self.is_alive = True

    def determine_position(self, new_position):
        x1, y1 = self.current_position
        x2, y2 = new_position
        return abs(x2 - x1) + abs(y2 - y1)
    
    def is_valid_position(self, position):
        #Check if position is within the board's bounds (assuming a 5x5 board)
        x, y = position
        return 0 <= x <= 4 and 0 <= y <= 4

    def is_occupied(self, position, other_card):
        #Check if the position is already occupied by another card
        return any(card.current_position == position for card in other_card)

    def get_occupied_card(self, position, other_card):
        #Get info of card occupying a specified position
        for card in other_card:
            if card.current_position == position:
                return card
        return None
    
    def attack_enemy_player(self, enemy_player):
        #Check if the enemy player is in range and deal damage directly to the player's healh while on-
        #- a specific grind
        if self.current_position == (2, 4):  #example position for triggering attack
            enemy_player.receive_damage(self.attack)
    
class CoreZone:
    def __init__(self):
        self.bottom = None
        self.middle = None
        self.top = None

    def push_card(self, card):
        if self.bottom is None:
            self.bottom = card
        elif self.middle is None:
            self.middle = self.bottom
            self.bottom = card
        else:
            self.top = self.middle
            self.middle = self.bottom
            self.bottom = card
            self.revive_top_card()

    def revive_top_card(self):
        if self.top:
            self.top.revive()
            self.top = None
    
class Player:
    def __init__(self, name, Health):
        self.name = name
        self.Health = Health
        self.cards = []  #Player's cards in the game
        self.is_winner = None
        self.game_app = None  # Initialize game_app attribute
        self.is_winner = None

    def receive_damage(self, damage):
        self.Health -= damage
        if self.Health <= 0:
            self.is_winner = False  
            self.on_player_loses()

    def on_player_loses(self):
        if self.game_app:
            self.game_app.on_player_loses()

class GameScreen(Screen):
    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        
class GameApp(App):
    def build(self):
        screen_manager = ScreenManager()
        self.player = Player()
        self.player.game_app = self

        title_screen = TitleScreen(name="title_screen")
        game_screen = GameScreen(name="game_screen")
        options_screen = OptionsScreen(name="options_screen")
        instructions_screen = InstructionsScreen(name="instructions_screen")
        end_screen = TitleScreen(name="end_screen")

        screen_manager.add_widget(title_screen)
        screen_manager.add_widget(game_screen)
        screen_manager.add_widget(options_screen)
        screen_manager.add_widget(instructions_screen)
        screen_manager.add_widget(end_screen)

        return screen_manager

    def on_player_loses(self):
        self.screen_manager.current = "end_screen"

if __name__ == '__main__':
    GameApp().run()
