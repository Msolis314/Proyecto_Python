from tkinter import font
import os
import customtkinter
import ttkbootstrap as ttk
from PIL import ImageTk, Image

#from config import COLOR_SUPERIOR, COLOR_MENU, COLOR_BODY,FG_COLOR,HOVER_COLOR,TEXT_COLOR

#Caracteristicas del sistema
COLOR_SUPERIOR=("#a7a5a5","#f6f1e8")
COLOR_MENU=("#a7a5a5","#f6f1e8")
COLOR_BODY="transparent"
HOVER_COLOR=("gray70", "gray30")
TEXT_COLOR=("gray10", "black")
FG_COLOR="transparent"
BUTTOM_HOVER=("gray60","gray25")

class ExceptionSystem(Exception):
    ''' Clase para el manejo de excepciones'''
    def __init__(self, mensaje="Error"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

def set_font(family):
    ''' Funcion para setear una fuente'''
    try:
        return customtkinter.CTkFont(family=family, size=12)
    except:
        return customtkinter.CTkFont(family='calibri', size=12)

"""
Funcion para colocar la ventana en el centro de la pantalla
Parametros
----------
<objeto de pantalla>:
<ancho ventana>:int
<largo ventana>: int 
Retorno
----------
Geometria de ventana: instancia de CTk
"""
def center(screen, weight_app, height_app):
    screen_weight= screen.winfo_screenwidth()
    screen_height= screen.winfo_screenheight()
    # Calcular la posicion en x y y de la ventana
    """
    Tengo que obtener el offset por tanto 
    resto la mitad de lo valores de altura 
    de pantalla y ventana"""
    y = int((screen_height/2)-(height_app/2))
    x = int((screen_weight/2)- (weight_app/2))

    # Retorna lo debe ir en geometru
    return screen.geometry(f"{weight_app}x{height_app}+{x}+{y}")


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
def read_image(path,name, tam= (20,20)):
    try:
        return customtkinter.CTkImage(Image.open(os.path.join(path,name)), size=tam)
    except FileNotFoundError:
        print("Error al cargar las imagenes")
# Directorio donde estan las imagenes 
global path_image
path_image =path_image= os.path.join(os.path.dirname(os.path.realpath("Documents")),r"input\Imagenes_Python")

"""
Clase de la vetana princiapal
hereda de customtkinter.CTk
"""

class MainWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        #Configurar la principal
        self.title("Presupuesto Mensual")
        self.iconbitmap(os.path.join(path_image,"icon.ico"))
        weight = 1000
        height = 600
        center(self,weight,height)
        

        self.sections()

    """
    funcion donde se declaran las secciones presentes en el display
    """
    def sections(self):
        #Frames de las secciones principales
        self.up_panel= UpperBar(self)
        #La declaracion de este widget sucede en esta seccion para acceder a la funcion que contrae y despliega el menu
        self.side_menu_image=read_image(path_image,"sidemenu.png",(10,10))
        #Boton de abrir y cerrar menu
        self._menu_bottom= customtkinter.CTkButton(self.up_panel,
                                                   text=" ", 
                                                   border_width=0,width=20,
                                                   fg_color=COLOR_SUPERIOR,
                                                   hover_color=HOVER_COLOR,
                                                   text_color=TEXT_COLOR,
                                                   image=self.side_menu_image,
                                                   compound="left",
                                                   command=self.toggle_panel)
        self._menu_bottom.pack(side=ttk.LEFT)
        self.menu_panel= MenuFrame(self)
        self.body_panel=Body_Frame(self)

        #Metodos para desplegar widgets
        self.up_panel.widgets_upper_bar()
        self.menu_panel.widgets_menu(self.body_panel)
    """
    funcion para contraer o desplegar el menu lateral
    """
    def toggle_panel(self):
        if self.menu_panel.winfo_ismapped():
            self.menu_panel.pack_forget()
        else:
            self.menu_panel.pack(side=ttk.LEFT,fill='y')
""" 
Definicion de los Frames de cada seccion 
Heredan de customtkinter.CTkFrame
Necesitan que se les pase el Master
"""
class UpperBar(customtkinter.CTkFrame):
    ''' Clase de la barra superior'''
    def __init__(self,master):
        super().__init__(master)
        self.configure(master, fg_color=COLOR_SUPERIOR, height=50)
        self.pack(side=ttk.TOP, fill ='both')
    #Display barra superior
    def widgets_upper_bar(self):
        self.title=customtkinter.CTkLabel(self, 
                                          text_color=TEXT_COLOR,
                                          text="Presupuesto digital",
                                          font=("Cascadia Mono SemiBold",15),
                                          fg_color='transparent',padx=10,
                                          pady=10,
                                          width=16)
        self.title.pack(side=ttk.LEFT)
        #Usuario actual
        self._current_user= customtkinter.CTkLabel(self,
                                                    text="user",pady=10, padx=10,
                                                    text_color=TEXT_COLOR,
                                                    font=("Century Gothic",12))
        self._current_user.pack(side=ttk.RIGHT)
"""Clase que define al menu lateral"""
class MenuFrame(customtkinter.CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        self.menu_icon=read_image(path_image,"menu.png",(40,40))
        self.image2=read_image(path_image,"salary.png",(20,20))
        self.image3=read_image(path_image,"line-chart.png",(20,20))
        self.image4=read_image(path_image,"file.png",(20,20))
        self.configure(master,width=400)
        self.pack(side=ttk.LEFT, fill='both', expand=False)
        self.grid_rowconfigure(5,weight=1)
    """
    funcion que maneja los widgets del menu
    recibe por parametro el body que representan donde se debe colocar cada widget
    """
    def widgets_menu(self,body):
       #Opciones del menu lateral
        self.menu_label=customtkinter.CTkLabel(self, text = " ",compound="top",image=self.menu_icon)
        self.menu_label.grid(row=0, column=0,padx=20,pady=20,sticky="nsew")
        self.master=body
        self.data_user= customtkinter.CTkButton(self, text ="Datos del usuario",
                                                corner_radius=0,
                                                height=30,
                                                border_spacing=10,
                                                fg_color='transparent', 
                                                text_color=("gray10", "gray90"), 
                                                hover_color=("gray70", "gray30"),
                                                image=self.image2, 
                                                anchor="w",
                                                command=self.evento_data_user)
        self.data_user.grid(row=2,column=0, sticky="nsew")
        self._analisis= customtkinter.CTkButton(self, text ="Visualizacion de datos",
                                            corner_radius=0,
                                            height=30,
                                            border_spacing=10,
                                            fg_color='transparent', 
                                            text_color=("gray10", "gray90"), 
                                            hover_color=("gray70", "gray30"), 
                                            anchor="w",
                                            image=self.image3,
                                            command=self.evento_analisis)
        self._analisis.grid(row=3,column=0, sticky="nsew")
        self.exportar_datos= customtkinter.CTkButton(self, text ="Exportar_Datos",
                                            corner_radius=0,
                                            height=30,
                                            border_spacing=10,
                                            fg_color='transparent', 
                                            text_color=("gray10", "gray90"), 
                                            hover_color=("gray70", "gray30"), 
                                            anchor="w",
                                            image=self.image4,
                                            command=self.evento3)
        self.exportar_datos.grid(row=4,column=0, sticky="nsew")
        self.menu_display= customtkinter.CTkOptionMenu(master=self,values = ['blue','dark-blue','green'], command=self.evento_color)
        self.menu_display.grid(row =6, column=0,padx=20,pady=20 ,sticky = "s")
        self.menu_display= customtkinter.CTkOptionMenu(master=self,
                                                       values = ['dark','system','light'], 
                                                       command=self.evento_apariencia)
        self.menu_display.grid(row =5, column=0,padx=20,pady=20 ,sticky = "s")
        self.change_window("data_user")
    #Definir eventos para los botones y menus
    def evento_apariencia(self,op):
        customtkinter.set_appearance_mode(op)
    #Eventocolor
    def evento_color(self,color_theme):
        customtkinter.set_default_color_theme(color_theme)
    #Al clickear entrada de datos    
    def evento_data_user(self):
        self.change_window("data_user")
    #Evento para analisis
    def evento_analisis(self):
        self.change_window("analisis")
    #evento para exportar datos
    def evento3(self):
        self.change_window("export")
    """
    Esta es la funcion que se encarga de cambiar lo que se ve en el panel principal
    """
    def change_window(self,buttom):
        #Esto es para que quede marcada la opcion que se muestra en el momento en pantalla
        if buttom == "analisis":
            self._analisis.configure(fg_color=BUTTOM_HOVER)
        else:
            self._analisis.configure(fg_color="transparent")
        if buttom == "data_user":
            self.data_user.configure(fg_color=BUTTOM_HOVER)
        else:
            self.data_user.configure(fg_color="transparent")
        if buttom == "export":
            self.exportar_datos.configure(fg_color=BUTTOM_HOVER)
        else:
            self.exportar_datos.configure(fg_color="transparent")
        #Creo las instancias de los frames 
        data = EntradaDatosFrame(self.master)
        analisis= Analisis(self.master)
        export = Exportardatos(self.master)
        #Posiciono los Frames
        if buttom == "data_user":   
            data.get_frame().grid(row=0, column=2, sticky = "nsew")
        else:
            data.get_frame().grid_forget()
        if buttom == "analisis":
            analisis.get_frame().grid(row=0, column=2, sticky = "nsew")
        else:
            analisis.get_frame().grid_forget()
        if buttom == "export":
            export.get_frame().grid(row=0, column=2, sticky = "nsew")
        else:
            export.get_frame().grid_forget()

#Clase abstracta para definir caracteristicas de las otras subclases de la ventana
class SubFrames(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self._layout= customtkinter.CTkFrame(master, corner_radius=0,fg_color="transparent")
        self._layout.grid_columnconfigure(0, weight=1)
    def get_frame(self):
         return self._layout
   


#Clase para el boton data_user
class EntradaDatosFrame(SubFrames):
    def __init__(self,master):
        #Boton 1
        super().__init__(master)
        self.image_ingresos=customtkinter.CTkImage(Image.open(os.path.join(path_image,"profits.png")), size=(40,40))
        self.buttom_ingresos= customtkinter.CTkButton(master=self._layout,
                                                      text="Ingresos",
                                                      image=self.image_ingresos, 
                                                      compound="top",
                                                      command=self.event_boton1)
        self.buttom_ingresos.grid(row=0 , column= 0, padx=20,pady=10, sticky ="nsew")
        # Boton 2 
        self.image_gastos=customtkinter.CTkImage(Image.open(os.path.join(path_image,"expense.png")), size=(40,40))
        self.buttom_gastos =customtkinter.CTkButton(master=self._layout,
                                                    text="Gastos",
                                                    image=self.image_gastos, 
                                                    compound="top")
        self.buttom_gastos.grid(row=1 , column= 0, padx=20,pady=10, sticky ="nsew")

        #Boton 3
        self.image_presupuesto= customtkinter.CTkImage(Image.open(os.path.join(path_image,"budget.png")), size=(40,40))
        self.buttom_budget=customtkinter.CTkButton(master=self._layout,
                                                   text="Presupuesto",
                                                   image=self.image_presupuesto, 
                                                   compound="top")
        self.buttom_budget.grid(row=2 , column= 0, padx=20,pady=10, sticky ="nsew")
        #Nuevo frame
        self.new_frame=SubFrames(master)
    def event_boton1(self):
        #Para entrar un nuevo Frame
        self._layout.grid_forget()
        self.new_frame._layout.grid(row=0, column=2, sticky = "nsew")
        self.new_frame.columnconfigure(0, weight=1)
#Clase para el boton analisis
class Analisis(SubFrames):
    def __init__(self,master):
        super().__init__(master)
        self.option_men_var= customtkinter.StringVar(value = "grafica")
        self.options_analisis= customtkinter.CTkOptionMenu(self._layout, values=["Grafica","Pie chart","muestreo","Comparacion"],command=self.get_option_menu_choice ,variable=self.option_men_var)

        self.options_analisis.grid(row=0, column=0,padx=20,pady=10,sticky="nsew")
   #Prueba
    def get_option_menu_choice(self,choice):
        print(choice)

# Clase para el boton de exportar datos

class Exportardatos(SubFrames):
    def __init__(self,master):
        super().__init__(master)
        self.title_frame3= customtkinter.CTkLabel(self._layout, text ="Opciones de descarga",font=customtkinter.CTkFont(family="Century Gothic", weight="bold"))
        self.title_frame3.grid(row=0, column=0, padx=20,pady=20, sticky="nsew",columnspan=2)
        #Radio buttoms
        self.radio_var = customtkinter.IntVar(value=0)
        self.op1=customtkinter.CTkRadioButton(self._layout, text="Excel",font=customtkinter.CTkFont(family="Century Gothic"),command=self.radio_event,variable=self.radio_var, value =1)
        self.op1.grid(row=1, column=0, padx=10, pady =(0,20),sticky="w")
        self.op2=customtkinter.CTkRadioButton(self._layout, text="Graficos",font=customtkinter.CTkFont(family="Century Gothic"),command=self.radio_event,variable=self.radio_var, value =2)
        self.op2.grid(row=1, column=1, padx=10, pady =(0,20), sticky="w")
        
    def radio_event(self):
        print(f'radio var is {self.radio_var.get()}')
class Body_Frame(customtkinter.CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        self.configure(master,fg_color=COLOR_BODY,width=150)
        self.pack(side=ttk.RIGHT, fill='both', expand=True)
        
        self.grid_columnconfigure(2, weight=1)
#Clase abstracta para definir caracteristicas de las otras subclases de la ventana

app= MainWindow()
app.mainloop()
print(app)