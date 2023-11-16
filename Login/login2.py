import customtkinter
import ttkbootstrap as tk
from ttkbootstrap.dialogs import Messagebox
import os
from master import Panel
from Usos import reader_image
from Usos import center
from Usos import set_font 
from Usos import ExceptionSystem
from Vars import COLOR_BG
from Vars import TEXT_COLOR, HOVER_COLOR,BUTTOM_HOVER
from interfaz_login import AbstractLogin
from tablelogin import Usuario
from Login.users_mem import Usuario_mem
import crypto as cr
global path_image
path_image=os.path.join(os.path.dirname(os.path.realpath("Documents")),r"./Imagenes")
class MainApp(AbstractLogin):
    def __init__(self):
        self.usuario_mem= Usuario_mem()
        super().__init__()
    
    def checkpass(self):
        """funcion para verificar la entra de constra del usuario"""
        user_data : Usuario = self.usuario_mem.get_user(self.User.get())
        if (self.checkUser(user_data)):
            self.checkContra(self.password.get(), user_data)
        
        
    
    def checkContra(self, user: Usuario, contra:str):
        '''Funcion para revisar si la contra es correcta'''
        byte_pass = cr.decrypt(user.password)
        if( contra == byte_pass):
            self.destroy()
            Panel()
        else:
            Messagebox.show_error("Incorrect username or password",title='Wrong password')

    def checkUser(self, user: Usuario):
        '''Funcion para revisar si existe el usuario'''
        status: bool = True
        if ( user == None):
            status=False
            Messagebox.show_error(message='Usuario no existente, porfavor registrarse para continuar',title='Not user')
        return status



MainApp()