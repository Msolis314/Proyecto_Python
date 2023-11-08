import customtkinter
import ttkbootstrap as ttk
import os
from PIL import ImageTk, Image
import datetime as dt
from ttkbootstrap.toast import ToastNotification
global path_image 
path_image =path_image= os.path.join(os.path.dirname(os.path.realpath("Documents")),"input\\Imagenes_Python")
class MenuFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        #Poner imagene de menu
        #global path_image 
        #path_image =path_image= os.path.join(os.path.dirname(os.path.realpath("Documents")),"Imagenes_Python")
        self.image1=customtkinter.CTkImage(Image.open(os.path.join(path_image,"menu.png")), size=(40,40))
        #Imagen del boto data_user
        self.image2=customtkinter.CTkImage(Image.open(os.path.join(path_image,"salary.png")), size=(20,20))
        #Imagen del boton analisis
        self.image3= customtkinter.CTkImage(Image.open(os.path.join(path_image,"line-chart.png")), size=(20,20))
        #Imagen del boton de exportar 
        self.image4 = customtkinter.CTkImage(Image.open(os.path.join(path_image,"file.png")), size=(20,20))
        self.menu_label=customtkinter.CTkLabel(self, text = " ",compound="top",image=self.image1)
        self.menu_label.grid(row=0, column=0,padx=20,pady=20)
        
        date=dt.datetime.now()
        self.Label_date=customtkinter.CTkLabel(self, text= f"{date:%A, %B %d, %Y}", font=customtkinter.CTkFont(family="Century Gothic"))
        self.Label_date.grid(row=1, column=0,padx=10,pady=10)

        # Crear los botones del menu 
        self.master = master
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
        self.data_user.grid(row=2,column=0, sticky="ew")
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
        self._analisis.grid(row=3,column=0, sticky="ew")
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
        self.exportar_datos.grid(row=4,column=0, sticky="ew")
        self.Menu_display= customtkinter.CTkOptionMenu(master=self,values = ['blue','dark-blue','green'], command=self.evento_color)
        self.Menu_display.grid(row =6, column=0,padx=20,pady=20 ,sticky = "s")
        self.Menu_display= customtkinter.CTkOptionMenu(master=self,values = ['dark','system','light'], command=self.evento_apariencia)
        self.Menu_display.grid(row =5, column=0,padx=20,pady=20 ,sticky = "s")
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
            self._analisis.configure(fg_color=("gray60","gray25"))
        else:
            self._analisis.configure(fg_color="transparent")
        if buttom == "data_user":
            self.data_user.configure(fg_color=("gray60","gray25"))
        else:
            self.data_user.configure(fg_color="transparent")
        if buttom == "export":
            self.exportar_datos.configure(fg_color=("gray60","gray25"))
        else:
            self.exportar_datos.configure(fg_color="transparent")
        #Creo las instancias de los frames 
        data = Entrada_DatosFrame(self.master)
        analisis= Analisis(self.master)
        export = Exportar_datos(self.master)

        #Posiciono los Frames
        if buttom == "data_user":   
            data.get_frame().grid(row=0, column=1, sticky = "nsew")
        else:
            data.get_frame().grid_forget()
        if buttom == "analisis":
            analisis.get_frame().grid(row=0, column=1, sticky = "nsew")
        else:
            analisis.get_frame().grid_forget()
        if buttom == "export":
            export.get_frame().grid(row=0, column=1, sticky = "nsew")
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
class Entrada_DatosFrame(SubFrames):
    def __init__(self,master):
        #Boton 1
        super().__init__(master)
        self.image_ingresos=customtkinter.CTkImage(Image.open(os.path.join(path_image,"profits.png")), size=(40,40))
        self.buttom_ingresos= customtkinter.CTkButton(master=self._layout,
                                                      text="Ingresos",
                                                      image=self.image_ingresos, 
                                                      compound="top",
                                                      command=self.event_boton1)
        self.buttom_ingresos.grid(row=0 , column= 0, padx=20,pady=10, sticky ="ew")

        # Boton 2 
        self.image_gastos=customtkinter.CTkImage(Image.open(os.path.join(path_image,"expense.png")), size=(40,40))
        self.buttom_gastos =customtkinter.CTkButton(master=self._layout,
                                                    text="Gastos",
                                                    image=self.image_gastos, 
                                                    compound="top")
        self.buttom_gastos.grid(row=1 , column= 0, padx=20,pady=10, sticky ="ew")

        #Boton 3
        self.image_presupuesto= customtkinter.CTkImage(Image.open(os.path.join(path_image,"budget.png")), size=(40,40))
        self.buttom_budget=customtkinter.CTkButton(master=self._layout,
                                                   text="Presupuesto",
                                                   image=self.image_presupuesto, 
                                                   compound="top")
        self.buttom_budget.grid(row=2 , column= 0, padx=20,pady=10, sticky ="ew")
        
        self.new_frame=SubFrames(master)
    def event_boton1(self):
        self._layout.grid_forget()
        self.new_frame.grid(row=0, column=1, sticky = "nsew")
        self.new_frame.columnconfigure(0, weight=1)
        
    

