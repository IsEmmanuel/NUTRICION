from customtkinter import * 
from PIL import Image

ventana = CTk()
ventana.geometry("1367x867")
ventana.config(background="blue")

#-------------------------------
# Listas

Meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]


#------------------------------------
# Funciones Botenes izquierdos

def Funcion_admin():
    Boton_Registro.configure(fg_color="#202020")
    Boton_Clientes.configure(fg_color="#202020")
    Boton_opcion1.configure(fg_color="#202020")
    Boton_opcion2.configure(fg_color="#202020")
    Boton_opcion3.configure(fg_color="#202020")
#1
def funcion_Boton_Registro():
    Funcion_admin()
    Boton_Registro.configure(fg_color="#494848")
    Frame_Fondo.pack(pady=70)
    Frame_Fondo_2.pack_forget()
    Frame_Ambos.pack_forget()
#2    
def funcion_Boton_Clientes():
    Funcion_admin()
    Boton_Clientes.configure(fg_color="#494848")
    Frame_Fondo_2.pack(pady=70)
    Frame_Fondo.pack_forget()
    Frame_Ambos.pack_forget()
#3
def funcion_Boton_opcion1():
    Funcion_admin()
    Boton_opcion1.configure(fg_color="#494848")
    Frame_Ambos.pack(fill="both",expand=True)
    Frame_Fondo.pack_forget()
    Frame_Fondo_2.pack_forget()
#4
def funcion_Boton_opcion2():
    Funcion_admin()
    Boton_opcion2.configure(fg_color="#494848")
#5
def funcion_Boton_opcion3():
    Funcion_admin()
    Boton_opcion3.configure(fg_color="#494848")

#----------------------------------------
# Imagenes

imagen_registro = CTkImage(light_image=Image.open("Usuario.png"),size=(46, 56))
imagen_registro = CTkImage(light_image=Image.open("Usuario.png"),size=(46, 56))
imagen_registro = CTkImage(light_image=Image.open("Usuario.png"),size=(46, 56))
imagen_registro = CTkImage(light_image=Image.open("Usuario.png"),size=(46, 56))
imagen_configuracion = CTkImage(light_image=Image.open("configuracion.png"),size=(46, 46))

#---------------------------------------
# Frame Botones izquierdos

Frame_Botones = CTkFrame(ventana, fg_color="#202020", corner_radius=0)
Frame_Botones.pack(side="left",fill="both")

#---------------------------------------
# Botones izquierdos

Boton_Registro = CTkButton(Frame_Botones,text="",image=imagen_registro,width=0,corner_radius=50
                           ,fg_color="#202020",command=funcion_Boton_Registro,background_corner_colors=["#202020"]*4)#,hover_color="#494848"
Boton_Registro.grid(row=0,column=0,pady=(50,0),sticky="w",padx=10)

Boton_Clientes = CTkButton(Frame_Botones,text="",image=imagen_registro,width=0,corner_radius=50
                           ,fg_color="#202020",command=funcion_Boton_Clientes,background_corner_colors=["#202020"]*4)#,hover_color="#494848"
Boton_Clientes.grid(row=1,column=0,pady=(50,0),sticky="w",padx=10)

Boton_opcion1 = CTkButton(Frame_Botones,text="",image=imagen_registro,width=0,corner_radius=50
                          ,fg_color="#202020",command=funcion_Boton_opcion1,background_corner_colors=["#202020"]*4)#,hover_color="#494848"
Boton_opcion1.grid(row=2,column=0,pady=(50,0),sticky="w",padx=10)

Boton_opcion2 = CTkButton(Frame_Botones,text="",image=imagen_registro,width=0,corner_radius=50
                          ,fg_color="#202020",command=funcion_Boton_opcion2,background_corner_colors=["#202020"]*4)#,hover_color="#494848"
Boton_opcion2.grid(row=3,column=0,pady=(50,0),sticky="w",padx=10)

Boton_opcion3 = CTkButton(Frame_Botones,text="",image=imagen_configuracion,width=0,corner_radius=50
                          ,fg_color="#202020",command=funcion_Boton_opcion3,background_corner_colors=["#202020"]*4)#,hover_color="#494848"
Boton_opcion3.grid(row=4,column=0,pady=(50,0),sticky="w",padx=10)

#----------------------------------------
# Frame Pricipal

Frame_Pricipal= CTkFrame(ventana, fg_color="#25272b", corner_radius=0)
Frame_Pricipal.pack(fill="both",expand=True)

#----------------------------------------
# Espacio



#----------------------------------------
# Funciones de Botones Siguientes y Atras


