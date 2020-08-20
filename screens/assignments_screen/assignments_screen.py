import tkinter as tk
from screens.assignments_screen.workspace_assitance import *
from screens.assignments_screen.worksapce_exams import *
from widgets.class_button import Class_Button
from styles import *
from PIL import ImageTk, Image

class Assignments_Screen(tk.Frame):
    def __init__(self, container):
        super().__init__(container, bg = dark_color, width = 1000, height = 500)

        self.clases = tk.LabelFrame(self,
                                    width = 300,
                                    height = 500-margin*2,
                                    bg = dark_color,
                                    text = "Classes",
                                    borderwidth = frame_width,
                                    font = label_frame_font(self),
                                    fg =  white_color)
        self.clases.place(x=margin, width = 300, height = 500-margin)

        self.container = tk.Frame(self, bg = dark_color)
        self.container.place(x=300+margin*2, width=1000-(300+margin*2), height = 500)

        self.workspaces = {}
        for workspace in (Workspace_Exams, Workspace_Assistance):
            name = workspace.__name__
            frame = workspace(self.container, margin = margin, controller = self)
            self.workspaces[name] = frame
            frame.place(x=0,y=0, height = 500)
        self.show_workspace("Workspace_Assistance")

        for b in range(7):
            b = Class_Button(master = self.clases, level = "PR1", schedule="L X V 16:00 - 17:00")
            b.colocar()

    def show_workspace(self, workspace):
        frame = self.workspaces[workspace]
        frame.tkraise()