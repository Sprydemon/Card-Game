from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.clock import Clock

class TitleScreen(Screen):
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
        self.manager.current = "game_screen"

    def goto_options(self, instance):
        self.manager.current = "options_screen"

    def goto_instructions(self, instance):
        self.manager.current = "instructions_screen"

    def quit_game(self, instance):
        App.get_running_app().stop()


class EndScreen(TitleScreen):
    def __init__(self, **kwargs):
        super(EndScreen, self).__init__(**kwargs)
        game_over_label = Label(text="Game Over", font_size=40)
        game_over_label.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        self.add_widget(game_over_label)
        Clock.schedule_once(self.remove_game_over, 5)

    def remove_game_over(self, dt):
        self.remove_widget(self.game_over_label)