def Siguiente_1():
    Frame_2.pack(pady=90,padx=90)
    Frame_1.pack_forget()
    
def Atras1():
    Frame_2.pack_forget()
    Frame_1.pack(pady=90,padx=90)

def Siguiente_2():
    Frame_3.pack(pady=90,padx=90)
    Frame_2.pack_forget()

def Atras2():
    Frame_2.pack(pady=90,padx=90)
    Frame_3.pack_forget()

#-----------------------------------
# Listas de Frame

Frame_Fondo = CTkFrame(Frame_Pricipal,fg_color="gray20",width=100,height=100,corner_radius=50)
Frame_Fondo.pack_forget()

Frame_1 = CTkFrame(Frame_Fondo,fg_color="gray28",width=800,height=300,corner_radius=20)

Frame_2 = CTkFrame(Frame_Fondo,fg_color="gray28",width=800,height=300,corner_radius=20)

Frame_3 = CTkFrame(Frame_Fondo,fg_color="gray28",width=800,height=300,corner_radius=20)

Frame_3.pack_forget()
Frame_2.pack_forget()
Frame_1.pack(pady=90,padx=90)


def prueva():
    print("Datos Guardados")

#--------------------------------
# 1er Frame

my_image = CTkImage(light_image=Image.open("personas.png"),size=(95, 85))

image_label = CTkLabel(Frame_1, image=my_image, text="")
image_label.grid(row=0, column=0,padx=30,pady=(10,0))

LabelNombre = CTkLabel(Frame_1,text="Nombre",font=("",18))
LabelNombre.grid(row=0, column=1,pady=(40),padx=(0,190))

EntryNombre = CTkEntry(Frame_1,fg_color="transparent",width = 280, height=30,corner_radius=50,border_width=0)
EntryNombre.grid(row=0, column=1,pady=(70,0))

linea_frame = CTkFrame(Frame_1, width=250, height=2, fg_color="gray84", corner_radius=0)
linea_frame.grid(row=0, column=1,pady=(90,0))

LabelApellido = CTkLabel(Frame_1,text="Apellido",font=("",18))
LabelApellido.grid(row=1, column=1,padx=(0,190),pady=(20,5))

EntryApellido = CTkEntry(Frame_1,fg_color="transparent",width = 280,corner_radius=50,border_width=0)
EntryApellido.grid(row=2, column=1)

linea_frame = CTkFrame(Frame_1, width=250, height=2, fg_color="gray84", corner_radius=0)
linea_frame.grid(row=2, column=1,pady=(20,0))

BotonSig1 = CTkButton(Frame_1,text="Siguiente",font=("",22),command=Siguiente_1)
BotonSig1.grid(row=3, column=2,padx = (20,50),pady=(0,20))

#--------------------------------
# 2do Frame

my_image = CTkImage(light_image=Image.open("pesa.png"),size=(95, 85))

image_label_2 = CTkLabel(Frame_2, image=my_image, text="")
image_label_2.grid(row=0, column=0,padx=30,pady=(10,0))

LabelEstatura = CTkLabel(Frame_2,text="Estatura",font=("",18))
LabelEstatura.grid(row=0, column=1,pady=(40),padx=(0,190))

EntryEstatura = CTkEntry(Frame_2,fg_color="transparent",width = 280,corner_radius=50,border_width=0)
EntryEstatura.grid(row=0, column=1,pady=(70,0))

linea_frame = CTkFrame(Frame_2, width=250, height=2, fg_color="gray84", corner_radius=0)
linea_frame.grid(row=0, column=1,pady=(90,0))

LabelPeso = CTkLabel(Frame_2,text="Peso",font=("",18))
LabelPeso.grid(row=1, column=1,padx=(0,210),pady=(20,5))

EntryPeso = CTkEntry(Frame_2,fg_color="transparent",width = 280,corner_radius=50,border_width=0)
EntryPeso.grid(row=2, column=1)

linea_frame = CTkFrame(Frame_2, width=250, height=2, fg_color="gray84", corner_radius=0)
linea_frame.grid(row=2, column=1,pady=(20,0))

BotonAtra1 = CTkButton(Frame_2,text="⬅️",width=50,font=("",22),command=Atras1)
BotonAtra1.grid(row=3, column=0,padx = (20,50),pady=(0,20))

BotonSig2 = CTkButton(Frame_2,text="Siguiente",font=("",22),command=Siguiente_2)
BotonSig2.grid(row=3, column=2,padx = (20,50),pady=(0,20))

#--------------------------------
# 3er Frame

