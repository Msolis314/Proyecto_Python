import customtkinter
import ttkbootstrap as ttk
import os
from PIL import ImageTk, Image
from config import TEXT_COLOR
class Login(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("925x500 + 300 +200")
        self.config(bg="#fff")
        self.resizable(False,False)
        path_image =path_image= os.path.join(os.path.dirname(os.path.realpath("Documents")),"input\\Imagenes_Python")
        img=self.image1=customtkinter.CTkImage(Image.open(os.path.join(path_image,"login.png")), size=(400,400))
        Label1= customtkinter.CTkLabel(self,text=" " ,image=img, bg_color='white')
        Label1.place(x=50,y=50)
        self.frame= customtkinter.CTkFrame(self, width=350, height=350)
        self.grid_columnconfigure(0, weight=1)
        self.frame.place(x=480, y =70)

        title=customtkinter.CTkLabel(self.frame, text="Sign in", text_color=TEXT_COLOR, font=customtkinter.CTkFont(family="Microsoft YaHei UI Light", size=23, weight='bold'))
        title.grid(row=0, column=0)

        user= customtkinter.CTkEntry(self.frame, width=100, bg_color='black',corner_radius=1,fg_color="white",font=customtkinter.CTkFont(family="Microsoft YaHei UI Light", size=11))
        user.grid(row=1, column=0)
        user.insert(0,'Username')
        

App= Login()
App.mainloop()