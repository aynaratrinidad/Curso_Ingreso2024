import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Aynara
apellido: Trinidad
---
Ejercicio: while_02bis
---
Enunciado:
Al presionar el botón ‘Mostrar Iteración’, mostrar mediante alert la suma 
de los numeros pares comprendidos entre el 1 y el 10.
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar iteración", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):
        contador = 0
        acumulador_suma = 0
        while contador < 11:
            
            if contador % 2 == 0:
                acumulador_suma = acumulador_suma + contador
            contador += 1

            print("Mensaje", f"La suma de los números pares entre 1 y 10 es: {acumulador_suma}" )
    
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()