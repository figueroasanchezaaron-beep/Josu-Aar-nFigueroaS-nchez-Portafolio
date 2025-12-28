"""Josue Aaron Figueroa Sanchez
    No. Control: 23420335"""

from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QApplication
from gui.RegistroPV import RegistroWindow
from gui.DepositoPV import Depositowindow

class MainGUI(QMainWindow):
    def __init__(self):
        super(MainGUI, self).__init__()
        # Cargar la interfaz principal desde archivo .ui
        self.maingui = uic.loadUi("gui/mainBnko.ui")
        # Inicializar conexiones y configuraciones de la GUI
        self.initMainGui()
        # Mostrar la ventana maximizada
        self.maingui.showMaximized()

    def initMainGui(self):
        # Conectar la acción o botón "btnRegTransf" para abrir registro de transferencias
        self.maingui.btnRegTransf.triggered.connect(self.registrarTrans)

    def registrarTrans(self):
        # Crear y mostrar la ventana para registrar transferencias
        self.RegistroGUI = RegistroWindow()

