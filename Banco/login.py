"""Josue Aaron Figueroa Sanchez
    No. Control: 23420335"""

from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox, QMainWindow
from data.usuarioD import UsuarioData
from gui.mainGui import MainGUI
from model.user import Usuario


class Login(QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        # Cargar interfaz desde archivo .ui
        self.login = uic.loadUi("gui/Login_01.ui")

        # Inicializar el mensaje vacío en la etiqueta lbMensaje
        self.login.lbMensaje.setText('')

        # Configurar señales y slots de la GUI
        self.initGUI()

        # Mostrar la ventana de login
        self.login.show()

    def initGUI(self):
        # Conectar el botón de acceso al método ingresar
        self.login.btnAcceder.clicked.connect(self.ingresar)

    def ingresar(self):
        # Validar que el usuario tenga al menos 2 caracteres
        if len(self.login.txtUsuario.text()) < 2:
            self.login.lbMensaje.setText('Ingrese un usuario válido')
            self.login.txtUsuario.setFocus()

        # Validar que la contraseña tenga al menos 2 caracteres
        elif len(self.login.txtContrasena.text()) < 2:
            self.login.lbMensaje.setText('Ingrese un password válido')
            self.login.txtContrasena.setFocus()

        else:
            # Limpiar el mensaje de error
            self.login.lbMensaje.setText('')

            # Crear objeto Usuario con los datos ingresados
            usu = Usuario(
                usuario=self.login.txtUsuario.text(),
                clave=self.login.txtContrasena.text()
            )

            # Crear objeto UsuarioData para acceso a la base de datos
            usuData = UsuarioData()

            # Intentar hacer login con el usuario
            res = usuData.login(usu)

            # Imprimir datos ingresados (para debug)
            print(usu._nombre, " ", usu._usuario, " ", usu._clave)

            # Si se obtuvo un usuario válido, imprimir datos (debug)
            if res != None:
                print(res._nombre, " ", res._usuario, " ", res._clave)

            if res:
                # Login exitoso: mostrar mensaje, abrir GUI principal y ocultar login
                self.login.lbMensaje.setText('Acceso correcto')
                self.guiMain = MainGUI()
                self.login.hide()
            else:
                # Login fallido: mostrar mensaje de error
                self.login.lbMensaje.setText('Datos de acceso incorrectos')