my_image = CTkImage(light_image=Image.open("calendario.png"),size=(100, 90))

image_label_3 = CTkLabel(Frame_3, image=my_image, text="")
image_label_3.grid(row=0, column=0,padx=30,pady=(10,0))

LabelFecha = CTkLabel(Frame_3,text="Fecha de Nacimiento",font=("",18))
LabelFecha.grid(row=0, column=1,padx=(0,210),sticky="W")

Entrydia = CTkEntry(Frame_3,width=110,height=35,corner_radius=8,border_color="gray84",placeholder_text="Dia")
Entrydia.grid(row=0, column=1,pady=(70,0),sticky="W")

BarraMeses = CTkOptionMenu(Frame_3,values=Meses,width=120,height=35,corner_radius=8,fg_color="gray19",button_color="gray19")
BarraMeses.grid(row=0, column = 1,pady=(70,0),padx=(0,100))
#BarraMeses.set("Diciembre")

Entryano = CTkEntry(Frame_3,width=110,height=35,corner_radius=8,border_color="gray84",placeholder_text="Año")
Entryano.grid(row=0, column=1,pady=(70,0),padx=(275,100))

LabelEnfer = CTkLabel(Frame_3,text="Enfermedad",font=("",18))
LabelEnfer.grid(row=2, column=1,padx=(0,280),pady=(0,13),sticky="W")

BarraEnfer = CTkOptionMenu(Frame_3,width=150,height=25,corner_radius=5,fg_color="gray19",button_color="gray19")
BarraEnfer.grid(row=2, column = 1,pady=(40,0),padx=(0,230),sticky="W")
BarraEnfer.set("Enfermedad")

LabelGenero = CTkLabel(Frame_3,text="Genero",font=("",18))
LabelGenero.grid(row=2, column=1,padx=(60,0),pady=(0,13))

BarraGenero = CTkOptionMenu(Frame_3,values=["Femenino","masculino"],width=120,height=25,corner_radius=5,fg_color="gray19",button_color="gray19")
BarraGenero.grid(row=2, column = 1,pady=(40,0),padx=(110,0))
BarraGenero.set("Genero")

BotonAtra2 = CTkButton(Frame_3,text="⬅️",width=50,font=("",22),command=Atras2)
BotonAtra2.grid(row=3, column=0,padx = (20,50),pady=(20,20))

BotonSig3 = CTkButton(Frame_3,text="Guardar",font=("",22),command=prueva)
BotonSig3.grid(row=3, column=1,padx = (0,50),pady=(20,20),sticky="E")

#---------------------------------------
# Informacion de Usuario

Frame_Fondo_2 = CTkFrame(Frame_Pricipal,fg_color="gray20",width=1000,height=900,corner_radius=50)
Frame_Fondo_2.pack_forget()

my_image = CTkImage(light_image=Image.open("global.png"),size=(95, 85))

image_label_info = CTkLabel(Frame_Fondo_2, image=my_image, text="")
image_label_info.grid(row=0,column=0,padx=(20,0),pady=(20,0))

def combobox_callback(choice):
    print("combobox dropdown clicked:", choice)

combobox = CTkComboBox(Frame_Fondo_2, values=Meses,
                                     command=combobox_callback)
combobox.set("Personas")

combobox.grid(row=1,column=0,padx=(20,0),pady=(20,0))

LabelNombre_info = CTkLabel(Frame_Fondo_2,text="Nombre",font=("",18))
LabelNombre_info.grid(row=0,column=1,padx=(20,0),pady=(20,0),sticky="W")

EntryNombre_info = CTkEntry(Frame_Fondo_2,fg_color="transparent",width = 280, height=30,corner_radius=50,border_width=0)
EntryNombre_info.grid(row=1,column=1,padx=(5,0),sticky="W")

linea_frame = CTkFrame(Frame_Fondo_2, width=250, height=2, fg_color="gray84", corner_radius=0)
linea_frame.grid(row=1,column=1,padx=(20,0),pady=(20,0),sticky="W")

LabelApellido = CTkLabel(Frame_Fondo_2,text="Apellido",font=("",18))
LabelApellido.grid(row=2,column=1,padx=(20,0),pady=(20,0),sticky="W")

EntryApellido = CTkEntry(Frame_Fondo_2,fg_color="transparent",width = 280,corner_radius=50,border_width=0)
EntryApellido.grid(row=3,column=1,padx=(5,0),sticky="W")

linea_frame = CTkFrame(Frame_Fondo_2, width=250, height=2, fg_color="gray84", corner_radius=0)
linea_frame.grid(row=3,column=1,padx=(20,0),pady=(20,0),sticky="W")

