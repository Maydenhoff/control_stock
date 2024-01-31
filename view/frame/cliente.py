import tkinter as tk

class Frame_cliente(tk.Frame):
    def __init__(self, root= None):
        super().__init__(root, width=480, height=320)
        self.root = root
        self.pack()

        self.boton_agregar = tk.Button(self, text="Agregar cliente")
        self.boton_agregar.config(width=20, font=("Arial",12, "bold"))
        self.boton_agregar.grid(row=0, column=0, padx=10, pady=10)
       