class boton1(SubFrames):
    def __init__(self, master):
        super().__init__(master)

#Clase para el boton analisis

class Analisis(SubFrames):
    def __init__(self,master):
        super().__init__(master)
        self.option_men_var= customtkinter.StringVar(value = "grafica")
        self.options_analisis= customtkinter.CTkOptionMenu(self._layout, values=["Grafica","Pie chart","muestreo","Comparacion"],command=self.get_option_menu_choice ,variable=self.option_men_var)

        self.options_analisis.grid(row=0, column=0,padx=20,pady=10,sticky="ew")
    def get_option_menu_choice(self,choice):
        print(choice)

# Clase para el boton de exportar datos

class Exportar_datos(SubFrames):
    def __init__(self,master):
        super().__init__(master)
        self.title_frame3= customtkinter.CTkLabel(self._layout, text ="Opciones de descarga",font=customtkinter.CTkFont(family="Century Gothic", weight="bold"))
        self.title_frame3.grid(row=0, column=0, padx=20,pady=20, sticky="ew",columnspan=2)
        #Radio buttoms
        self.radio_var = customtkinter.IntVar(value=0)
        self.op1=customtkinter.CTkRadioButton(self._layout, text="Excel",font=customtkinter.CTkFont(family="Century Gothic"),command=self.radio_event,variable=self.radio_var, value =1)
        self.op1.grid(row=1, column=0, padx=10, pady =(0,20),sticky="w")
        self.op2=customtkinter.CTkRadioButton(self._layout, text="Graficos",font=customtkinter.CTkFont(family="Century Gothic"),command=self.radio_event,variable=self.radio_var, value =2)
        self.op2.grid(row=1, column=1, padx=10, pady =(0,20), sticky="w")
        
    def radio_event(self):
        print(f'radio var is {self.radio_var.get()}')
class Main_Window(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Presupuesto Mensual")
        self.geometry("600x500")
        #self.iconbitmap(os.path.join(path_image,"icon.ico"))

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
        self.myFrame.grid_rowconfigure(5,weight=1)

        '''
        grid(row, column, rowspan, columspan,sticky, padx,pady,ipadx,ipady)
        rowspan --> determina cuantas filas adjacentes se puede expandir el widget
        columspan--> determina cuantas columnas se puede expandir
        sticky---> si el widget es mas tiny que la celda dice como distribuir el espacio extra
        padx y pady---> distancia externa al widget
        ipadx y  ipady ---> distancia interna dentro del widget 
        '''
        

    def handle_keypress(event):
        #print the characeter associated to the key 
        print(event.char)

App = Main_Window()
App.mainloop()