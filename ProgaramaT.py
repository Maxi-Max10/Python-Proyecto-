#IMPORT
#INTERFAZ
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
#BASE
import sqlite3
##CONEXION
conexion = sqlite3.connect("baseAlumnos1.db")
##VENTANA
ventana = Tk()
ventana.title("Base de datos")
ventana.geometry("800x600")
###FRAMES
frameBotones = Frame(ventana)
frameBotones.place(x=0,y=0,width=800)
frameGuardar = Frame(ventana)
frameGuardar.config(bg="slate gray")
frameGuardar.place(x=0,y=60,width=800,height=600)
frameModificar = Frame(ventana)
frameModificar.config(bg="peachpuff")
frameEliminar = Frame(ventana)
frameEliminar.config(bg="wheat1")
frameListar = Frame(ventana)
frameListar.config(bg="palegreen")
#GUARDAR
labelDniGuardar = Label(frameGuardar,text="Dni",font=("Calibri",15,"bold"),bg="slate gray")
labelDniGuardar.grid(row=0,column=0,pady=(60,20),padx=(260,20))
entryDniGuardar  = Entry(frameGuardar,font=("Calibri",15,"bold"))
entryDniGuardar.grid(row=0,column=1,pady=(40,0))
labelNombreGuardar  = Label(frameGuardar,text="Nombre",font=("Calibri",15,"bold"),bg="slate gray")
labelNombreGuardar.grid(row=1,column=0,pady=20,padx=(260,20))
entryNombreGuardar  = Entry(frameGuardar,font=("Calibri",15,"bold"))
entryNombreGuardar.grid(row=1,column=1,pady=20)
labelCursoGuardar = Label(frameGuardar,text="Curso",font=("Calibri",15,"bold"),bg="slate gray")
labelCursoGuardar.grid(row=2,column=0,pady=20,padx=(260,20))
entryCursoGuardar  = Entry(frameGuardar,font=("Calibri",15,"bold"))
entryCursoGuardar.grid(row=2,column=1,pady=20)
entryDniGuardar.focus_set()
def baseGuardar():
    if(entryDniGuardar.get() == "" or entryNombreGuardar.get()=="" or entryCursoGuardar.get()== ""):
        messagebox.showwarning("Base de datos","Complete todos los datos")
    else:
        datos = (entryDniGuardar.get(),entryNombreGuardar.get(),entryCursoGuardar.get())
        tabla = conexion.cursor()
        tabla.execute("INSERT INTO alumnos(dni,nombre,curso) VALUES(?,?,?)",datos)
        conexion.commit()
        tabla.close()
        messagebox.showinfo("Base de datos","Se ha guardado correctamente")
        entryDniGuardar.delete(0,END)
        entryNombreGuardar.delete(0,END)
        entryCursoGuardar.delete(0,END)
        entryDniGuardar.focus_set()
botonGuardar = Button(frameGuardar,text="Nuevo Registro",width=20,height=2,font=("Calibri",15,"bold"),command=baseGuardar)
botonGuardar.place(x=300,y=300)
##########
######modificar
entryBuscarModificar = Entry(frameModificar,width=30,font=("Calibri",15,"bold"))
entryBuscarModificar.grid(row=0,column=0,columnspan=2,pady=(60,0),padx=(20,0))
comboModificar = ttk.Combobox(frameModificar,width=30,font=("Calibri",15,"bold"))
comboModificar.grid(row=1,column=0,columnspan=2,pady=20,padx=(30,0))
def buscarCombo(evento):
    indice= comboModificar.current()
    buscarLegajo = (datosAlumno[indice][0],)
    tabla = conexion.cursor()
    tabla.execute("SELECT * FROM alumnos WHERE legajo=?",buscarLegajo)
    datosBuscados = tabla.fetchall()
    entryLegajoModificar.config(state="normal")
    entryLegajoModificar.delete(0,END)
    entryDniModificar.delete(0,END)
    entryNombreModificar.delete(0,END)
    entryCursoModificar.delete(0,END)
    for dato in datosBuscados:
        entryLegajoModificar.insert(0,dato[0])
        entryLegajoModificar.config(state="disabled")
        entryDniModificar.insert(0,dato[1])
        entryNombreModificar.insert(0,dato[2])
        entryCursoModificar.insert(0,dato[3])      
