import tkinter as tk
import time
from styles import *

class Class_Button(tk.Frame):
    def __init__(self, master, level, schedule, id, controller, bg = light_color, fg = white_color):
        super().__init__(master, relief = "raised", borderwidth = button_width, bg = bg)
        self.id = id
        self.level = level
        self.schedule = schedule
        self.controller = controller

        self.bind("<Button-1>", lambda event : self._onPressed())
        self.bind("<ButtonRelease-1>", lambda event : self._onRelease())

        level_tag = tk.Label(self, text = f"- {level} -", justify = "left", bg = bg, fg = fg, font = upper_button_font(self))
        level_tag.pack()
        level_tag.bind("<Button-1>", lambda event : self._onPressed())
        level_tag.bind("<ButtonRelease-1>", lambda event : self._onRelease())

        schedule_tag = tk.Label(self, text = schedule, bg = bg, fg = fg, font = lower_button_font(self))
        schedule_tag.pack()
        schedule_tag.bind("<Button-1>", lambda event : self._onPressed())
        schedule_tag.bind("<ButtonRelease-1>", lambda event : self._onRelease())

    def _onPressed(self):
        self.configure(relief = "sunken")
        self.controller.get_students_info(id = self.id, level = self.level, schedule = self.schedule)

    def _onRelease(self):
        self.configure(relief = "raised")

    def colocar(self):
        self.pack(fill = "both", pady = 2, padx = 7)