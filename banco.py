"""Josue Aaron Figueroa Sanchez
    No. Control: 23420335"""

import sys
import os
from PyQt6.QtWidgets import QApplication
from gui.login import Login

class Banco():
    def __init__(self):
        self.clear_screen()  # Limpia la consola al iniciar
        self.app = QApplication([])  # Crea la instancia de la aplicación Qt
        # También se puede usar: QApplication(sys.argv)
        self.log = Login()  # Carga la ventana de login
        sys.exit(self.app.exec())  # Ejecuta el loop principal de la aplicación

    def clear_screen(self):
        # Limpia la pantalla dependiendo del sistema operativo
        if os.name == 'nt':  # Windows
            os.system('cls')
        else:  # Linux, MacOS, etc.
            os.system('clear')