comboModificar.bind("<<ComboboxSelected>>",buscarCombo)

def buscoModificar():
    buscarLegajo = (entryBuscarModificar.get(),)
    tabla = conexion.cursor()
    tabla.execute("SELECT * FROM alumnos WHERE legajo=?",buscarLegajo)
    datosBuscados = tabla.fetchall()
    entryLegajoModificar.config(state="normal")
    entryLegajoModificar.delete(0,END)
    entryDniModificar.delete(0,END)
    entryNombreModificar.delete(0,END)
    entryCursoModificar.delete(0,END)
    if(len(datosBuscados) > 0):
        for dato in datosBuscados:
            entryLegajoModificar.insert(0,dato[0])
            entryLegajoModificar.config(state="disabled")
            entryDniModificar.insert(0,dato[1])
            entryNombreModificar.insert(0,dato[2])
            entryCursoModificar.insert(0,dato[3])
    else:
        messagebox.showwarning("Base de datos","No se ha encontrado el alumno")
  
botonBuscaModificar = Button(frameModificar,text="Buscar",width=10,font=("Calibri",15,"bold"),command=buscoModificar)
botonBuscaModificar.grid(row=0,column=2,pady=(60,0),sticky="W")

labelLegajoModificar = Label(frameModificar ,text="Legajo",font=("Calibri",15,"bold"),bg="peachpuff")
labelLegajoModificar.grid(row=2,column=0,pady=20,padx=10)
entryLegajoModificar = Entry(frameModificar ,font=("Calibri",15,"bold"),state="disabled")
entryLegajoModificar.grid(row=2,column=1,pady=20)
labelDniModificar = Label(frameModificar ,text="Dni",font=("Calibri",15,"bold"),bg="peachpuff")
labelDniModificar.grid(row=2,column=2,pady=20,padx=10)
entryDniModificar = Entry(frameModificar ,font=("Calibri",15,"bold"))
entryDniModificar.grid(row=2,column=3,pady=20)
labelNombreModificar = Label(frameModificar ,text="Nombre",font=("Calibri",15,"bold"),bg="peachpuff")
labelNombreModificar.grid(row=3,column=0,padx=10,pady=20)
entryNombreModificar = Entry(frameModificar ,font=("Calibri",15,"bold"))
entryNombreModificar.grid(row=3,column=1,pady=20)
labelCursoModificar= Label(frameModificar ,text="Curso",font=("Calibri",15,"bold"),bg="peachpuff")
labelCursoModificar.grid(row=3,column=2,padx=10,pady=20)
entryCursoModificar = Entry(frameModificar ,font=("Calibri",15,"bold"))
entryCursoModificar.grid(row=3,column=3,pady=20)

def baseModificar():
    if(entryDniModificar.get() == "" or entryNombreModificar.get()=="" or entryCursoModificar.get()== ""):
        messagebox.showwarning("Base de datos","Complete todos los datos")
    else:
        entryLegajoModificar.config(state="normal")
        datosModificar = (entryDniModificar.get(),entryNombreModificar.get(),entryCursoModificar.get(),entryLegajoModificar.get())
        entryLegajoModificar.config(state="disabled")
        tabla = conexion.cursor()
        tabla.execute("UPDATE alumnos SET dni=?,nombre=?,curso=? WHERE legajo=?",datosModificar)
        conexion.commit()
        tabla.close()
        messagebox.showinfo("Base de datos","Se ha modificado correctamente")
botonModificar = Button(frameModificar,text="Modificar Registro",width=20,height=2,font=("Calibri",15,"bold"),command=baseModificar)
botonModificar.place(x=300,y=420)
######
def guardarFrame():
    frameModificar.place_forget()
    frameEliminar.place_forget()
    frameListar.place_forget()
    frameGuardar.place(x=0,y=60,width=800,height=600)
    entryDniGuardar.focus_set()
