import tkinter as tk
from styles import *
from screens.assignments_screen.assignments_screen import Assignments_Screen
from screens.authentication_screen.authentication_screen import Authentication_Screen

class Easy2English(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.iconbitmap("assets/logo_icon.ico")
        self.title("Easy2English")
        self.geometry("1000x500")
        self.configure(bg = dark_color)
        self.resizable(0,0)

        self.screens = {}

        for screen in (Assignments_Screen, Authentication_Screen):
            screen_name = screen.__name__
            frame = screen(self)
            self.screens[screen_name] = frame
            frame.place(x=0, y=0, width = 1000, height = 500)
        self.show_screen("Authentication_Screen")
    def show_screen(self, screen):
        frame = self.screens[screen]
        frame.tkraise()

app = Easy2English()
app.mainloop()