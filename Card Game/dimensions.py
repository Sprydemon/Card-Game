from tkinter import *

screen_width = Tk().winfo_screenwidth()
screen_height = Tk().winfo_screenheight()
screen_width_kv = (Tk().winfo_screenwidth())*1.5
screen_height_kv = (Tk().winfo_screenheight())*1.5
board_width = int((screen_width/1.777)*1.5)
board_height = int(screen_height*1.5)
board_width_pos = (screen_width_kv - board_width)/2
