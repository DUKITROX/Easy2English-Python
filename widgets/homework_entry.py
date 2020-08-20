import tkinter as tk
from styles import *

class Homework_Entry(tk.Text):
    def __init__(self, master):
        super().__init__(master,
                         bg = dark_color,
                         bd = 0,
                         font = lower_button_font(master),
                         fg = light_white_color,
                         insertbackground = light_color,
                         selectbackground = light_color,
                         wrap = "word",
                         )
        self.on_placeholder = True
        super().insert("0.0", "Homework...")
        super().bind("<FocusIn>",  self._clear_placeholder)
        super().bind("<FocusOut>", self._add_placeholder)

    def _clear_placeholder(self, event):
        if self["fg"] == light_white_color:
            super().delete("0.0","end")
            self["fg"] = white_color
            self.on_placeholder = False

    def _add_placeholder(self, event):
        a = super().get("0.0", "end")
        if a.strip() == "":
            self["fg"] = light_white_color
            super().insert("0.0", "Homework...")
            self.on_placeholder = True

    def clear(self):
        if not self.on_placeholder:
            super().delete("0.0","end")

    def colocar(self):
        self.place(x = margin, y = margin, height = 135-margin*2, width = 1000 - (300 + margin * 6))