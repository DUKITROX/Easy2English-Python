import tkinter as tk
from tkinter import messagebox
import datetime
from widgets.student_checkbox import *
from widgets.homework_entry import *
from services.database_methods import database
from styles import *

class Workspace_Assistance(tk.Frame):
    def __init__(self, master, margin, controller):
        super().__init__(master, bg = dark_color)

        self.master = master
        self.controller = controller
        self.class_info_dict = None
        self.rendered_canvas = False
        self.students_list = []

    #FRAMES
        self.assistance_frame = tk.LabelFrame(self,
                          text = "Assitance",
                          font = label_frame_font(self),
                          fg =white_color,
                          bg = dark_color,
                          borderwidth = frame_width,
                          height = 300,
                          width = 1000-(300+margin*3)
                          )
        self.assistance_frame.pack(fill = "both", padx = margin)

        homework_frame = tk.LabelFrame(self,
                          text="Homework",
                          font=label_frame_font(self),
                          fg=white_color,
                          bg=dark_color,
                          borderwidth=frame_width,
                          )
        homework_frame.place(width = 1000 - (300 + margin * 3), x = 0, y = 300, height=179-margin*3)

        self.entry = Homework_Entry(homework_frame)
        self.entry.colocar()

        buttons_frame = tk.Frame(self, height = 120, bg = dark_color)
        buttons_frame.place(width=1000 - (300 + margin * 3), y = 479 - margin * 2)

    #BUTTONS at the bottom of the screen

        assistance_button = tk.Button(buttons_frame,
                                    text="Update assistance",
                                    font=lower_button_font(self),
                                    fg=white_color,
                                    activeforeground=white_color,
                                    bg=light_color,
                                    activebackground=light_color,
                                    borderwidth=button_width,
                                    command = lambda : self._assistance_button()
                                    )
        assistance_button.pack(fill = "x", expand = True, side="left", padx=3)

        homework_button = tk.Button(buttons_frame,
                                    text = "Send homework",
                                    font = lower_button_font(self),
                                    fg = white_color,
                                    activeforeground = white_color,
                                    bg = light_color,
                                    activebackground = light_color,
                                    borderwidth = button_width,
                                    command = lambda : self._homework_button())
        homework_button.pack(fill = "x", expand = True, side="left", padx=3)

        exams_button = tk.Button(buttons_frame,
                      text = "Go to exams",
                      font = lower_button_font(self),
                      fg = white_color,
                      activeforeground = white_color,
                      bg = light_color,
                      activebackground = light_color,
                      borderwidth = button_width,
                      command = lambda : self._exams_button()
                      )
        exams_button.pack(fill = "x", expand = True, side="left", padx=3)

    #FUNCTIONS

    def _assistance_button(self):
        students_assistance_dictionary = {}
        if self.students_list:
            level = self.class_info_dict["level"]
            schedule = self.class_info_dict["schedule"]
            result = messagebox.askyesno(title="Assistance",
                                         message=f"Would you like to upload student's assistance for class {level} at {datetime.date.today()}?",)
            if result:
                for student in self.students_list:
                    students_assistance_dictionary[student.id] = student.value.get()
                try:
                    database.upload_students_assistance(students_assistance_dictionary)
                except Exception:
                    messagebox.showerror(title="Assistance", message=f"Assistance couldn't be uploaded for class {level} at {datetime.date.today()}")
        else:messagebox.showerror(title="Assistance", message="Please select a classroom first")

    def _homework_button(self):
        if self.class_info_dict :
            level = self.class_info_dict["level"]
            schedule = self.class_info_dict["schedule"]
            if self.entry.get("0.0","end").strip()=="Homework..." or self.entry.get("0.0","end").strip()=="":
                messagebox.showerror(title="Homework",message="Please, enter something before submiting homework")
                self.focus_set()
            else:
                result = messagebox.askyesno(title="Homework",
                                             message=f"Would you like to send homework for class {level} at {datetime.date.today()}?")
                self.focus_set()
                if result:
                    try:
                        database.upload_homework(class_id=self.class_info_dict["id"],text=self.entry.get("0.0","end"))
                        messagebox.showinfo(title="Homework",
                                            message=f"Homework for class {level} was succesfully uploaded at {datetime.date.today()}")
                    except Exception:
                        messagebox.showerror(title="Homework", message=f"Homework couldn't be uploaded for class {level} at {datetime.date.today()}")
        else:
            messagebox.showerror(title="Homework", message="Please select a classroom first")
            self.focus_set()

    def clear_homework(self):
        self.entry.delete("0.0","end")
        self.entry["fg"] = light_white_color
        self.entry.insert("0.0", "Homework...")

    def _exams_button(self):
        self.controller.show_workspace("Workspace_Exams")

    def place_students(self):
        self.students_list = []
        if self.rendered_canvas:
            self.assistance_frame.destroy()
            self.assistance_frame = tk.LabelFrame(self,
                                                  text="Assitance",
                                                  font=label_frame_font(self),
                                                  fg=white_color,
                                                  bg=dark_color,
                                                  borderwidth=frame_width,
                                                  height=300,
                                                  width=1000 - (300 + margin * 3)
                                                  )
            self.assistance_frame.pack(fill="both", padx = margin)

        self.canvas = tk.Canvas(self.assistance_frame, background=dark_color, highlightthickness=0)
        self.canvas.pack(fill = "both", expand = True, side = "left")

        self.scrollbar = tk.Scrollbar(self.assistance_frame, orient = "vertical",command = self.canvas.yview)
        self.scrollbar.pack(fill = "y", side = "right")

        self.canvas.configure(yscrollcommand = self.scrollbar.set)
        self.canvas.bind("<Configure>", lambda event: self.canvas.configure(scrollregion = self.canvas.bbox("all")))

        students_frame = tk.Frame(self.canvas, background = dark_color)
        self.canvas.create_window((0,0), anchor = "nw", window = students_frame)

        for s in database.students:
            id = s["id"]
            surname = s["surname"]
            name = s["name"]
            student_name = f"{surname} {name}"
            value = s["value"]
            c = Student_Checkbox(students_frame, student_name=student_name, id = id, initial_value = value)
            c.colocar()
            self.students_list.append(c)
        self.rendered_canvas = True

    def log_out(self):
        self.students_list = []
        self.class_info_dict = None
        self.assistance_frame.destroy()
        self.assistance_frame = tk.LabelFrame(self,
                                              text="Assitance",
                                              font=label_frame_font(self),
                                              fg=white_color,
                                              bg=dark_color,
                                              borderwidth=frame_width,
                                              height=300,
                                              width=1000 - (300 + margin * 3)
                                              )
        self.assistance_frame.pack(fill="both", padx=margin)
        self.entry.delete("0.0", "end")
        self.entry["fg"] = light_white_color
        self.entry.insert("0.0", "Homework...")