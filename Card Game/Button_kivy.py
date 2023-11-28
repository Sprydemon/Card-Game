# import kivy module
import kivy

# this restrict the kivy version i.e
# below this kivy version you cannot
# use the app or software
kivy.require("1.9.1")

# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App

# creates the button in kivy
# if not imported shows the error
from kivy.uix.button import Button

# class in which we are creating the button
class ButtonApp(App):
	
    def build(self):
		# use a (r, g, b, a) tuple
        btn = Button(text ="Push Me !",
				font_size ="20sp",
				background_color =(1, 1, 1, 1),
				color =(1, 1, 1, 1), 
				size =(32, 32),
				size_hint =(.2, .2),
				pos =(300, 250))

        return btn
	


# creating the object root for ButtonApp() class 
root = ButtonApp()

# run function runs the whole program
# i.e run() method which calls the
# target function passed to the constructor.
root.run()
