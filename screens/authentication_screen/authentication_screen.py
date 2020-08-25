import tkinter as tk
from PIL import ImageTk, Image
from styles import *
from widgets.entry import Entry
from widgets.authentication_toasts import Authentication_Toasts
from services.database_methods import database

class Authentication_Screen(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg = dark_color, width = 1000, height = 500)

        self.master = master

        logo_image = ImageTk.PhotoImage(Image.open("c:/Users/pilot/OneDrive/Escritorio/Easy2English Python/assets/logo_photo.png"))
        logo = tk.Label(self)
        logo.image = logo_image
        logo.configure(image = logo_image, bg = dark_color)
        logo.place(relx = 0.5, rely = 0.2, anchor = "center")

        frame = tk.Frame(self, bg = white_color)
        frame.place(relx = 0.5, rely = 0.5, anchor = "center", width = 250, height = 79)

        self.id = Entry(frame, placeholder ="Id...", on_password = False)
        self.id.pack(fill="x", padx = 1, pady = 1)
        self.password = Entry(frame, placeholder ="Password...", on_password = True)
        self.password.pack(fill ="x", padx = 1, pady = 0)

        login_button = tk.Button(self,
                                    text = "Log In",
                                    font = lower_button_font(self),
                                    fg = white_color,
                                    activeforeground = white_color,
                                    bg = light_color,
                                    activebackground = light_color,
                                    borderwidth = 1,
                                    relief = "ridge",
                                    command = lambda : self._log_in(id = self.id.get().strip(), password = self.password.get().strip())
                                    )
        login_button.place(relx = 0.5, rely = 0.65, anchor = "center", width = 300)

    def _log_in(self, id, password):
        if id == "":
            t = Authentication_Toasts(self, error="ID does not exist")
        else:
            result = database.log_in(id, password)
            if result == True:
                database.fetch_clases()
                self.password.clear()
                self.id.clear()
                self.focus_set()
                self.master.screens["Assignments_Screen"].place_classes()
                self.master.show_screen("Assignments_Screen")
            else:
                t = Authentication_Toasts(self, error=result).colocar()