
#Importando el TK inter
from tkinter import ttk
from tkinter import *
import math
import datetime
class Desk:
    def __init__(self, window,):
        #Ventana del programa
        ancho1 = 400
        altura1 = 200
        self.wind = window
        self.wind.geometry(str(ancho1)+'x'+str(altura1))
        #TITULO
        self.wind.columnconfigure(0, weight=1)
        self.wind.title('EXAMEN ISC')
        #ENTRADA
        frame = LabelFrame(self.wind, text = 'Bienvenido!!! rellene lo que se le solicita')
        frame.grid(row = 0, column = 2, columnspan = 20, pady = 20)
       #NOMBRE DEL USUARIO
        Label(frame, text = 'Nombre: ').grid(row = 1, column = 0)
        self.p1 = Entry(frame)
        self.p1.focus()
        self.p1.grid(row = 1, columnspan = 6)
        #APELLIDO DEL USUARIO
        Label(frame, text = 'Apellido.: ').grid(row = 2, column = 0)
        self.op2 = Entry(frame)
        self.op2.grid(row = 2, columnspan = 6)
        #Day
        Label(frame, text = 'Día: ').grid(row = 3, column = 0)
        self.pp3 = Entry(frame)
        self.pp3.grid(row = 3, columnspan = 6)
         #month
        Label(frame, text = 'Mes: ').grid(row = 4, column = 0)
        self.pes4 = Entry(frame)
        self.pes4.grid(row = 4, columnspan = 6)
        #year
        Label(frame, text = 'Año: ').grid(row = 5, column = 0)
        self.pap5 = Entry(frame)
        self.pap5.grid(row = 5, columnspan = 6)
        #Colocacion de botones y posicion
        Button(frame, text = 'Función 1', command = self.funcion1).grid(row = 6, column = 0 , sticky = W + E)
        Button(frame, text = 'Función 2', command = self.funcion2).grid(row = 6, column = 1 , sticky = W + E)
        Button(frame, text = 'Función 3', command = self.funcion3).grid(row = 6, column = 2 , sticky = W + E)
        Button(frame, text = 'Función 4', command = self.funcion4).grid(row = 6, column = 3 , sticky = W + E)
        Button(frame, text = 'Función 5', command = self.funcion5).grid(row = 6, column = 4 , sticky = W + E)
        #Resutado:
        self.message = Label(text = '', fg = 'Black')
        self.message.grid(row = 3, column = 1, columnspan = 2, sticky = W + E)
