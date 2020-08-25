import tkinter as tk
from styles import *

class Student_Checkbox(tk.Frame):
    def __init__(self, master, student_name, id, initial_value = True):
        #todo inherit from "CHECKBUTTON" and not ftom "FRAME"
        super().__init__(master, bg = dark_color)

        self.value = tk.BooleanVar()
        self.value.set(initial_value)
        initial_fg = white_color
        self.id = id
        if initial_value:
            initial_fg = white_color
        else: initial_fg = "red"

        self.checkbox = tk.Checkbutton(self,
                                       bg = dark_color,
                                       selectcolor = white_color,
                                       activebackground = dark_color,
                                       activeforeground = "red",
                                       text = student_name,
                                       font = lower_button_font(self),
                                       fg = initial_fg,
                                       command = lambda: self._change_color(),
                                       variable = self.value,
                                       onvalue = False,
                                       offvalue = True
                                       )
        self.checkbox.pack(side = "left", padx = margin, pady = margin)

    def _change_color(self):
        if self.value.get() == False :
            self.checkbox["fg"] = "red"
        else :
            self.checkbox["fg"] = white_color
    def deselect(self):
        self.checkbox.deselect()
        self.checkbox["fg"] = white_color
    def colocar(self):
        self.pack(fill="x", expand = True)