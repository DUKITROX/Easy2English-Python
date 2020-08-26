import tkinter as tk
from screens.assignments_screen.workspace_assitance import *
from screens.assignments_screen.worksapce_exams import *
from services.database_methods import database
from widgets.class_button import Class_Button
from styles import *

class Assignments_Screen(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg = dark_color, width = 1000, height = 500)
        self.clases = tk.LabelFrame(self,
                                    width = 300,
                                    height = 500-margin,
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
            frame.place(x=0,y=0, height = 500, width=1000-(300+margin*2))
        self.show_workspace("Workspace_Assistance")

    def show_workspace(self, workspace):
        frame = self.workspaces[workspace]
        frame.tkraise()

    def place_classes(self):
        for b in database.get_classes():
            id = b["id"]
            b = Class_Button(self.clases,
                             level = b["level"],
                             schedule = b["schedule"],
                             id = id,
                             controller = self,
                             )
            b.colocar()

    def get_students_info(self, id, level, schedule):
        database.fetch_students_info(id = id)
        class_info_dict = {
            "id":str(id),
            "level":str(level),
            "schedule":str(schedule)
        }
        self.workspaces["Workspace_Assistance"].class_info_dict = class_info_dict
        self.workspaces["Workspace_Assistance"].clear_homework()
        self.focus_set()
        self.workspaces["Workspace_Assistance"].place_students()

        self.workspaces["Workspace_Exams"].place_students()

    def log_out(self):
        self.clases.destroy()
        self.clases = tk.LabelFrame(self,
                                    width=300,
                                    height=500 - margin,
                                    bg=dark_color,
                                    text="Classes",
                                    borderwidth=frame_width,
                                    font=label_frame_font(self),
                                    fg=white_color)
        self.clases.place(x=margin, width=300, height=500 - margin)
        self.workspaces["Workspace_Assistance"].log_out()