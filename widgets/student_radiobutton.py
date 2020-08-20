import tkinter as tk
from styles import *

class Student_RadioButton(tk.Radiobutton):
    def __init__(self, master, student_name, variable, id, command = None, *args, **kwargs):
        super().__init__(master,
                         text = student_name,
                         font = lower_button_font(master),
                         fg = white_color,
                         activeforeground = light_color,
                         selectcolor = white_color,
                         bg = dark_color,
                         activebackground = dark_color,
                         variable = variable,
                         value = id,
                         command = command,
                         *args, **kwargs)

        self.white_color = white_color
        self.light_color = light_color
        self.variable = variable
        self.variable.trace("w", self._change_fg)

    def _change_fg(self, *args):
        if self["value"] == self.variable.get():
            self["fg"] = light_color
        else: self["fg"] = white_color

    def colocar(self):
        self.pack(fill = "x", expand = True, pady = margin/2)