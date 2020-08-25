import tkinter as tk
from tkinter import messagebox
from styles import *
from widgets.entry import Entry
from widgets.student_radiobutton import  Student_RadioButton
from services.database_methods import database

class Workspace_Exams(tk.Frame):
    def __init__(self, master, margin, controller):
        super().__init__(master, bg = dark_color)

        self.controller = controller
        self.rendered_canvas = False
        self.entry_width = 250
        self.entry_height = 30

    #FRAMES
        self.students_frame = tk.LabelFrame(self,
                                         text="Students",
                                         font=label_frame_font(self),
                                         fg=white_color,
                                         bg=dark_color,
                                         borderwidth=frame_width,
                                         height=300,
                                         width=1000 - (300 + margin * 3)
                                         )
        self.students_frame.pack(fill="both", padx = margin)

        #Exams Frame

        exams_frame = tk.LabelFrame(self,
                                       text="Exams",
                                       font=label_frame_font(self),
                                       fg=white_color,
                                       bg=dark_color,
                                       borderwidth=frame_width,
                                       height=167 - margin * 2,
                                       width=1000 - (300 + margin * 3)
                                       )
        exams_frame.place(width=1000 - (300 + margin * 3), x=0, y=300, height=179 - margin * 3)

            #Exams OptionMenu to give the ability to select between the first exam

        option_menu_var = tk.StringVar()
        option_menu_var.set("- First Exam -")
        exam_option = tk.OptionMenu(exams_frame, option_menu_var, "- First Exam -", "- Second Exam -")
        exam_option.place(relx = 0.5, rely = 0.1, anchor = "center", width = 1000 - (300 + margin*3 + frame_width*3), height = 25)

            #Exam Entries for retrieving the information from each different part of the exam

        exam_marks = tk.Frame(exams_frame, width = self.entry_width*2+button_width*3, height = self.entry_height*2+button_width*3, bg = white_color)
        exam_marks.place(relx = 0.5, rely = 0.6, anchor = "center")

        reading_and_use_of_english_entry = Entry(exam_marks, placeholder = "Reading and use of English", on_password=False)
        reading_and_use_of_english_entry.place(x = button_width, y = button_width, width = self.entry_width, height = self.entry_height)

        writing_entry = Entry(exam_marks, placeholder="Writing", on_password=False)
        writing_entry.place(x=self.entry_width+button_width*2,y=button_width, width = self.entry_width, height = self.entry_height)

        listening_entry = Entry(exam_marks, placeholder="Listening", on_password=False, state = "normal")
        listening_entry.place(x=button_width, y=self.entry_height+button_width*2, width = self.entry_width, height = self.entry_height)

        speaking_entry = Entry(exam_marks, placeholder="Listening", on_password=False)
        speaking_entry.place(x=self.entry_width+button_width*2, y=self.entry_height+button_width*2, width = self.entry_width, height = self.entry_height)

        #todo add binding to "exam_option" with tkinter variables but later on when i am implementing firebase logic

        #Buttons Frame
        buttons_frame = tk.Frame(self, height=120, bg=dark_color)
        buttons_frame.place(width=1000 - (300 + margin * 3), y=479 - margin * 2)

        # BUTTONS at the bottom of the screen

        exams_button = tk.Button(buttons_frame,
                                 text="Set exams mark",
                                 font=lower_button_font(self),
                                 fg=white_color,
                                 activeforeground=white_color,
                                 bg=light_color,
                                 activebackground=light_color,
                                 borderwidth=button_width,
                                 command = lambda: self._exams_button()
                                 )
        exams_button.pack(fill = "x", expand = True, side="left", padx=3)

        assistance_button = tk.Button(buttons_frame,
                      text = "Go to assitance",
                      font = lower_button_font(self),
                      fg = white_color,
                      activeforeground = white_color,
                      bg = light_color,
                      activebackground = light_color,
                      borderwidth = button_width,
                      command = lambda : controller.show_workspace("Workspace_Assistance")
                      )
        assistance_button.pack(fill = "x", expand = True, side="left", padx=3)

        logout_button = tk.Button(buttons_frame,
                                 text="LOG OUT",
                                 font=lower_button_font(self),
                                 fg=white_color,
                                 activeforeground=white_color,
                                 bg=medium_color,
                                 activebackground=medium_color,
                                 borderwidth=button_width,
                                 command=lambda: self._log_out()
                                 )
        logout_button.pack(fill = "x", expand = True, side="left", padx=3)

    #FUNCTIONS

    def _exams_button(self):
        messagebox.showinfo(title="Exams",message="Students marks have been succesfully updated")

    def _log_out(self):
        self.controller.show_workspace("Workspace_Assistance")
        self.controller.master.show_screen("Authentication_Screen")

    def place_students(self):
        students_list = []
        if self.rendered_canvas:
            self.students_frame.destroy()
            self.students_frame = tk.LabelFrame(self,
                                                  text="Assitance",
                                                  font=label_frame_font(self),
                                                  fg=white_color,
                                                  bg=dark_color,
                                                  borderwidth=frame_width,
                                                  height=300,
                                                  width=1000 - (300 + margin * 3)
                                                  )
            self.students_frame.pack(fill="both", padx=margin)

        self.canvas = tk.Canvas(self.students_frame, background=dark_color, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True, side="left")

        self.scrollbar = tk.Scrollbar(self.students_frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(fill="y", side="right")

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind("<Configure>", lambda event: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        students_frame = tk.Frame(self.canvas, background=dark_color)
        self.canvas.create_window((0, 0), anchor="nw", window=students_frame)

        students_var = tk.IntVar()

        for s in database.students:
            id = s["id"]
            surname = s["surname"]
            name = s["name"]
            student_name = f"{surname} {name}"
            dict = {
                "id":id,
                "student_name":student_name
            }
            students_list.append(dict)
        for s in students_list:
            r = Student_RadioButton(students_frame, student_name=s["student_name"], variable = students_var, id=int(s["id"]))
            r.colocar()
        self.rendered_canvas = True