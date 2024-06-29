from customtkinter import *
from PIL import Image
import customtkinter as ctk

ventana = CTk()

ventana.geometry("1366x768")

pestaña = CTkTabview(master=ventana,width=1266,height=675,fg_color="white")
pestaña.pack()

pestaña.add("Reguisto")
pestaña.add("Info")
# Listas

Meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]


# Funciones de botones Siguientes y Atras

def Siguiente_1():
    Frame_2.pack(pady=125)
    Frame_1.pack_forget()
    
def Atras1():
    Frame_2.pack_forget()
    Frame_1.pack(pady=125)

def Siguiente_2():
    Frame_3.pack(pady=125)
    Frame_2.pack_forget()

def Atras2():
    Frame_2.pack(pady=125)
    Frame_3.pack_forget()

# Listas de Frame

Frame_1 = CTkFrame(pestaña.tab("Reguisto"),fg_color="gray28",width=800,height=300,corner_radius=20)

Frame_2 = CTkFrame(pestaña.tab("Reguisto"),fg_color="gray28",width=800,height=300,corner_radius=20)

Frame_3 = CTkFrame(pestaña.tab("Reguisto"),fg_color="gray28",width=800,height=300,corner_radius=20)

Frame_3.pack(pady=125)
Frame_2.pack_forget()
Frame_1.pack_forget()

# ---- set Inicia siempre en Registro
pestaña.set("Reguisto")

# 1er Frame

my_image = CTkImage(light_image=Image.open("personas.png"),size=(75, 65))

image_label = CTkLabel(Frame_1, image=my_image, text="")
image_label.grid(row=0, column=0,padx=30,pady=(10,0))

LabelNombre = CTkLabel(Frame_1,text="Nombre",font=("",18))
LabelNombre.grid(row=0, column=1,pady=(40),padx=(0,190))

EntryNombre = CTkEntry(Frame_1,fg_color="transparent",width = 280, height=30,corner_radius=50,border_width=0)
EntryNombre.grid(row=0, column=1,pady=(70,0))

line_frame = CTkFrame(Frame_1, width=250, height=2, fg_color="gray84", corner_radius=0)
line_frame.grid(row=0, column=1,pady=(90,0))

LabelApellido = CTkLabel(Frame_1,text="Apellido",font=("",18))
LabelApellido.grid(row=1, column=1,padx=(0,190),pady=(20,5))

EntryApellido = CTkEntry(Frame_1,fg_color="transparent",width = 280,corner_radius=50,border_width=0)
EntryApellido.grid(row=2, column=1)

line_frame = CTkFrame(Frame_1, width=250, height=2, fg_color="gray84", corner_radius=0)
line_frame.grid(row=2, column=1,pady=(20,0))

BotonSig1 = CTkButton(Frame_1,text="Siguiente",font=("",22),command=Siguiente_1)
BotonSig1.grid(row=3, column=2,padx = (20,50),pady=(0,20))

# 2do Frame

my_image = CTkImage(light_image=Image.open("pesa.png"),size=(75, 65))

image_label_2 = CTkLabel(Frame_2, image=my_image, text="")
image_label_2.grid(row=0, column=0,padx=30,pady=(10,0))

LabelEstatura = CTkLabel(Frame_2,text="Estatura",font=("",18))
LabelEstatura.grid(row=0, column=1,pady=(40),padx=(0,190))

EntryEstatura = CTkEntry(Frame_2,fg_color="transparent",width = 280,corner_radius=50,border_width=0)
EntryEstatura.grid(row=0, column=1,pady=(70,0))

line_frame = CTkFrame(Frame_2, width=250, height=2, fg_color="gray84", corner_radius=0)
line_frame.grid(row=0, column=1,pady=(90,0))

LabelPeso = CTkLabel(Frame_2,text="Peso",font=("",18))
LabelPeso.grid(row=1, column=1,padx=(0,210),pady=(20,5))

EntryPeso = CTkEntry(Frame_2,fg_color="transparent",width = 280,corner_radius=50,border_width=0)
EntryPeso.grid(row=2, column=1)

line_frame = CTkFrame(Frame_2, width=250, height=2, fg_color="gray84", corner_radius=0)
line_frame.grid(row=2, column=1,pady=(20,0))

BotonAtra1 = CTkButton(Frame_2,text="⬅️",width=50,font=("",22),command=Atras1)
BotonAtra1.grid(row=3, column=0,padx = (20,50),pady=(0,20))

BotonSig2 = CTkButton(Frame_2,text="Siguiente",font=("",22),command=Siguiente_2)
BotonSig2.grid(row=3, column=2,padx = (20,50),pady=(0,20))

# 3er Frame

my_image = CTkImage(light_image=Image.open("calendario.png"),size=(75, 65))

image_label_3 = CTkLabel(Frame_3, image=my_image, text="")
image_label_3.grid(row=0, column=0,padx=30,pady=(10,0))

LabelFecha = CTkLabel(Frame_3,text="Fecha de Nacimiento",font=("",18))
LabelFecha.grid(row=0, column=1,padx=(0,210))

#---------------------------------

Entrydia = CTkEntry(Frame_3,width=80,height=30,corner_radius=8)
Entrydia.grid(row=0, column=1,pady=(70,0),padx=(0,300))

BarraMeses = CTkOptionMenu(Frame_3,values=Meses,width=120,height=30,corner_radius=8,fg_color="gray15")
BarraMeses.grid(row=0, column = 1,pady=(70,0),padx=(85,150))
BarraMeses.set("Diciembre")

Entryano = CTkEntry(Frame_3,width=80,height=30,corner_radius=8)
Entryano.grid(row=0, column=1,pady=(70,0),padx=(275,100))

LabelEnfer = CTkLabel(Frame_3,text="Enfermedad",font=("",18))
LabelEnfer.grid(row=2, column=1,padx=(0,280))

BarraEnfer = CTkOptionMenu(Frame_3,width=150,height=30,corner_radius=8,fg_color="gray15")
BarraEnfer.grid(row=2, column = 1,pady=(68,0),padx=(0,230))
BarraEnfer.set("Enfermedad")

LabelEnfer = CTkLabel(Frame_3,text="Genero",font=("",18))
LabelEnfer.grid(row=2, column=1,padx=(60,0))

BarraGenero = CTkOptionMenu(Frame_3,width=120,height=30,corner_radius=8,fg_color="gray15")
BarraGenero.grid(row=2, column = 1,pady=(68,0),padx=(110,0))
BarraGenero.set("Genero")

BotonAtra2 = CTkButton(Frame_3,text="⬅️",width=50,font=("",22),command=Atras2)
BotonAtra2.grid(row=3, column=0,padx = (20,50),pady=(0,20))

BotonSig3 = CTkButton(Frame_3,text="Guardar",font=("",22),command=Siguiente_2)
BotonSig3.grid(row=3, column=1,padx = (20,50),pady=(20,20))

#----------------------------------------------------------------------------



ventana.mainloop()