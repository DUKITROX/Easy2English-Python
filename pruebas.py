import tkinter as tk
from tkinter import ttk
from styles import *

class Student_Checkbox(tk.Frame):
    def __init__(self, master, student_name):
        super().__init__(master, bg = light_color,)
        self.student_name = tk.Label(self, text = student_name, bg = light_color, font = lower_button_font(self), fg = white_color)
        self.student_name.pack(side="left", padx=margin,pady=margin)

        self.c = tk.Checkbutton(self, bg = light_color, activebackground = light_color)
        self.c.pack(side="right",padx=margin,pady = margin)
    def colocar(self):
        self.pack(fill="x")

root = tk.Tk()
root.geometry("650x300")
root.config(background = light_color)

f = tk.Frame(root)
f.pack(fill="both", expand = 1)

canvas = tk.Canvas(f)
canvas.pack(fill="both", expand = True, side = "left")

scrollbar = tk.Scrollbar(f, orient = "vertical", command = canvas.yview, background = light_color)
scrollbar.place(x = 500, y=0, height = 300)

canvas.configure(yscrollcommand = scrollbar.set)
canvas.bind("<Configure>", lambda event: canvas.configure(scrollregion = canvas.bbox("all")))

frame = tk.Frame(canvas)
canvas.create_window((0,0), window = frame, anchor = "nw")

for c in range(100):
    c = Student_Checkbox(frame, "Mora Tarriño Alejandro")
    c.colocar()
root.mainloop()