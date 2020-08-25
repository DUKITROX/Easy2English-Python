import tkinter as tk
from styles import *

class Student_RadioButton(tk.Frame):
    def __init__(self, master, student_name, variable, id, command = None, *args, **kwargs):
        super().__init__(master, bg = dark_color)
        self.radiobutton = tk.Radiobutton(self,
                         text = student_name,
                         font = lower_button_font(self),
                         fg = white_color,
                         activeforeground = light_color,
                         selectcolor = white_color,
                         bg = dark_color,
                         activebackground = dark_color,
                         variable = variable,
                         value = id,
                         command = command,
                         *args, **kwargs)
        self.radiobutton.pack(fill="x", side = "left")

        self.white_color = white_color
        self.light_color = light_color
        self.variable = variable
        self.variable.trace("w", self._change_fg)

    def _change_fg(self, *args):
        if self.radiobutton["value"] == self.variable.get():
            self.radiobutton["fg"] = light_color
        else: self.radiobutton["fg"] = white_color

    def colocar(self):
        self.pack(fill = "x", expand = True, pady = margin/2)