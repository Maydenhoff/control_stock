import tkinter as tk

class Frame_productos(tk.Frame):
    def __init__(self, root= None):
        super().__init__(root, width=480, height=320)
        self.root = root
        self.pack()

        #Boton productos
        self.boton_agregar = tk.Button(self, text="productos")
        self.boton_agregar.config(width=20, font=("Arial",12, "bold"))
        self.boton_agregar.grid(row=0, column=0, padx=10, pady=10)
        # Boton Clientes
        # self.boton_agregar = tk.Button(self, text="Clientes")
        # self.boton_agregar.config(width=20, font=("Arial",12, "bold"))
        # self.boton_agregar.grid(row=1, column=0, padx=10, pady=10)
        # #Boton Ventas
        # self.boton_agregar = tk.Button(self, text="ventas")
        # self.boton_agregar.config(width=20, font=("Arial",12, "bold"))
        # self.boton_agregar.grid(row=2, column=0, padx=10, pady=10)
        # #Boton Salir
        # self.boton_agregar = tk.Button(self, text="Salir")
        # self.boton_agregar.config(width=20, font=("Arial",12, "bold"))
        # self.boton_agregar.grid(row=3, column=0, padx=10, pady=10)

