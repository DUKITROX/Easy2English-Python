import tkinter as tk
from widgets.student_checkbox import *
from widgets.homework_entry import *
from styles import *

class Workspace_Assistance(tk.Frame):
    def __init__(self, master, margin, controller):
        super().__init__(master, bg = dark_color)

        f = tk.LabelFrame(self,
                          text = "Assitance",
                          font = label_frame_font(self),
                          fg =white_color,
                          bg = dark_color,
                          borderwidth = frame_width,
                          height = 300,
                          width = 1000-(300+margin*3)
                          )
        f.pack(fill = "both")

        canvas = tk.Canvas(f, background = dark_color, highlightthickness = 0)
        canvas.pack(fill = "both", expand = True, side = "left")

        scrollbar = tk.Scrollbar(f, orient = "vertical",command = canvas.yview)
        scrollbar.pack(fill = "y", side = "right")

        canvas.configure(yscrollcommand = scrollbar.set)
        canvas.bind("<Configure>", lambda event: canvas.configure(scrollregion = canvas.bbox("all")))

        students = tk.Frame(canvas, background = dark_color)
        canvas.create_window((0,0), anchor = "nw", window = students)

        for h in range(12):
            h = Student_Checkbox(students, student_name=f"Student nasdasdasdsadasd dumasdsdber").colocar()


        g = tk.LabelFrame(self,
                          text="Homework",
                          font=label_frame_font(self),
                          fg=white_color,
                          bg=dark_color,
                          borderwidth=frame_width,
                          height=177-margin*2,
                          width=1000 - (300 + margin * 3)
                          )
        g.pack(fill = "x")

        entry = Homework_Entry(g).colocar()

        assistance_button = tk.Button(self,
                                    text="Send assistance",
                                    font=lower_button_font(self),
                                    fg=white_color,
                                    activeforeground=white_color,
                                    bg=light_color,
                                    activebackground=light_color,
                                    borderwidth=button_width,
                                     )
        assistance_button.pack(fill="x", expand=True, side="left", pady=margin, padx=3)

        homework_button = tk.Button(self,
                                    text = "Send homework",
                                    font = lower_button_font(self),
                                    fg = white_color,
                                    activeforeground = white_color,
                                    bg = light_color,
                                    activebackground = light_color,
                                    borderwidth = button_width)
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

        #todo implement homework textEntryBox