LabelEstatura = CTkLabel(Frame_Fondo_2,text="Estatura",font=("",18))
LabelEstatura.grid(row=4,column=1,padx=(20,0),pady=(20,0),sticky="W")

EntryEstatura = CTkEntry(Frame_Fondo_2,fg_color="transparent",width = 280,corner_radius=50,border_width=0)
EntryEstatura.grid(row=5,column=1,padx=(5,0),sticky="W")

linea_frame = CTkFrame(Frame_Fondo_2, width=250, height=2, fg_color="gray84", corner_radius=0)
linea_frame.grid(row=5,column=1,padx=(20,0),pady=(20,0),sticky="W")

LabelPeso = CTkLabel(Frame_Fondo_2,text="Peso",font=("",18))
LabelPeso.grid(row=6,column=1,padx=(20,0),pady=(20,0),sticky="W")

EntryPeso = CTkEntry(Frame_Fondo_2,fg_color="transparent",width = 280,corner_radius=50,border_width=0)
EntryPeso.grid(row=7,column=1,padx=(5,0),sticky="W")

linea_frame = CTkFrame(Frame_Fondo_2, width=250, height=2, fg_color="gray84", corner_radius=0)
linea_frame.grid(row=7,column=1,padx=(20,0),pady=(35,20),sticky="W")

LabelFecha = CTkLabel(Frame_Fondo_2,text="Fecha de Nacimiento",font=("",18))
LabelFecha.grid(row=0,column=2,padx=(20,0),pady=(20,0),sticky="W")

Entrydia = CTkEntry(Frame_Fondo_2,width=110,height=35,corner_radius=8,border_color="gray84",placeholder_text="Dia")
Entrydia.grid(row=1,column=2,pady=(25,0),padx=(20,0),sticky="W")

BarraMeses = CTkOptionMenu(Frame_Fondo_2,values=Meses,width=120,height=35,corner_radius=8,fg_color="gray15",button_color="gray15")
BarraMeses.grid(row=1,column=2,pady=(25,0),padx=(140))
#BarraMeses.set("Diciembre")

Entryano = CTkEntry(Frame_Fondo_2,width=110,height=35,corner_radius=8,border_color="gray84",placeholder_text="Año")
Entryano.grid(row=1,column=2,pady=(25,0),padx=(0,20),sticky="E")

LabelEnfer = CTkLabel(Frame_Fondo_2,text="Enfermedad",font=("",18))
LabelEnfer.grid(row=2,column=2,padx=(20,0),pady=(20,0),sticky="W")

BarraEnfer = CTkOptionMenu(Frame_Fondo_2,width=150,height=25,corner_radius=5,fg_color="gray15",button_color="gray15")
BarraEnfer.grid(row=3,column=2,padx=(20,0),pady=(20,0),sticky="W")
BarraEnfer.set("Enfermedad")

LabelGenero = CTkLabel(Frame_Fondo_2,text="Genero",font=("",18))
LabelGenero.grid(row=4,column=2,padx=(20,0),pady=(20,0),sticky="W")

BarraGenero = CTkOptionMenu(Frame_Fondo_2,values=["Femenino","masculino"],width=120,height=25,corner_radius=5,fg_color="gray15",button_color="gray15")
BarraGenero.grid(row=5,column=2,padx=(20,0),pady=(20,0),sticky="W")
BarraGenero.set("Genero")

my_image_lapiz = CTkImage(light_image=Image.open("Lapiz.png"),size=(214, 134))

BotonLapiz = CTkButton(Frame_Fondo_2,image=my_image_lapiz,corner_radius=100,
                       text="",fg_color="#494949",border_width=0,border_spacing=0)                
#BotonLapiz.grid(row=6,column=2,padx=(0,20),sticky="E")


#---------------------------------------
# Frame Busqueda y  Añadir alimentos 

Frame_Ambos = CTkFrame(Frame_Pricipal,fg_color="#25272b")
Frame_Ambos.pack_forget()

Frame_Busqueda = CTkFrame(Frame_Ambos,width=400, height=6, fg_color="#32353a",background_corner_colors=["#25272b"]*4
                          ,corner_radius=20)
Frame_Busqueda.pack(side="left",fill="y",pady=10,padx=10)

Frame_mas_Alimento = CTkFrame(Frame_Ambos,width=400, height=600, fg_color="#32353a",background_corner_colors=["#25272b"]*4
                              ,corner_radius=20)
Frame_mas_Alimento.pack(side="left",fill="both",expand=True,pady=10,padx=10)



ventana.mainloop()