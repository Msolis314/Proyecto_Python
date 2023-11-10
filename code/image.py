import customtkinter
import ttkbootstrap as ttk
import os
from PIL import ImageTk, Image

def read_image(path,name, tam= (20,20)):
    return customtkinter.CTkImage(Image.open(os.path.join(path,name)), size=tam)