import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Aynara
apellido: Trinidad
---
Ejercicio: if_06bis
---
Enunciado:

A partir del ingreso de la altura en centímetros de un jugador de baloncesto, 
el programa deberá determinar la posición del jugador en la cancha, 
considerando los siguientes parametros:

Menos de 160 cm: Base
Entre 160 cm y 179 cm: Escolta
Entre 180 cm y 199 cm: Alero
200 cm o más: Ala-Pívot o Pívot

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Altura")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_altura = customtkinter.CTkEntry(master=self)
        self.txt_altura.grid(row=0, column=1)
                
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, padx=30, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        ingresar_altura = float(self.txt_altura.get())
        if ingresar_altura < 160:
            mensaje = "Es base"
        elif 160 <= ingresar_altura < 180:
            mensaje = "Es escolta"
        elif 180 <= ingresar_altura < 200:
            mensaje = "Es alero"
        else:
            mensaje = "Es ala-pívot o pívot"
        alert("Mensaje", mensaje)
        
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()