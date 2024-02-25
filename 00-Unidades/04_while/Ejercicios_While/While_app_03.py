import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Aynara
apellido: Trinidad
---
Ejercicio: while_03
---
Enunciado:
Al presionar el botón ‘Pedir clave’, solicitar al usuario que ingrese una contraseña mediante prompt. 
Comprobar que la contraseña ingresada sea ‘utn750’. En caso de no coincidir, volver a solicitarla hasta que coincidan.
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_pedir_clave = customtkinter.CTkButton(master=self, text="Ingresar", command=self.btn_pedir_clave_on_click)
        self.btn_pedir_clave.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_pedir_clave_on_click(self):
        '''clave = prompt("Clave", "Ingrese clave")
        while clave != "utn750":
            clave = prompt("Error", "Reingrese clave")
'''
        cantidad_personas = 0
        suma_edades = 0
        while cantidad_personas < 10 :
            edad = prompt("Ingreso", "Ingreso de edad")
            edad = int(edad)
        while edad < 18 or edad > 120 :
            edad = prompt("Ingreso", "Ingreso de edad")
            edad = int(edad)

            suma_edades = suma_edades + edad
            cantidad_personas = cantidad_personas + 1

        
        promedio_edades = suma_edades / cantidad_personas
        print(promedio_edades)
        print(suma_edades)
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()