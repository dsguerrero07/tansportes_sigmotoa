import sqlite3

def crear_tablas():
    conexion = sqlite3.connect("transportes.db")
    cursor = conexion.cursor

    cursor.execute()

    cursor.execute()

    conexion.comit()
    conexion.close()