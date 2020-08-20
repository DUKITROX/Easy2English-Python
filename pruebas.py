import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
image = ImageTk.PhotoImage(Image.open("/assets/logo_photo.png"))
#new_image = image.resize((int(image.width/5),int(image.height/5)))
#new_image.save("c:/Users/pilot/OneDrive/Escritorio/Easy2English Python/assets/logo_photo.png")
#new_image.show()
f = tk.LabelFrame(root, text = "caca", width = 400, height = 400, bg = "red").pack()
label = tk.Label(f, image=image)
label.place(x=0,y=0)
root.mainloop()