guardar = Button(frameBotones,text="Guardar",width=20,height=2,font=("Calibri",15,"bold"),bd=0,bg="slate gray",command=guardarFrame)
guardar.grid(row=0,column=0)
def modificarFrame():
    frameGuardar.place_forget()
    frameEliminar.place_forget()
    frameListar.place_forget()
    frameModificar.place(x=0,y=60,width=800,height=600)
    tabla = conexion.cursor()
    tabla.execute("SELECT legajo,nombre FROM alumnos ORDER BY legajo")
    conexion.commit()
    global datosAlumnoModificar
    datosAlumno = tabla.fetchall()
    tabla.close()
    misAlumnosModificar=[]
    for dato in datosAlumno:
        misAlumnosModificar.append("Legajo: "+ str(dato[0])+", "+dato[1])
    comboModificar["values"] = misAlumnosModificar
modificar = Button(frameBotones,text="Modificar",width=19,height=2,font=("Calibri",15,"bold"),bd=0,bg="peachpuff",command=modificarFrame)
modificar.grid(row=0,column=1)
def eliminarFrame():
    frameGuardar.place_forget()
    frameModificar.place_forget()
    frameListar.place_forget()
    frameEliminar.place(x=0,y=60,width=800,height=600)
    tabla = conexion.cursor()
    tabla.execute("SELECT legajo,nombre FROM alumnos ORDER BY legajo")
    conexion.commit()
    global datosAlumno
    datosAlumno = tabla.fetchall()
    tabla.close()
    misAlumnosEliminar=[]
    for dato in datosAlumno:
        misAlumnosEliminar.append("Legajo: "+ str(dato[0])+", "+dato[1])
    comboEliminar["values"] = misAlumnosEliminar
eliminar = Button(frameBotones,text="Eliminar",width=19,height=2,font=("Calibri",15,"bold"),bd=0,bg="wheat1",command=eliminarFrame)
eliminar.grid(row=0,column=2)
def listarFrame():
    frameGuardar.place_forget()
    frameModificar.place_forget()
    frameEliminar.place_forget()
    frameListar.place(x=0,y=60,width=800,height=600)
listar = Button(frameBotones,text="Listar",width=20,height=2,font=("Calibri",15,"bold"),bd=0,bg="palegreen",command=listarFrame)
listar.grid(row=0,column=3)

#########eliminar
entryBuscarEliminar = Entry(frameEliminar,width=30,font=("Calibri",15,"bold"))
entryBuscarEliminar.grid(row=0,column=0,columnspan=2,pady=(60,0),padx=(20,0))
comboEliminar = ttk.Combobox(frameEliminar,width=30,font=("Calibri",15,"bold"))
comboEliminar.grid(row=1,column=0,columnspan=2,pady=20,padx=(30,0))
def buscarCombo(evento):
    indice= comboEliminar.current()
    buscarLegajo = (datosAlumno[indice][0],)
    tabla = conexion.cursor()
    tabla.execute("SELECT * FROM alumnos WHERE legajo=?",buscarLegajo)
    datosBuscados = tabla.fetchall()
    entryLegajoEliminar.config(state="normal")
    entryDniEliminar.config(state="normal")
    entryNombreEliminar.config(state="normal")
    entryCursoEliminar.config(state="normal")
    entryLegajoEliminar.delete(0,END)
    entryDniEliminar.delete(0,END)
    entryNombreEliminar.delete(0,END)
    entryCursoEliminar.delete(0,END)
    for dato in datosBuscados:
        entryLegajoEliminar.insert(0,dato[0])
        entryDniEliminar.insert(0,dato[1])
        entryNombreEliminar.insert(0,dato[2])
        entryCursoEliminar.insert(0,dato[3])
    entryLegajoEliminar.config(state="disabled")
    entryDniEliminar.config(state="disabled")
    entryNombreEliminar.config(state="disabled")
    entryCursoEliminar.config(state="disabled")   
comboEliminar.bind("<<ComboboxSelected>>",buscarCombo)
def buscoEliminar():
    buscarLegajo = (entryBuscarEliminar.get(),)
    print(buscaLegajo)
    tabla = conexion.cursor()
    tabla.execute("SELECT * FROM alumnos WHERE legajo=?",buscarLegajo)
    datosBuscados = tabla.fetchall()
    entryLegajoEliminar.config(state="normal")
    entryDniEliminar.config(state="normal")
    entryNombreEliminar.config(state="normal")
    entryCursoEliminar.config(state="normal")
    entryLegajoEliminar.delete(0,END)
    entryDniEliminar.delete(0,END)
    entryNombreEliminar.delete(0,END)
    entryCursoEliminar.delete(0,END)
    if(len(datosBuscados) > 0):
        for dato in datosBuscados:
            entryLegajoEliminar.insert(0,dato[0])
            entryDniEliminar.insert(0,dato[1])
            entryNombreEliminar.insert(0,dato[2])
            entryCursoEliminar.insert(0,dato[3])
            
    else:
        messagebox.showwarning("Base de datos","No se ha encontrado el alumno")
    entryLegajoEliminar.config(state="disabled")
    entryDniEliminar.config(state="disabled")
    entryNombreEliminar.config(state="disabled")
    entryCursoEliminar.config(state="disabled")
