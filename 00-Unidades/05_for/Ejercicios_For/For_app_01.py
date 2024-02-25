import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as 
import customtkinter
import random


'''
nombre:
apellido:
---
Ejercicio: for_01
---
Enunciado:
Al presionar el botón Mostrar 5 veces un mensaje (utilizando el Dialog Alert) con números ASCENDENTES, desde el 1 al 5.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        # QUE VA ANTES DEL WHILE
        seguir = True
        contador_masculino_IOT_IA = 0
        contador_IOT = 0
        contador_IA = 0 
        contador_RV_RA = 0 
        tecnologia_mas_votada = None
        contador_masculino = 0
        contador_femenino = 0
        contador_otro = 0
        contador_IOT_edad = 0
        contador_femenino_IA = 0
        acumulador_femenino_edad_IA = 0 
        bandera_del_minimo = False
        minima_edad = 0
        nombre_minimo = 0
        genero_minimo = 0



        # QUE VA ADENTRO DEL WHILE
        while seguir : # sirve ambas "seguir == True"
            nombre = ("Ingrese nombre")

            edad = ("Ingrese edad")
            edad = int(edad)
            while edad > 18 and edad <99 : #NO SE VALUA CON IF
                edad = ("ERROR","Ingrese edad una edad +18")
                edad = int(edad) 

            genero = ("Ingrese genero")
            while genero != "Masculino"  and genero != "Femenino" and genero != "Otro" :
                genero = ("Error", "Reingrese genero")


            tecnologia = ("Ingrese tecnologia")
            while tecnologia != "IA"  and tecnologia != "RV/RA" and tecnologia != "IOT" : #VALIDACION DISTITNOS
                tecnologia = ("Error", "Reingrese tecnologia")



#1) Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad este entre 25 y 50 años inclusive.

            match tecnologia: 
                case "IA":
                    contador_IA +=1 
                case "IOT":
                    contador_IOT += 1
                    # punto 4
                    if edad >= 18 and edad <= 25 or edad >= 33 and edad <= 42 :
                        contador_IOT_edad += 1

                case "RV/RA":           # para descarte se usa "..-"
                    contador_RV_RA += 1
                    #6 punto
                    if bandera_del_minimo == False or edad < minima_edad:
                        minima_edad = edad 
                        bandera_del_minimo = True
                        genero_minimo = genero
                        nombre_minimo = nombre


#3) Porcentaje de empleados por cada genero
            match genero:
                case "Masculino":
                    contador_masculino =+ 1
                    # punto 1
                    if genero == "Masculino" and (tecnologia == "IOT" or tecnologia == "IA") and edad >= 25 and edad <= 50 :
                            contador_masculino_IOT_IA += 1
                case "Femenino":
                    contador_femenino =+ 1  
                    #5 punto
                    if tecnologia == "IA":
                        contador_femenino_IA += 1
                        acumulador_femenino_edad_IA 
                        
                case "Otro":
                    contador_otro += 1
#ultima sentencia del while
        seguir = question("Seguir", "Desea continuar?")
        #fuera del while 
        # punto b del 3
        total_empleados = contador_femenino + contador_masculino + contador_otro
        
        porcentaje_masculino = (contador_masculino * 100) / total_empleados
        porcentaje_femenino  = (contador_femenino * 100) / total_empleados
        porcentaje_otro  = 100 * (porcentaje_femenino + porcentaje_masculino)

            # 4
        porcentaje_iot_edad=( contador_IOT_edad*100)/total_empleados #O por el contador_IOT
            # 5 punto
        if contador_femenino_IA != 0:
            promedio_edad = acumulador_femenino_edad_IA / contador_femenino_IA
        else:
            promedio_edad = "No se ingreso ningun femenino que cumpla con la condicion"

        

            

        print(f"1. Cantidad masculino que votaron por IOT o IA, cuya edad este entre 25 y 50 años inclusive{contador_masculino_IOT_IA}")
        print(f"2. La tecnologia mas votada es: {tecnologia_mas_votada}")
        print(promedio_edad)
        print("3.",f" porcentaje\n\tMasculino: {porcentaje_masculinos}\n\tporcentaje femenino: {porcentaje_femenino}\n\tporcentaje otro: {porcentaje_otro}")
        print("4."f"El porcentaje de IOT que votaron es de : {porcentaje_iot_edad}")
        print("5.",f"Promedio de edad de los empleados de genero Femenino que votaron por IA: {promedio_edad}")
        if contador_RV_RA != 0:
            print(f"6.{nombre_minimo}{genero_minimo}{minima_edad}")
        else: 
            print("Mensaje","No se encontro minimo para RV")
        

    


            

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

    '''
UTN Tecnologies, una reconocida software factory se encuentra en la busqueda de ideas para 
su proximo desarrollo en python, 
que promete revolucionar el mercado. 
Las posibles aplicaciones son las siguientes: 
# Inteligencia artificial (IA),
# Realidad virtual/aumentada (RV/RA), 
# Internet de las cosas (IOT) o 
# Procesamiento de lenguaje natural (NLP).

Para ello, realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas:

Los datos a ingresar por cada encuestado son:
    * nombre del empleado
    * edad (no menor a 18)
    * genero (Masculino - Femenino - Otro)
    * tecnologia (IA, RV/RA, IOT)    

En esta opción, se ingresaran empleados hasta que el usuario lo desee.

Una vez finalizado el ingreso, mostrar:

    #!X 1) - Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad 
    este entre 25 y 50 años inclusive.
    #!X 2) - Tecnología que mas se votó.
    #!X 3) - Porcentaje de empleados por cada genero
    #!X 4) - Porcentaje de empleados que votaron por IOT, siempre y cuando
    su edad se encuentre entre 18 y 25 o entre 33 y 42.  
    #!X 5) - Promedio de edad de los empleados de genero Femenino que votaron por IA
    #!X 6) - Nombre y género del empleado que voto por RV/RA con menor edad.

'''

