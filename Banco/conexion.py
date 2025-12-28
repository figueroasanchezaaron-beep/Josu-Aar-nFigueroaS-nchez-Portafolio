"""Josue Aaron Figueroa Sanchez
    No. Control: 23420335"""

import sqlite3
import os

class Conexion():
    def __init__(self):
        try:
            rutaCarpeta = 'dataBase/'
            #rutaCarpeta = '' #Por si se necesitan hacer pruebas unitarias por interfaz
            nomArchivo = 'bancoss.db'
            self.rutaArchivo = os.path.join(rutaCarpeta, nomArchivo)
            if os.path.isfile(self.rutaArchivo):
                print(f"La base de datos {nomArchivo} existe.")
            else:
                print(f"La base de datos {nomArchivo} no existe.")
                self.CrearBaseDatos()
        except Exception as e:
            print(e)

    def CrearBaseDatos(self):
        #self.con = sqlite3.connect(banco.db) #Por si se necesita hacer pruebas unitarias
        self.con = sqlite3.connect('dataBase/bancos.db')
        self.crearTablas()

    def conectar(self):
        self.con = sqlite3.connect('dataBase/bancos.db')
        return self.con

    def crearTablas(self):
        sql_crear_tabla = """ CREATE TABLE IF NOT EXISTS usuarios
        (   id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        usuario TEXT UNIQUE,
        clave TEXT )"""
        cursor = self.con.cursor()
        res = cursor.execute(sql_crear_tabla)
        print("Resultado de crear o no la base de datos: ", res.__getstate__())
        self.crearUsuario1() #Crea el usuario al inicializar el sistema user1
        #self.crearAdmin() #Si se desea crear el administrador Admin1
        cursor.close()
        print("Acceso a la tabla exitosa")
        self.con.commit()
        self.con.close()

    def crearAdmin(self):
        try:
            sql_insert = 'INSERT INTO usuarios values (NULL, ?, ?, ?)'
            parametros = ("Administrador", "admin1", "admin123")
            cursor = self.con.cursor()
            cursor.execute(sql_insert, parametros)
            self.con.commit()
            print("Usuario creado con éxito")
        except Exception as e:
            print("Usuario existente, Error: {}".format(e))

    def crearUsuario1(self):
        try:
            sql_insert = """INSERT INTO usuarios VALUES (NULL, '{}', '{}', '{}')""".format("USUARIO", "user1", "user123")
            cursor = self.con.cursor()
            cursor.execute(sql_insert)
            self.con.commit()
            print("Usuario creado con exito")
        except Exception as e:
            print("Usuario existente, Error:{}".format(e))

if __name__ == '__main__': #En caso de que se quiera probar individualmente
    obj = Conexion()