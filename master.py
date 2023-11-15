import customtkinter
import funciones as fun
import os

global path_image
path_image=os.path.join(os.path.dirname(os.path.realpath("Vscode")),r"/Proyecto_Python/Imagenes")
class Panel(customtkinter.CTk):
    """Panel principal, hereda de CTk"""
    def __init__(self):
        super().__init__()
        self.title("Sistema de Login")
        w,h= self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (w,h))
        self.resizable(False,False)
        
        self.welcomeimage = fun.read_image(path_image,"login.png",(200,200))
        self.label1= customtkinter.CTkLabel(self, image=self.welcomeimage,bg_color='#3a7ff6')
        self.label1.place(x=0,y=0,relwidth=1,relheight=1)
        self.mainloop()

Panel()