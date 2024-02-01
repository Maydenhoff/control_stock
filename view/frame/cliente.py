import tkinter as tk
from tkinter import ttk, messagebox
from model.clientes import get_client, create_client, Cliente

class Frame_cliente(tk.Frame):
    def __init__(self, root= None):
        super().__init__(root, width=480, height=320)
        self.root = root
        self.pack()

        self.boton_add = tk.Button(self, text="Agregar cliente", command=self.create_client)
        self.boton_add.config(width=20, font=("Arial",12, "bold"))
        self.boton_add.grid(row=0, column=0, padx=10, pady=10)

        self.my_name = tk.StringVar()

        self.table_clients()

    def table_clients(self):
        self.list_clients = get_client()
        self.list_clients.reverse()

        self.table = ttk.Treeview(self, columns=("Nombre"))
        self.table.grid(row=1, column=0, columnspan=2, sticky="nse")

        self.table.heading("#0", text="Nombre")
        self.table.heading("#1", text="Acciones")

        for i in self.list_clients:
            self.table.insert("", 1, text=i[0], values=(i[1]))
        # self.table.insert("", 0, text=self.list_clients[0][0])
        # print(self.list_clients[0][0])
        

        # for i in self.list_clients:
        #     print(i, i[0], "este es 0")
    #         self.table.tag_configure("button")
    #         self.table.tag_bind("button", "<ButtonRelease-1>", lambda event, client=i: self.eliminar_cliente(client))
    #         self.table.window_create(tk.END, window=button_delete)

    # def eliminar_cliente(self, client):
    #     # Implementa aquí la lógica para eliminar el cliente
    #     print(f"Eliminar cliente: {client}")
            
            
    def create_client(self):
        window_secundary = tk.Toplevel()
        window_secundary.title("Ventana secundaria")
        window_secundary.config(width=300, height=200)
        window_secundary.focus()
        window_secundary.grab_set()
        
        #Labels
        label_name = tk.Label(window_secundary, text = "Nombre: ")
        label_name.config(font= ("Arial", 12, "bold"))
        label_name.grid(row= 0, column= 0, padx=10, pady=10)

        #enreys
        
        entry_name = tk.Entry(window_secundary, textvariable=self.my_name)
        entry_name.config(width=50, font=("Arial", 12))
        entry_name.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

        #botones
        boton_register = tk.Button(window_secundary, text= "Registrar", command=lambda:self.register_client(window_secundary))
        boton_register.config(width=20, font=("Arial", 12, "bold"))
        boton_register.grid(row=3, column=1, padx=10, pady=10)

        
    def register_client(self, window_secundary):
        cliente = Cliente(
            self.my_name.get()
        )
        create_client(cliente)
        self.table_clients()
        window_secundary.destroy()
        
    # def buton_eliminar(self):
    #     boton_eliminar = tk.Button(self, text="Eliminar")
    #     boton_eliminar.config(width=5, font=("Arial", 12, "bold"))
    #     boton_eliminar.grid(row=3, column=1, padx=1, pady=11)