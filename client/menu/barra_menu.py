import tkinter as tk
from client.gui_app import Frame
# from model.clientes import get_client

def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu = barra_menu, width=300, height=300)

    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_checkbutton(label="Cliente", command=Frame.ventana_clientes)
    # barra_menu.add_cascade(label="Cliente", menu=menu_inicio, command=abrir_ventana_secundaria)

    # menu_inicio.add_cascade(label="Dar de alta cliente")
    # menu_inicio.add_command(label="Ver clientes", command=get_client)