botonBuscaEliminar = Button(frameEliminar,text="Buscar",width=10,font=("Calibri",15,"bold"),command=buscoEliminar)
botonBuscaEliminar.grid(row=0,column=2,pady=(60,0),padx=10,sticky="W")
labelLegajoEliminar = Label(frameEliminar ,text="Legajo",font=("Calibri",15,"bold"),bg="wheat1")
labelLegajoEliminar.grid(row=2,column=0,pady=20,padx=20)
entryLegajoEliminar = Entry(frameEliminar ,font=("Calibri",15,"bold"),state="disabled")
entryLegajoEliminar.grid(row=2,column=1,pady=20)
labelDniEliminar = Label(frameEliminar,text="Dni",font=("Calibri",15,"bold"),bg="wheat1")
labelDniEliminar.grid(row=2,column=2,pady=20,padx=20)
entryDniEliminar = Entry(frameEliminar ,font=("Calibri",15,"bold"),state="disabled")
entryDniEliminar.grid(row=2,column=3,pady=20)
labelNombreEliminar = Label(frameEliminar,text="Nombre",font=("Calibri",15,"bold"),bg="wheat1")
labelNombreEliminar.grid(row=3,column=0,padx=20,pady=20)
entryNombreEliminar = Entry(frameEliminar ,font=("Calibri",15,"bold"),state="disabled")
entryNombreEliminar.grid(row=3,column=1,pady=20)
labelCursoEliminar= Label(frameEliminar ,text="Curso",font=("Calibri",15,"bold"),bg="wheat1")
labelCursoEliminar.grid(row=3,column=2,padx=20,pady=20)
entryCursoEliminar = Entry(frameEliminar ,font=("Calibri",15,"bold"),state="disabled")
entryCursoEliminar.grid(row=3,column=3,pady=20)
def baseEliminar():
    entryLegajoEliminar.config(state="normal")
    entryDniEliminar.config(state="normal")
    entryNombreEliminar.config(state="normal")
    entryCursoEliminar.config(state="normal")
    datoEliminar = (entryLegajoEliminar.get(),)
    tabla = conexion.cursor()
    tabla.execute("DELETE FROM alumnos WHERE legajo=?",datoEliminar)
    conexion.commit()
    tabla.close()
    messagebox.showwarning("Base de datos","Se ha eliminado el alumno")
    entryLegajoEliminar.delete(0,END)
    entryDniEliminar.delete(0,END)
    entryNombreEliminar.delete(0,END)
    entryCursoEliminar.delete(0,END)
    entryLegajoEliminar.config(state="disabled")
    entryDniEliminar.config(state="disabled")
    entryNombreEliminar.config(state="disabled")
    entryCursoEliminar.config(state="disabled")
botonEliminar = Button(frameEliminar,text="Eliminar Registro",width=20,height=2,font=("Calibri",15,"bold"),command=baseEliminar)
botonEliminar.place(x=300,y=420)

#####LISTAR

listaAlumnos = Listbox(frameListar)
listaAlumnos.place(x=200,y=20, width=400,height=400)
def baseListar():
    tabla = conexion.cursor()
    tabla.execute("SELECT * FROM alumnos ORDER BY nombre")
    conexion.commit()
    listaDeAlumnos = tabla.fetchall()
    listaAlumnos.delete(0,END)
    for alumno in listaDeAlumnos:
        listaAlumnos.insert(END,alumno)
botonListarAlumnos = Button(frameListar,text="Listar Alumnos",width=20,height=2,font=("Calibri",15,"bold"),command=baseListar)
botonListarAlumnos.place(x=250,y=450)
######CIERRE

ventana.mainloop()
