from .conexion_db import ConexionDB
from tkinter import messagebox

def create_table():
    conexion = ConexionDB()
    sql = '''
CREATE TABLE IF NOT EXISTS clientes(
    id_cliente INTEGER,
    nombre VARCHAR,
    PRIMARY KEY(id_cliente AUTOINCREMENT)
)'''

 
    conexion.cursor.execute(sql)
    conexion.cerrar()
   


class Cliente:
    def __init__(self, nombre):
        self.id_cliente = None
        self.nombre = nombre

    def __str__(self):
        return f'Cliente[{self.nombre}]'




def create_client(cliente):
    conexion = ConexionDB()

    sql = f"""INSERT INTO clientes (nombre)
    VALUES('{cliente.nombre}')"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = "Registro de cliente"
        mensaje= "El cliente no pudo ser registrado"
        messagebox.showerror(titulo,mensaje)

def get_client():
    conexion = ConexionDB()
    list_client = []

    sql = "SELECT * FROM clientes"

    try:
        conexion.cursor.execute(sql)
        list_client = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        titulo = "Conexion a la base de datos"
        mensaje= "La base de datos no esta conectada"
        messagebox.showwarning(titulo,mensaje)
    print(list_client)
    return list_client
