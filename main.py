import tkinter as tk
from view.frame.principal import Frame_principal
from view.frame.productos import Frame_productos
from view.frame.cliente import Frame_cliente

class MainApplication(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Stock")
        self.resizable(0,0)

        self.frame_prinicipal = Frame_principal(self)
        self.frame_productos = Frame_productos(self)
        self.frame_clientes = Frame_cliente(self)

        self.show_frame("principal")

    def show_frame(self, frame_name):
        if frame_name == "principal":
            self.frame_prinicipal.pack()
            self.frame_clientes.pack_forget()
            self.frame_productos.pack_forget()
        elif frame_name == "productos":
            self.frame_productos.pack()
            self.frame_clientes.pack_forget()
            self.frame_prinicipal.pack_forget()
        elif frame_name == "clientes":
            self.frame_clientes.pack()
            self.frame_prinicipal.pack_forget()
            self.frame_productos.pack_forget()
        else:
            self.frame_clientes.pack()
            self.frame_productos.pack_forget()



# def main():
#     root= tk.Tk()
#     root.title("Stock")
#     root.resizable(0,0)

#     app = Frame_principal(root = root)
#     app.mainloop()

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()

