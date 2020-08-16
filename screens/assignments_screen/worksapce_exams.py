import tkinter as tk
from styles import *

class Workspace_Exams(tk.Frame):
    def __init__(self, master, margin, controller):
        super().__init__(master, bg = dark_color)

        f = tk.LabelFrame(self,
                          text = "Exams",
                          font = label_frame_font(self),
                          fg =white_color,
                          bg = dark_color,
                          borderwidth = frame_width,
                          height = 471-margin*2,
                          width =1000 - (300 + margin * 3)
                          )
        f.pack()

        b = tk.Button(self,
                      text = "Go to assitance",
                      font = lower_button_font(self),
                      fg = white_color,
                      activeforeground = white_color,
                      bg = light_color,
                      activebackground = light_color,
                      borderwidth = button_width,
                      command = lambda : controller.show_workspace("Workspace_Assistance")
                      )
        b.pack(fill="x", side = "bottom", pady = margin)