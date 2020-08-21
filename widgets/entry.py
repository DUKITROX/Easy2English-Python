import tkinter as tk
from styles import *

class Entry(tk.Entry):
    def __init__(self, master, placeholder, on_password, *args, **kwargs):
        super().__init__(master,
                         *args,
                         **kwargs,
                         width = 30,
                         bg = light_color,
                         bd = 10,
                         relief = "flat",
                         font = lower_button_font(master),
                         fg = light_white_color,
                         selectbackground = white_color,
                         selectforeground = light_color,
                         insertbackground = white_color
                         )
        self._on_placeholder = True
        self._on_password = on_password
        self.placeholder = placeholder

        super().bind("<FocusIn>", self._clear_placeholder)
        super().bind("<FocusOut>", self._add_placeholder)
        super().insert("0", self.placeholder)

    def _clear_placeholder(self, event):
        if self._on_placeholder:
            super().delete("0","end")
            self["fg"] = white_color
            self._on_placeholder = False
            if self._on_password: self["show"] = "*"
    def _add_placeholder(self, event):
        if not self.get():
            self["fg"] = light_white_color
            self["show"] = ""
            super().insert("0", self.placeholder)
            self._on_placeholder = True
    def clear(self):
        self.delete("0","end")
        self._add_placeholder(event = "")
    #todo implement placeholder with "command" instead of "FocusIn" or "FocusOut"