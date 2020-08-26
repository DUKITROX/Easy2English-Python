import tkinter as tk
from tkinter import messagebox
import decimal
from styles import *
from widgets.entry import Entry
from widgets.student_radiobutton import  Student_RadioButton
from services.database_methods import database

class Workspace_Exams(tk.Frame):
    def __init__(self, master, margin, controller):
        super().__init__(master, bg = dark_color)

        self.controller = controller
        self.exam_number = "first_exam"
        self.null_mark_message = "Nota no asignada"
        self.students_list = []
        self.students_var = tk.IntVar()
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

        self.option_menu_var = tk.StringVar()
        self.option_menu_var.set("- First Exam -")
        self.option_menu_var.trace("w", self._update_exam_number)

        exam_option = tk.OptionMenu(exams_frame, self.option_menu_var, "- First Exam -", "- Second Exam -")
        exam_option.place(relx = 0.5, rely = 0.1, anchor = "center", width = 1000 - (300 + margin*3 + frame_width*3), height = 25)

            #Exam Entries for retrieving the information from each different part of the exam

        exam_marks = tk.Frame(exams_frame, width = self.entry_width*2+button_width*3, height = self.entry_height*2+button_width*3, bg = white_color)
        exam_marks.place(relx = 0.5, rely = 0.6, anchor = "center")

        self.reading_and_use_of_english_entry = Entry(exam_marks, placeholder = "Reading and use of English", on_password=False)
        self.reading_and_use_of_english_entry.place(x = button_width, y = button_width, width = self.entry_width, height = self.entry_height)

        self.writing_entry = Entry(exam_marks, placeholder="Writing", on_password=False)
        self.writing_entry.place(x=self.entry_width+button_width*2,y=button_width, width = self.entry_width, height = self.entry_height)

        self.listening_entry = Entry(exam_marks, placeholder="Listening", on_password=False)
        self.listening_entry.place(x=button_width, y=self.entry_height+button_width*2, width = self.entry_width, height = self.entry_height)

        self.speaking_entry = Entry(exam_marks, placeholder="Speaking", on_password=False)
        self.speaking_entry.place(x=self.entry_width+button_width*2, y=self.entry_height+button_width*2, width = self.entry_width, height = self.entry_height)

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

    def _update_exam_number(self, *args):
        if self.option_menu_var.get() == "- First Exam -" :
            self.exam_number = "first_exam"
            self.focus_set()
            self.get_student_mark()
        else:
            self.exam_number = "second_exam"
            self.focus_set()
            self.get_student_mark()

    def get_student_mark(self):
        self.focus_set()
        if self.students_var.get():
            exam_marks = database.fetch_student_exam(student_id=str(self.students_var.get()), exam_number=self.exam_number)
            if exam_marks:
                if not exam_marks["reading"] == self.null_mark_message:
                    self.reading_and_use_of_english_entry.add_exam_marks(exam_marks["reading"]),
                else: self.reading_and_use_of_english_entry.clear()
                if not exam_marks["writing"] == self.null_mark_message:
                    self.writing_entry.add_exam_marks(exam_marks["writing"])
                else:self.writing_entry.clear()
                if not exam_marks["listening"] == self.null_mark_message:
                    self.listening_entry.add_exam_marks(exam_marks["listening"])
                else: self.listening_entry.clear()
                if not exam_marks["speaking"] == self.null_mark_message:
                    self.speaking_entry.add_exam_marks(exam_marks["speaking"])
                else: self.speaking_entry.clear()
            else:
                self.reading_and_use_of_english_entry.clear()
                self.writing_entry.clear()
                self.listening_entry.clear()
                self.speaking_entry.clear()

    def _exams_button(self):
        exam_number = self.exam_number.replace("_"," ")
        reading_mark, writing_mark, listening_mark, speaking_mark = self.null_mark_message, self.null_mark_message, self.null_mark_message, self.null_mark_message
        self.correct_data = False
        if self.students_list:
            if self.students_var.get():
                #veryfing and assigning marks value so that therefore, they can be uploaded
                for mark in (self.reading_and_use_of_english_entry, self.writing_entry, self.listening_entry, self.speaking_entry):
                    if mark.on_placeholder == False and mark.get() != "":
                        try:
                            if mark.placeholder == "Reading and use of English" and float(mark.get().strip())<=10:
                                reading_mark = float(mark.get().strip())
                            elif mark.placeholder == "Writing" and float(mark.get().strip())<=10:
                                writing_mark = float(mark.get().strip())
                            elif mark.placeholder == "Listening" and float(mark.get().strip())<=10:
                                listening_mark = float(mark.get().strip())
                            elif mark.placeholder == "Speaking" and float(mark.get().strip())<=10:
                                speaking_mark = float(mark.get().strip())

                            if not float(mark.get().strip())<=10:
                                self.correct_data = False
                                messagebox.showerror(title="Exams", message = "Marks cannot contain numbers over 10")
                                break
                            self.correct_data = True
                        except Exception:
                            messagebox.showerror(title="Exams", message='Marks cannot contain commas or letters')
                            self.correct_data = False
                            break
                    else:self.correct_data = True
                if self.correct_data == True:
                    for student in self.students_list:
                        if student.id == self.students_var.get():
                            index = self.students_list.index(student)
                            result = messagebox.askyesno(title="Exams",
                                                         message=f"Would you like to update the mark of {self.students_list[index].student_name} for his {exam_number}")
                            self.focus_set()
                            if result:
                                marks_dictionary = {
                                    "reading": reading_mark,
                                    "writing": writing_mark,
                                    "listening": listening_mark,
                                    "speaking": speaking_mark
                                }
                                database.upload_students_exam(student_id=str(self.students_list[index].id),
                                                              exam_number=self.exam_number,
                                                              marks_dictionary=marks_dictionary)
                                messagebox.showinfo(title="Exams", message=f"The marks of {self.students_list[index].student_name} for his {exam_number} have been succesuflly uploaded")
            else: messagebox.showerror(title="Exams", message="Please select a student first")
        else: messagebox.showerror(title="Exams", message="Please select a class first")

    def place_students(self):
        self.students_list = []
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

        for s in database.students:
            id = s["id"]
            surname = s["surname"]
            name = s["name"]
            student_name = f"{surname} {name}"
            r = Student_RadioButton(students_frame, controller=self, student_name=student_name,
                                    variable=self.students_var, id=int(id))
            r.colocar()
            self.students_list.append(r)
        self.rendered_canvas = True

    def clear_all_entries(self):
        self.reading_and_use_of_english_entry.clear()
        self.writing_entry.clear()
        self.listening_entry.clear()
        self.speaking_entry.clear()
        self.students_var = tk.IntVar()
        self.option_menu_var.set("- First Exam -")

    def _log_out(self):
        result = messagebox.askokcancel(title="Log Out", message="Would you like to log out?")
        if result:
            self.controller.show_workspace("Workspace_Assistance")
            self.controller.master.show_screen("Authentication_Screen")

            self.clear_all_entries()
            self.students_frame.destroy()
            self.students_frame = tk.LabelFrame(self,
                                                text="Students",
                                                font=label_frame_font(self),
                                                fg=white_color,
                                                bg=dark_color,
                                                borderwidth=frame_width,
                                                height=300,
                                                width=1000 - (300 + margin * 3)
                                                )
            self.students_frame.pack(fill="both", padx=margin)

            self.controller.log_out()