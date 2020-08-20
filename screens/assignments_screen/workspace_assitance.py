import tkinter as tk
from tkinter import messagebox
from widgets.student_checkbox import *
from widgets.homework_entry import *
from styles import *

class Workspace_Assistance(tk.Frame):
    def __init__(self, master, margin, controller):
        super().__init__(master, bg = dark_color)

        self.master = master
    #FRAMES
        assistance_frame = tk.LabelFrame(self,
                          text = "Assitance",
                          font = label_frame_font(self),
                          fg =white_color,
                          bg = dark_color,
                          borderwidth = frame_width,
                          height = 300,
                          width = 1000-(300+margin*3)
                          )
        assistance_frame.pack(fill = "both")

        canvas = tk.Canvas(assistance_frame, background = dark_color, highlightthickness = 0)
        canvas.pack(fill = "both", expand = True, side = "left")

        scrollbar = tk.Scrollbar(assistance_frame, orient = "vertical",command = canvas.yview)
        scrollbar.pack(fill = "y", side = "right")

        canvas.configure(yscrollcommand = scrollbar.set)
        canvas.bind("<Configure>", lambda event: canvas.configure(scrollregion = canvas.bbox("all")))

        students = tk.Frame(canvas, background = dark_color)
        canvas.create_window((0,0), anchor = "nw", window = students)

        self.students_list = []

        for h in range (12):
            h = Student_Checkbox(students, "asdasondmasoi valasdadwwa")
            h.colocar()
            self.students_list.append(h)

        homework_frame = tk.LabelFrame(self,
                          text="Homework",
                          font=label_frame_font(self),
                          fg=white_color,
                          bg=dark_color,
                          borderwidth=frame_width,
                          height=177-margin*2,
                          width=1000 - (300 + margin * 3)
                          )
        homework_frame.pack(fill = "x")

        entry = Homework_Entry(homework_frame)
        entry.colocar()

    #BUTTONS at the bottom of the screen

        assistance_button = tk.Button(self,
                                    text="Update assistance",
                                    font=lower_button_font(self),
                                    fg=white_color,
                                    activeforeground=white_color,
                                    bg=light_color,
                                    activebackground=light_color,
                                    borderwidth=button_width,
                                    command = lambda : self._assistance_button()
                                    )
        assistance_button.pack(fill="x", expand=True, side="left", pady=margin, padx=3)

        homework_button = tk.Button(self,
                                    text = "Send homework",
                                    font = lower_button_font(self),
                                    fg = white_color,
                                    activeforeground = white_color,
                                    bg = light_color,
                                    activebackground = light_color,
                                    borderwidth = button_width,
                                    command = lambda : self._homework_button())
        homework_button.pack(fill="x", expand = True, side="left", pady = margin, padx = 3)

        exams_button = tk.Button(self,
                      text = "Go to exams",
                      font = lower_button_font(self),
                      fg = white_color,
                      activeforeground = white_color,
                      bg = light_color,
                      activebackground = light_color,
                      borderwidth = button_width,
                      command = lambda : controller.show_workspace("Workspace_Exams")
                      )
        exams_button.pack(fill="x", expand = True, side="left", pady = margin, padx = 3)

    #FUNCTIONS

    def _assistance_button(self):
        result = messagebox.askyesno(title="Assistance", message="Are you sure you want to update today's assistance?")
        if result:
            for s in self.students_list:
                s.deselect()

    def _homework_button(self):
        res = messagebox.askokcancel(title="Send Homework", message = "Would you like to send homework for today?")