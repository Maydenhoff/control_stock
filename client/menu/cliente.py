import tkinter as tk

def abrir_ventana_secundaria():
    root = tk.Toplevel()
    root.title("Ventana secundaria")
    root.resizable(0,0)
    root.config(width=300, height=200)
    # return "Hola"
    app = Frame(root=root)
    app.mainloop()

class Frame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=480, height=320)
        self.root = root
        self.pack()
        
        self.campos_cliente()

    def campos_cliente(self):
        #labels
        print("est")
        self.label_nombre = tk.Label(self, text= "Nombre: ")
        self.label_nombre.config(font=("Arial", 12, "bold"))
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10)

        #enreys
        self.mi_nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable=self.mi_nombre)
        self.entry_nombre.config(width=50, font=("Arial", 12))
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10, columnspan=1)

        #botones
        self.boton_agregar = tk.Button(self, text="Agregar", command=self.agregar_cliente)
        self.boton_agregar.config(width=20, font=("Arial",12, "bold"))
        self.boton_agregar.grid(row=3, column=0, padx=10, pady=10)

#     def agregar_cliente(self):
#         cliente = Cliente(
#             self.mi_nombre.get()
#         )
#         create_client(cliente)
#         self.root.destroy()
#     # boton_cerrar = ttk.Button(
#     #     ventana_secundaria,
#     #     text="Cerrar ventana",
#     #     command=ventana_secundaria.destroy
#     # )
#     # boton_cerrar.place(x=75, y=75)