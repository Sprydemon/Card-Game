from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
from kivy.uix.button import Button


class OptionsScreen(Screen):
    def __init__(self, **kwargs):
        super(OptionsScreen, self).__init__(**kwargs)
        return_button = Button(text='Return to Main Menu', size_hint=(None, None), size=(200, 50))
        return_button.bind(on_press=self.return_to_main_menu)
        return_button.pos_hint = {'center_x': 0.14, 'center_y': 0.06}
        self.add_widget(return_button)

        #add options here

    def return_to_main_menu(self, instance):
        self.manager.current = "title_screen"  #navigates back to the title screen