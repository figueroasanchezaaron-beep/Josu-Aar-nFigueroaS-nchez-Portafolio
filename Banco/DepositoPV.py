"""Josue Aaron Figueroa Sanchez
    No. Control: 23420335"""

import sys
import requests
from PyQt6.QtWidgets import QMessageBox, QDialog, QApplication
from PyQt6 import uic

# Estilo CSS para los botones
stylesheet = """
QPushButton {
    background-color: lightblue;
}
QPushButton:hover {
    color: red;
    alternate-background-color: darkblue;
    active-background-color: black;
}
QPushButton:pressed {
    color: green;
    background-color: black;
}
"""

class Depositowindow(QDialog):
    def __init__(self):
        super(Depositowindow, self).__init__()
        # Cargar la interfaz gráfica desde archivo .ui (local o remoto)
        # self.regWin = uic.loadUi("gui/Deposito.ui")  # Para versión remota o distinta ruta
        self.depWin = uic.loadUi("DepositoBC.ui")  # Para ejecución local
        self.depWin.setWindowTitle("Registro")
        self.initDepGui()  # Inicializar componentes y cargar datos
        self.depWin.show()

    def initDepGui(self):
        # Diccionario para guardar clave de estados
        self.estados_dict = {}
        # Cargar la lista de estados en el comboBox
        self.cargar_estados()
        # Conectar evento: cuando cambia estado, cargar municipios
        self.depWin.cB_Estados.currentIndexChanged.connect(self.cargar_municipios)
        # Poner foco en el campo de número de documento
        self.depWin.linEdNumDoc.setFocus()
        # Aplicar estilo CSS al botón PB2
        self.depWin.PB2.setStyleSheet(stylesheet)

    def cargar_estados(self):
        try:
            # URL API para obtener estados
            url = "https://gaia.inegi.org.mx/wscatgeo/mgee/"
            respuesta = requests.get(url)
            datos = respuesta.json()
            estados = datos.get("datos", [])

            print("Estados: ", estados)

            # Agregar opción inicial para seleccionar estado
            self.depWin.cB_Estados.addItem("Selecciona un estado", "")

            # Agregar cada estado al comboBox con su clave
            for estado in estados:
                nombre = estado["nom_agee"]
                clave = estado["cvegeo"]
                self.depWin.cB_Estados.addItem(nombre, clave)
                self.estados_dict[nombre] = clave

        except Exception as e:
            # Mostrar error si falla la carga
            QMessageBox.critical(self, "Error", f"No se pudieron cargar los estados:\n{e}")

    def cargar_municipios(self):
        # Obtener clave del estado seleccionado
        estado_clave = self.depWin.cB_Estados.currentData()

        # Limpiar comboBox de municipios y agregar opción inicial
        self.depWin.cB_Municipios.clear()
        self.depWin.cB_Municipios.addItem("Selecciona una ciudad", "")

        if not estado_clave:
            # Si no hay estado seleccionado, salir
            return

        try:
            # URL API para obtener municipios según el estado
            url = f"https://gaia.inegi.org.mx/wscatgeo/v2/mgem/{estado_clave}"
            respuesta = requests.get(url)
            datos = respuesta.json()
            municipios = datos.get("datos", [])

            # Agregar municipios al comboBox
            for municipio in municipios:
                self.depWin.cB_Municipios.addItem(municipio["nomgeo"])

        except Exception as e:
            # Mostrar error si falla la carga
            QMessageBox.critical(self, "Error", f"No se pudieron cargar los municipios:\n{e}")

# Código para ejecutar la ventana de forma independiente
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Depositowindow()
    sys.exit(app.exec())
