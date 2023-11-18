import customtkinter
import ttkbootstrap as tk
from main_window.master import Panel
from .interfaz_login import AbstractLogin
from tablesetting.tablelogin import Usuario
from tablesetting.users_mem import Usuario_mem
from CTkMessagebox import CTkMessagebox
from .interfaz_register import Register
import tools.crypto as cr

class MainApp(AbstractLogin):
    def __init__(self):
        self.usuario_mem= Usuario_mem()
        self.sign_up_window = None
        super().__init__()
    
    def checkpass(self):
        """funcion para verificar la entra de constra del usuario"""
        user_data : Usuario = self.usuario_mem.get_user(self.User.get())
        if (self.checkUser(user_data)):
            self.checkContra(user_data,self.password.get())
        
        
    
    def checkContra(self, user: Usuario, contra:str):
        '''Funcion para revisar si la contra es correcta'''
        byte_pass = cr.uncrypting_pass(user.password)
        if( contra == byte_pass):
            self.destroy()
            Panel()
        else:
            CTkMessagebox(message="Incorrect username or password",title='Error',icon='cancel')

    def checkUser(self, user: Usuario):
        '''Funcion para revisar si existe el usuario'''
        status: bool = True
        if ( user == None):
            status=False
            CTkMessagebox(message='Usuario no existente, porfavor registrarse para continuar',title='Message')
        return status
    def registration(self):
     
        if self.sign_up_window is None or not self.sign_up_window.winfo_exists():
            self.sign_up_window = Register(self)  # create window if its None or destroyed
        else:
            self.sign_up_window.focus()
        



MainApp()