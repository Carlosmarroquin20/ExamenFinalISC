
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