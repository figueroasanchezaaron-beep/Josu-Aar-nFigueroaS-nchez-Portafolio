"""Josue Aaron Figueroa Sanchez
    No. Control: 23420335"""

from conexion import Conexion
from model.user import Usuario

from conexion import Conexion
from model.user import Usuario


class UsuarioData():
    def login(self, usuario: Usuario):
        # Crear objeto de conexión a la base de datos
        objDB = Conexion()
        print("Creo el objeto de conexión")

        # Abrir conexión con la base de datos
        con = objDB.conectar()
        print("Hizo la conexión")

        # Crear cursor para ejecutar consultas SQL
        cursor = con.cursor()
        print("Hizo el cursor")

        query = "SELECT * FROM usuarios WHERE usuario = ? AND clave=?"

        # Parámetros para evitar inyección SQL
        parametros = (usuario._usuario, usuario._clave)

        # Ejecutar consulta con parámetros
        res = cursor.execute(query, parametros)

        # Obtener el primer resultado (si existe)
        tupla = res.fetchone()

        if tupla:
            # Si se encontró usuario, crear objeto Usuario con los datos obtenidos
            usuario = Usuario(nombre=tupla[1], usuario=tupla[2], clave=tupla[3])
            cursor.close()
            con.close()
            return usuario  # Retornar usuario autenticado
        else:
            # No se encontró el usuario o la clave no coincide
            cursor.close()
            con.close()
            return None
