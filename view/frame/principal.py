import tkinter as tk

class Frame_principal(tk.Frame):
    def __init__(self, root= None):
        super().__init__(root, width=480, height=320)
        self.root = root
        self.pack()

        #Boton productos
        self.boton_productos = tk.Button(self, text="Productos", command=lambda:root.show_frame("productos"))
        self.boton_productos.config(width=20, font=("Arial",12, "bold"))
        self.boton_productos.grid(row=0, column=0, padx=10, pady=10)
        # Boton Clientes
        self.boton_clientes = tk.Button(self, text="Clientes",command=lambda:root.show_frame("clientes"))
        self.boton_clientes.config(width=20, font=("Arial",12, "bold"))
        self.boton_clientes.grid(row=1, column=0, padx=10, pady=10)
        #Boton Ventas
        self.boton_ventas = tk.Button(self, text="ventas")
        self.boton_ventas.config(width=20, font=("Arial",12, "bold"))
        self.boton_ventas.grid(row=2, column=0, padx=10, pady=10)
        #Boton Salir
        self.boton_salir = tk.Button(self, text="Salir")
        self.boton_salir.config(width=20, font=("Arial",12, "bold"))
        self.boton_salir.grid(row=3, column=0, padx=10, pady=10)



