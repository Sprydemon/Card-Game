from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.button import Button
from kivy.uix.label import Label

class InstructionsScreen(Screen):
    def __init__(self, **kwargs):
        super(InstructionsScreen, self).__init__(**kwargs)
        return_button = Button(text='Return to Main Menu', size_hint=(None, None), size=(200, 50))
        return_button.bind(on_press=self.return_to_main_menu)
        return_button.pos_hint = {'center_x': 0.5, 'center_y': 0.06}
        self.add_widget(return_button)

        Instructions_Title = Label(text='Intructions:', font_size='50sp')
        Instructions_Title.pos_hint = {'x': -0.4, 'y': 0.44}
        Instructions_Title.color = (1, 1, 1)
        self.add_widget(Instructions_Title)


        Instructions_Label = Label(text="Seige is a turn based card game. The game is endless and countinues until you lose. Difficulty increases eveytime you", font_size='26sp')
        Instructions_Label.pos_hint = {'x': 0.0, 'y': 0.35}
        Instructions_Label.color = (1, 1, 1)
        self.add_widget(Instructions_Label)

        Instructions_Label = Label(text="win. To move onto the next stage, you need defeat the opponent. This is one by destroying all three of opponet A.I's hearts.", font_size='25sp')
        Instructions_Label.pos_hint = {'x': 0.0, 'y': 0.30}
        Instructions_Label.color = (1, 1, 1)
        self.add_widget(Instructions_Label)

        Instructions_Label = Label(text="The opponent's hearts are destroyed by moving one of your cards to the red spots on the opposite side of the board. The red", font_size='25sp')
        Instructions_Label.pos_hint = {'x': 0.0, 'y': 0.25}
        Instructions_Label.color = (1, 1, 1)
        self.add_widget(Instructions_Label)

        Instructions_Label = Label(text="tiles are places where you can directly attack the opponent rather than its cards. However, The opponent's cards can be", font_size='25sp')
        Instructions_Label.pos_hint = {'x': 0.0, 'y': 0.20}
        Instructions_Label.color = (1, 1, 1)
        self.add_widget(Instructions_Label)

        Instructions_Label = Label(text="attacked anywhere on the board. The opponent can aslo attack you with the same logic. Your cards are given to on your", font_size='25sp')
        Instructions_Label.pos_hint = {'x': 0.0, 'y': 0.15}
        Instructions_Label.color = (1, 1, 1)
        self.add_widget(Instructions_Label)

        Instructions_Label = Label(text="deck and can be moved by tapping on them. Tap on the top to move forward, and tap on the bottom to move back. For spots", font_size='25sp')
        Instructions_Label.pos_hint = {'x': 0.0, 'y': 0.1}
        Instructions_Label.color = (1, 1, 1)
        self.add_widget(Instructions_Label)

        Instructions_Label = Label(text="where you can move left or right, tap on the corresponding side next to card rather than the card itself. The card's cooldown", font_size='25sp')
        Instructions_Label.pos_hint = {'x': 0.0, 'y': 0.05}
        Instructions_Label.color = (1, 1, 1)
        self.add_widget(Instructions_Label)

        Instructions_Label = Label(text="should be zero. The cooldown is given below the card on your deck. Cooldown decreases every turn. The cards also have an ", font_size='25sp')
        Instructions_Label.pos_hint = {'x': 0.0, 'y': 0.0}
        Instructions_Label.color = (1, 1, 1)
        self.add_widget(Instructions_Label)

        Instructions_Label = Label(text="attack stat (given in red), health (given in green), and speed (given in black) all on the card. Health is its hit points. Speed", font_size='25sp')
        Instructions_Label.pos_hint = {'x': 0.0, 'y': -0.05}
        Instructions_Label.color = (1, 1, 1)
        self.add_widget(Instructions_Label)

        Instructions_Label = Label(text="is the number of times it can move in one turn. Attack is the damage dealt to the opponent card. If attack exceedes the ", font_size='25sp')
        Instructions_Label.pos_hint = {'x': 0.0, 'y': -0.1}
        Instructions_Label.color = (1, 1, 1)
        self.add_widget(Instructions_Label)

        Instructions_Label = Label(text="opposing card's heatlh then that card dies and is sent to the core zone next to the deck. When three cards enter the core zone,", font_size='25sp')
        Instructions_Label.pos_hint = {'x': 0.0, 'y': -0.15}
        Instructions_Label.color = (1, 1, 1)
        self.add_widget(Instructions_Label)

        Instructions_Label = Label(text="the entry of a fourth card will card will trigger the revival of the first card to have died. It wil then be re-added to the player's", font_size='25sp')
        Instructions_Label.pos_hint = {'x': 0.0, 'y': -0.2}
        Instructions_Label.color = (1, 1, 1)
        self.add_widget(Instructions_Label)

        Instructions_Label = Label(text="deck. There also exists a draw system on the deck which can be used to obtain various boosts. These boosts are applied by ", font_size='25sp')
        Instructions_Label.pos_hint = {'x': 0.0, 'y': -0.25}
        Instructions_Label.color = (1, 1, 1)
        self.add_widget(Instructions_Label)

        Instructions_Label = Label(text="dragging them onto a card. Boosts can be drawn four times on the start of the first turn and then only once for the rest of", font_size='25sp')
        Instructions_Label.pos_hint = {'x': 0.0, 'y': -0.3}
        Instructions_Label.color = (1, 1, 1)
        self.add_widget(Instructions_Label)

        Instructions_Label = Label(text="the turn. Only four boosts can be held at at a time. The boosts include increase in attack, speed, health and more.", font_size='25sp')
        Instructions_Label.pos_hint = {'x': 0.0, 'y': -0.35}
        Instructions_Label.color = (1, 1, 1)
        self.add_widget(Instructions_Label)


    def return_to_main_menu(self, instance):
        self.manager.current = "title_screen"
