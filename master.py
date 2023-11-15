import customtkinter
import funciones as fun
import os
from PIL import Image

def read_image(path,name, tam= (20,20)):
    """
    Funcion para leer imagenes
    ----------
    <path(directorio donde esta la imagen)>:string
    <name(nombre de la imagen)>:string
    <tam(size que se quiere de la imagen)>: int 
    Retorno
    ----------
    carga la imagen con la funcion customtkinter.CTkImage
    """
    try:
        return customtkinter.CTkImage(Image.open(os.path.join(path,name)), size=tam)
    except FileNotFoundError:
        print("Error al cargar las imagenes")
        raise Exception

global path_image
path_image=os.path.join(os.path.dirname(os.path.realpath("Vscode")),r"./Imagenes")
class Panel(customtkinter.CTk):
    """Panel principal, hereda de CTk"""
    def __init__(self):
        super().__init__()
        self.title("Sistema de Login")
        w,h= self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (w,h))
        self.resizable(False,False)
        
        self.welcomeimage = read_image(path_image,"login.png",(200,200))
        self.label1= customtkinter.CTkLabel(self, image=self.welcomeimage,bg_color='#3a7ff6')
        self.label1.place(x=0,y=0,relwidth=1,relheight=1)
        self.mainloop()

Panel()