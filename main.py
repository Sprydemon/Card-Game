from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.button import Button
from InstructionsScreen import InstructionsScreen
from OptionsScreen import OptionsScreen
from new_test import PongApp
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button

# class Card:
#     def __init__(self, Attack, Health, Movement):
#         self.Attack = Attack
#         self.Health = Health
#         self.Movement = Movement  
#         self.current_position = (0, 0)  #start position of card on the game board
#         self.is_alive = True

#     def move(self, new_position, other_card):
#         # Check if the movement is within the allowed range based on grid distance and handle collisions
#         if self.determine_position(new_position) <= self.Movement and self.is_valid_position(new_position):
#             if not self.is_occupied(new_position, other_card):
#                 self.current_position = new_position
#                 self.Movement -= self.determine_position(new_position)  # Reduce movement points
#             else:
#                 # If the position is occupied, perform an attack on the enemy card
#                 enemy_card = self.get_occupied_card(new_position, other_card)
#                 if enemy_card:
#                     self.attack_enemy(enemy_card)

#     def attack_enemy(self, enemy_card):
#      #Check if the enemy card is within attack range
#         if self.determine_position(enemy_card.current_position) <= self.attack_range:
#             #Deal damage to the enemy card
#             enemy_card.receive_damage(self.Attack)

#     def receive_damage(self, damage):
#         #Reduce health points based on the damage received
#         self.Health -= damage
#         if self.Health <= 0:
#             #handle card death
#             self.is_alive = False
#             self.destroy()

#     def determine_position(self, new_position):
#         x1, y1 = self.current_position
#         x2, y2 = new_position
#         return abs(x2 - x1) + abs(y2 - y1)
    
#     def is_valid_position(self, position):
#         # Check if the position is within the game board's bounds (assuming a 5x5 board)
#         x, y = position
#         return 0 <= x <= 4 and 0 <= y <= 4

#     def is_occupied(self, position, other_cards):
#         # Check if the position is already occupied by another card
#         return any(card.current_position == position for card in other_cards)

#     def get_occupied_card(self, position, other_cards):
#         # Get the card occupying the specified position
#         for card in other_cards:
#             if card.current_position == position:
#                 return card
#         return None
    
# class Player:
#     def __init__(self, name):
#         self.name = name
#         self.cards = []  #Player's cards in the game
#         self.is_winner = False  #Track if the player has won

#     def add_card(self, card):
#         self.cards.append(card)

#     def remove_card(self, card):
#         self.cards.remove(card)

#     def check_win_condition(self, opponent):
#         #If the opponent has no cards remaining, this player wins
#         if not opponent.cards:
#             self.is_winner = True
#             print(f"{self.name} wins the game!")

class GameScreen(Screen):
    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        
class TitleScreen(Screen):
    global run_game
    run_game = False
    def __init__(self, **kwargs):
        super(TitleScreen, self).__init__(**kwargs)
        image = Image(source='C:/Users/Shaha/Downloads/Yogino.jpg', keep_ratio=False, allow_stretch=True)
        self.add_widget(image)

        title_label = Label(text='Seige', font_size='50sp')
        title_label.pos_hint = {'x': 0.0, 'y': 0.25}
        title_label.color = (0, 0, 0) #RGBA format
        self.add_widget(title_label)

        start_button = Button(text='Start Game', size_hint=(None, None), size=(200, 50))
        start_button.bind(on_press=self.start_game)
        start_button.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        self.add_widget(start_button)

        options_button = Button(text='Options', size_hint=(None, None), size=(200, 50))
        options_button.bind(on_press=self.goto_options)
        options_button.pos_hint = {'center_x': 0.5, 'center_y': 0.3}
        self.add_widget(options_button)

        instructions_button = Button(text='Instructions', size_hint=(None, None), size=(200, 50))
        instructions_button.bind(on_press=self.goto_instructions)
        instructions_button.pos_hint =  {'center_x': 0.5, 'center_y': 0.4}
        self.add_widget(instructions_button)

        quit_button = Button(text='Quit Game', size_hint=(None, None), size=(200, 50))
        quit_button.bind(on_press=self.quit_game)
        quit_button.pos_hint = {'center_x': 0.5, 'center_y': 0.2}
        self.add_widget(quit_button)

    def start_game(self, instance):
        global run_game
        run_game = True
        App.get_running_app().stop()

    def goto_options(self, instance):
        self.manager.current = "options_screen"

    def goto_instructions(self, instance):
        self.manager.current = "instructions_screen"

    def quit_game(self, instance):
        App.get_running_app().stop()

class GameApp(App):
    def build(self):
        screen_manager = ScreenManager()

        title_screen = TitleScreen(name="title_screen")
        game_screen = GameScreen(name="game_screen")
        options_screen = OptionsScreen(name="options_screen")
        instructions_screen = InstructionsScreen(name="instructions_screen")

        screen_manager.add_widget(title_screen)
        screen_manager.add_widget(game_screen)
        screen_manager.add_widget(options_screen)
        screen_manager.add_widget(instructions_screen)

        return screen_manager

if __name__ == '__main__':
    while True:
        GameApp().run()
        print(run_game)
        if run_game == True:
            PongApp().run()
            run_game = False
        else:
            break

    