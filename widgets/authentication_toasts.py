import tkinter as tk
from styles import *

class Authentication_Toasts(tk.Frame):
    def __init__(self, master, error):
        super().__init__(master, bg = light_color)

        l = tk.Label(self, text = f"  {error}  ", bg = dark_color, font = lower_button_font(master), fg = white_color)
        l.pack(fill="both", expand = True, padx = 1, pady = 1)

        self.after(2000, func=self.destroy)

    def colocar(self):
        self.place(relx = 0.5, rely = 0.825, anchor = "center",  height = 35)