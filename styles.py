from tkinter.font import *

margin = 7
frame_width = 4
button_width = 2

dark_color = "#283D3B"
light_color = "#197278"
white_color = "#EDDDD4"
light_white_color = "#F4EFEC"

def label_frame_font(root):
    return Font(
        root = root,
        family="Bahnschrift SemiCondensed",
        size=14,
        weight="bold"
    )
def upper_button_font(root):
    return Font(
        root = root,
        family = "Bahnschrift SemiBold",
        size = 13,
        weight = "bold")
def lower_button_font(root):
    return Font(
        root = root,
        family="Bahnschrift SemiBold",
        size=10)