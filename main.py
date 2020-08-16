import tkinter as tk
from styles import *
from screens.assignments_screen.assignments_screen import Assignments_Screen

class Easy2English(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.iconbitmap("assets/logo.ico")
        self.title("Easy2English")
        self.geometry("1000x500")
        self.configure(bg = dark_color)
        self.resizable(0,0)

app = Easy2English()
firstScreen = Assignments_Screen(app)
firstScreen.pack()
app.mainloop()