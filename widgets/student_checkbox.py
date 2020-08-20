import tkinter as tk
from styles import *

class Student_Checkbox(tk.Frame):
    def __init__(self, master, student_name):
        #todo inherit from "CHECKBUTTON" and not ftom "FRAME"
        super().__init__(master, bg = dark_color)

        self.value = tk.IntVar()

        self.checkbox = tk.Checkbutton(self,
                                       bg = dark_color,
                                       selectcolor = white_color,
                                       activebackground = dark_color,
                                       activeforeground = "red",
                                       text = student_name,
                                       font = lower_button_font(self),
                                       fg = white_color,
                                       command = lambda: self._change_color(),
                                       variable = self.value
                                       )
        self.checkbox.pack(side = "left", padx = margin, pady = margin)

    def _change_color(self):
        if self.value.get() == 1 :
            self.checkbox["fg"] = "red"
        else :
            self.checkbox["fg"] = white_color
    def deselect(self):
        self.checkbox.deselect()
        self.checkbox["fg"] = white_color
    def colocar(self):
        self.pack(fill="x", expand = True)