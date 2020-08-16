import tkinter as tk
from styles import *

class Homework_Entry(tk.Text):
    def __init__(self, master):
        super().__init__(master,
                         bg = dark_color,
                         bd = 0,
                         font = lower_button_font(master),
                         fg = white_color,
                         insertbackground = light_color,
                         selectbackground = light_color,
                         wrap = "word",
                         )
        #super().bind("<FocusIn>", lambda event: self._clear_placeholder())
        #super().bind("<Leave>", lambda event: self._add_placeholder())
    def _add_placeholder(self):
        if super().get() == None:
            self["fg"] = light_white_color
            super().insert("0.0", "Homework...")
    def _clear_placeholder(self):
        self["fg"] = white_color
        super().delete("0.0","end")

    def colocar(self):
        self.place(x = margin, y = margin, height = 135-margin*2, width = 1000 - (300 + margin * 6))