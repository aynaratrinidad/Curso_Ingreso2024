import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Aynara
apellido: Trinidad
---
Ejercicio: while_01
---
Enunciado:
se pide ingresar un numero del 100 al 1000 inclusive y informar desde el cero a ese número :
a-cuántos pares hay , 
b-cuantos multiplos de 5
c-la suma de los números divisibles por 100.
d-la suma acumulada de todos los números 

'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar iteración", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):
        ingrese_numero = prompt("Ingreso", "Ingrese numero")
        ingrese_numero = int(ingrese_numero)

        print(ingrese_numero)


    
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()