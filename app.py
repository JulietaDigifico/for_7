import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Julieta
apellido: Digifico
---
Ejercicio: for_07
---
Enunciado:
Al presionar el botón 'Mostrar' pedir un número. Informar si el número es PRIMO o no.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        Numero_ingresado = prompt("Ingrese un número", "Número")
        Numero_ingresado = int(Numero_ingresado)
        if Numero_ingresado > 1:
            numero_primo = True
            for i in range (2, Numero_ingresado):
                if (Numero_ingresado % i) == 0:
                    numero_primo = False
                    break

            if numero_primo:
                    Mensaje = f"El numero {Numero_ingresado} es primo"
            else:
                    Mensaje = f"El numero {Numero_ingresado} no es primo"
            alert("Mensaje", Mensaje)
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()