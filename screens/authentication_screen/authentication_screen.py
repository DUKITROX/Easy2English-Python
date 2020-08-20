import tkinter as tk
from PIL import ImageTk, Image
from styles import *
from widgets.entry import Entry
from widgets.authentication_toasts import Authentication_Toasts

class Authentication_Screen(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg = dark_color, width = 1000, height = 500)

        logo_image = ImageTk.PhotoImage(Image.open("c:/Users/pilot/OneDrive/Escritorio/Easy2English Python/assets/logo_photo.png"))
        logo = tk.Label(self)
        logo.image = logo_image
        logo.configure(image = logo_image, bg = dark_color)
        logo.place(relx = 0.5, rely = 0.2, anchor = "center")

        frame = tk.Frame(self, bg = white_color)
        frame.place(relx = 0.5, rely = 0.5, anchor = "center", width = 250, height = 79)

        id = Entry(frame, placeholder ="Id...", on_password = False).pack(fill="x", padx = 1, pady = 1)
        password = Entry(frame, placeholder ="Password...", on_password = True).pack(fill ="x", padx = 1, pady = 0)

        login_button = tk.Button(self,
                                    text = "Log In",
                                    font = lower_button_font(self),
                                    fg = white_color,
                                    activeforeground = white_color,
                                    bg = light_color,
                                    activebackground = light_color,
                                    borderwidth = 1,
                                    relief = "ridge",
                                    command = lambda : self._create_toast()
                                    #command = lambda : master.show_screen("Assignments_Screen")
                                    )
        login_button.place(relx = 0.5, rely = 0.65, anchor = "center", width = 300)

    def _create_toast(self):
        pass
