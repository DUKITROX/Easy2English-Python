import tkinter as tk
from styles import *

class Student_Checkbox(tk.Frame):
    def __init__(self, master, student_name):
        super().__init__(master, bg = dark_color)

        self.value = tk.IntVar()

        self.checkbox = tk.Checkbutton(self,
                                       bg = dark_color,
                                       selectcolor = white_color,
                                       activebackground = dark_color,
                                       activeforeground = light_color,
                                       text = student_name,
                                       font = lower_button_font(self),
                                       fg = white_color,
                                       command = lambda: self.change_color(),
                                       variable = self.value
                                       )
        self.checkbox.pack(side = "left", padx = margin, pady = margin)

    def change_color(self):
        if self.value.get() == 1 :
            self.checkbox["fg"] = light_color
        else :
            self.checkbox["fg"] = white_color

    def colocar(self):
        self.pack(fill="x", expand = 1)