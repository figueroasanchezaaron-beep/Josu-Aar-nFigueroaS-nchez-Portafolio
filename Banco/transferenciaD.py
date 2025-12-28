"""Josue Aaron Figueroa Sanchez
    No. Control: 23420335"""

from datetime import datetime
from conexion import Conexion
from model.movimientos import Transferencia
from PyQt6.QtWidgets import QMessageBox

class TransferenciaData:

    def __init__(self):
        # Crear conexión a la base de datos usando la clase Conexion
        con = Conexion()
        self.ConeXdb = con.conectar()
        # Crear la tabla de transferencias si no existe
        self.crearTransferencias()

    def crearTransferencias(self):
        if not self.ConeXdb:
            print("Error: no hay conexión a la base de datos.")
            return
        cursor = self.ConeXdb.cursor()
        try:
            # SQL para crear la tabla 'transferencias' con las columnas necesarias
            sql_crear_transferencias = """CREATE TABLE IF NOT EXISTS transferencias
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            monto NUMERIC,
            tipo TEXT, 
            documento TEXT, 
            motivo TEXT, 
            transfIntern BOOLEAN, 
            monedaDolares BOOLEAN,
            fecha_registro DATE, 
            verificado BOOLEAN DEFAULT 'false')"""
            cursor.execute(sql_crear_transferencias)  # Ejecutar creación de tabla
            self.ConeXdb.commit()  # Guardar cambios en la base de datos
            cursor.close()
            print("Tabla de transferencias creada exitosamente")
        except Exception as e:
            print("Tabla no creada...", e)  # Mostrar error si ocurre

    def registrar(self, info:Transferencia):
        # Obtener fecha y hora actual formateada
        fecha = datetime.now().strftime("%d%m%Y %H:%M:%S")
        cursor = self.ConeXdb.cursor()
        # SQL para insertar nuevo registro en transferencias; NULL para autoincrementar id
        query = "INSERT INTO transferencias values(NULL, ?, ?, ?, ?, ?, ?, ?, ?)"
        parametros = (info.monto, info.tipo, info.documento, info.motivo,
                      info.transfIntern, info.monedaDolares, fecha, False)
        cursor.execute(query, parametros)  # Ejecutar inserción con parámetros seguros
        self.ConeXdb.commit()  # Guardar cambios
        if cursor.rowcount == 1:  # Verificar que se haya insertado exactamente una fila
            cursor.close()
            self.ConeXdb.close()  # Cerrar conexión para liberar recursos
            return True  # Indicar éxito
        else:
            return False  # Indicar fallo en inserción
