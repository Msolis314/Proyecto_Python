import customtkinter
import os
from PIL import ImageTk, Image
class MenuFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        #Poner imagenes
        path_image= os.path.join(os.path.dirname(os.path.realpath("Documents")),"Imagenes_Python")
        self.image1=customtkinter.CTkImage(Image.open(os.path.join(path_image,"menu.png")), size=(20,20))
        self.Label=customtkinter.CTkLabel(self, text = "Menu",compound="left",image=self.image1,font=customtkinter.CTkFont(size=18,weight="bold",family="Century Gothic"))
        self.Label.grid(row=0, column=0,padx=20,pady=20)
        # Crear los botones del menu 
        self.master = master
        self.data_user= customtkinter.CTkButton(self, text ="Datos del usuario",
                                                corner_radius=0,
                                                height=30,
                                                border_spacing=10,
                                                fg_color='transparent', 
                                                text_color=("gray10", "gray90"), 
                                                hover_color=("gray70", "gray30"), 
                                                anchor="w",
                                                command=self.evento_data_user)
        self.data_user.grid(row=1,column=0, sticky="ew")
        self.Analisis= customtkinter.CTkButton(self, text ="Visualizacion de datos",
                                            corner_radius=0,
                                            height=30,
                                            border_spacing=10,
                                            fg_color='transparent', 
                                            text_color=("gray10", "gray90"), 
                                            hover_color=("gray70", "gray30"), 
                                            anchor="w",
                                            command=self.evento_analisis)
        self.Analisis.grid(row=2,column=0, sticky="ew")
        self.Exportar_Datos= customtkinter.CTkButton(self, text ="Exportar_Datos",
                                            corner_radius=0,
                                            height=30,
                                            border_spacing=10,
                                            fg_color='transparent', 
                                            text_color=("gray10", "gray90"), 
                                            hover_color=("gray70", "gray30"), 
                                            anchor="w",
                                            command=self.evento3)
        self.Exportar_Datos.grid(row=3,column=0, sticky="ew")
        self.Menu_display= customtkinter.CTkOptionMenu(master=self,values = ['blue','dark-blue','green'], command=self.evento_color)
        self.Menu_display.grid(row =5, column=0,padx=20,pady=20 ,sticky = "s")
        self.Menu_display= customtkinter.CTkOptionMenu(master=self,values = ['dark','system','light'], command=self.evento_apariencia)
        self.Menu_display.grid(row =4, column=0,padx=20,pady=20 ,sticky = "s")
        self.change_window("data_user")
    #Definir eventos para los botones y menus
    def evento_apariencia(self,op):
        customtkinter.set_appearance_mode(op)
    def evento_color(self,color_theme):
        customtkinter.set_default_color_theme(color_theme)
    def evento_data_user(self):
        self.change_window("data_user")
    def evento_analisis(self):
        self.change_window("analisis")
    def evento3(self):
        self.change_window("export")
    """
    Esta es la funcion que se encarga de cambiar lo que se ve en el panel principal
    """
    def change_window(self,buttom):
        #Esto es para que quede marcada la opcion que se muestra en el momento en pantalla
        if buttom == "analisis":
            self.Analisis.configure(fg_color=("gray60","gray25"))
        else:
            self.Analisis.configure(fg_color="transparent")
        if buttom == "data_user":
            self.data_user.configure(fg_color=("gray60","gray25"))
        else:
            self.data_user.configure(fg_color="transparent")
        if buttom == "export":
            self.Exportar_Datos.configure(fg_color=("gray60","gray25"))
        else:
            self.Exportar_Datos.configure(fg_color="transparent")
        #Creo las instancias de los frames 
        data = Entrada_DatosFrame(self.master)
        analisis= Analisis(self.master)
        export = Frame3(self.master)

        #Posiciono los Frames
        if buttom == "data_user":   
            data.get_entry_frame().grid(row=0, column=1, sticky = "nsew")
        else:
            data.get_entry_frame().grid_forget()
        if buttom == "analisis":
            analisis.get_analisis_frame().grid(row=0, column=1, sticky = "nsew")
        else:
            analisis.get_analisis_frame().grid_forget()
        if buttom == "export":
            export.get_frame().grid(row=0, column=1, sticky = "nsew")
        else:
            export.get_frame().grid_forget()


#Frame para las opciones de entrada de datos del usuario
class Entrada_DatosFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.entry_frame= customtkinter.CTkFrame(master, corner_radius=0,fg_color="transparent")
        self.Label1=customtkinter.CTkLabel(master= self.entry_frame, text="Prueba")
        self.Label1.grid(row=0,column=0)
    def get_entry_frame(self):
        return self.entry_frame

# Frame para las opciones de visualizacion de datos
class Analisis(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.Analisis= customtkinter.CTkFrame(master, corner_radius=0,fg_color="transparent")
    def get_analisis_frame(self):
        return self.Analisis
    
#Frame para las opciones de exportar datos
class Frame3(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.frame3= customtkinter.CTkFrame(master, corner_radius=0,fg_color="transparent")
    def get_frame(self):
        return self.frame3
class Elder(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Presupuesto Mensual")
        self.geometry("600x500")
        #self.iconbitmap("C:\Users\Mariana Solis\OneDrive - Universidad de Costa Rica\Documents\GitHub\Vscode\Imagenes_Python\cash_icon-icons.com_51090.ico")

        #Ahora voy a configurar the grid
        '''
        Los metodos .columnconfigure(index, weight) y .rowconfigure(index,weight). Weight determina el espacio relativa a otra columna o fila
        '''
        #La fila 0 es mas ancha
        self.grid_rowconfigure(0,weight=1)
        #quiero dividir el espacio en dos una columna con las opciones del menu y un espacio de display
        self.grid_columnconfigure(1, weight=1)

        self.myFrame= MenuFrame(self)
        self.myFrame.grid(column=0,row=0,sticky="nsew" )
        self.myFrame.grid_rowconfigure(4,weight=1)

        '''
        grid(row, column, rowspan, columspan,sticky, padx,pady,ipadx,ipady)
        rowspan --> determina cuantas filas adjacentes se puede expandir el widget
        columspan--> determina cuantas columnas se puede expandir
        sticky---> si el widget es mas tiny que la celda dice como distribuir el espacio extra
        padx y pady---> distancia externa al widget
        ipadx y  ipady ---> distancia interna dentro del widget 
        '''
        self.myButton = customtkinter.CTkButton(self, text = "hola")

    def handle_keypress(event):
        #print the characeter associated to the key 
        print(event.char)

App = Elder()
App.mainloop()