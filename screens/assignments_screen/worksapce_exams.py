import tkinter as tk
from tkinter import messagebox
from styles import *
from widgets.entry import Entry
from widgets.student_radiobutton import  Student_RadioButton

class Workspace_Exams(tk.Frame):
    def __init__(self, master, margin, controller):
        super().__init__(master, bg = dark_color)

        self.controller = controller
        self.entry_width = 250
        self.entry_height = 30

    #FRAMES
        students_frame = tk.LabelFrame(self,
                                         text="Students",
                                         font=label_frame_font(self),
                                         fg=white_color,
                                         bg=dark_color,
                                         borderwidth=frame_width,
                                         height=300,
                                         width=1000 - (300 + margin * 3)
                                         )
        students_frame.pack(fill="x", expand = True)

        canvas = tk.Canvas(students_frame, background=dark_color, highlightthickness=0)
        canvas.pack(fill="both", expand=True, side="left")

        scrollbar = tk.Scrollbar(students_frame, orient="vertical", command=canvas.yview)
        scrollbar.pack(fill="y", side="right")

        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))

        students = tk.Frame(canvas, background=dark_color)
        canvas.create_window((0, 0), anchor="nw", window=students)

        students_var = tk.IntVar()

        for h in range(12):
            h = Student_RadioButton(students, student_name = "asdasdas asdasd asd", variable=students_var, id=h)
            h.colocar()

        #todo implement "Radiobuttons" instead of "CheckBoxes"
        #EXAMS FRAME

        exams_frame = tk.LabelFrame(self,
                                       text="Exams",
                                       font=label_frame_font(self),
                                       fg=white_color,
                                       bg=dark_color,
                                       borderwidth=frame_width,
                                       height=177 - margin * 2,
                                       width=1000 - (300 + margin * 3)
                                       )
        exams_frame.pack(fill="x")

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

        #todo add binding to "exam_option" but later on when i am implementing firebase logic

        # BUTTONS at the bottom of the screen

        exams_button = tk.Button(self,
                                 text="Set exams mark",
                                 font=lower_button_font(self),
                                 fg=white_color,
                                 activeforeground=white_color,
                                 bg=light_color,
                                 activebackground=light_color,
                                 borderwidth=button_width,
                                 command = lambda: self._exams_button()
                                 )
        exams_button.pack(fill="x", side="left", expand=True, pady=margin, padx=3)

        assistance_button = tk.Button(self,
                      text = "Go to assitance",
                      font = lower_button_font(self),
                      fg = white_color,
                      activeforeground = white_color,
                      bg = light_color,
                      activebackground = light_color,
                      borderwidth = button_width,
                      command = lambda : controller.show_workspace("Workspace_Assistance")
                      )
        assistance_button.pack(fill="x", side = "left", expand = True, pady = margin, padx = 3)

        logout_button = tk.Button(self,
                                 text="LOG OUT",
                                 font=lower_button_font(self),
                                 fg=white_color,
                                 activeforeground=white_color,
                                 bg=medium_color,
                                 activebackground=medium_color,
                                 borderwidth=button_width,
                                 command=lambda: self._log_out()
                                 )
        logout_button.pack(fill="x", side="left", expand=True, pady=margin, padx=3)

    #FUNCTIONS

    def _exams_button(self):
        messagebox.showinfo(title="Exams",message="Students marks have been succesfully updated")
    def _log_out(self):
        self.controller.show_workspace("Workspace_Assistance")
        self.controller.master.show_screen("Authentication_Screen")