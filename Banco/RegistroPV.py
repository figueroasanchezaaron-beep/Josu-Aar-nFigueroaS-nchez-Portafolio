"""Josue Aaron Figueroa Sanchez
    No. Control: 23420335"""

import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox, QDialog, QApplication
from data.transferenciaD import TransferenciaData
from model.movimientos import Transferencia


class RegistroWindow(QDialog):
    def __init__(self):
        super(RegistroWindow, self).__init__()
        # Cargar la interfaz gráfica desde archivo .ui
        self.regWin = uic.loadUi("gui/RegistroT.ui")  # activar p/ ejecutar aplicacion
        # self.regWin = uic.loadUi("RegistroT.ui")  # activar para ejecucion local
        self.regWin.setWindowTitle("Registro")
        self.initRegGUI()  # inicializar conexiones y configuración de la GUI
        self.regWin.show()  # mostrar la ventana

    def initRegGUI(self):
        # Conectar el botón de registro a la función registrarTransaction
        self.regWin.pushBotRegTransac.clicked.connect(self.registrarTransaction)

    def registrarTransaction(self):
        # Imprimir para depuración
        print("registrarTransaction")

        # Obtener valores de la GUI
        tipoDoc = self.regWin.cBox_TipoDoc.currentText()
        motivoGiro = self.regWin.cBox_MotGiro.currentText()
        numDoc = self.regWin.linEdNumDoc.text()
        monto = self.regWin.linEdMonto.text()
        transfInter = self.regWin.chekBoxTransInter.isChecked()
        dollars = self.regWin.chekBoxDolares.isChecked()

        # Imprimir valores para depuración
        print("tipoDoc", tipoDoc)
        print("motivoGiro", motivoGiro)
        print("numDoc", numDoc)
        print("monto", monto)
        print("transfInter", transfInter)
        print("dolares", dollars)

        # Inicializar variables para acumulación de errores
        error = ''
        e = ''

        # Validaciones de campos obligatorios y formato correcto
        if tipoDoc == '':
            error = "Seleccione el tipo de documento \n"
            e = e + '1'
        if motivoGiro == '':
            error = error + "Seleccione el motivo giro \n"
            e = e + '2'
        if numDoc == '':
            error = error + "Ingrese el numero de documento \n"
            e = e + '3'

        try:
            # Verificar que monto sea un entero positivo distinto de cero
            if monto == '' or int(monto) == 0:
                error = error + "Ingrese el monto"
                e = e + '4'
        except:
            # Capturar error si monto no es numérico
            error = error + "Tipo de dato incorrecto en monto"
            e = e + '4'

        # Si no hay errores, crear objeto Transferencia y registrar
        if error == '':
            Regtransferencia = Transferencia(
                tipo=tipoDoc,
                documento=numDoc,
                motivo=motivoGiro,
                monto=monto,
                transfIntern=transfInter,
                monedaDolares=dollars
            )

            objTransData = TransferenciaData()
            res = objTransData.registrar(Regtransferencia)  # registrar en BD
            msbox = QMessageBox()
            msbox.setWindowTitle("Registrar")

            # Mostrar mensaje según resultado del registro
            if res == 1:
                msbox.setText("Registro Almacenado con Éxito")
                self.limpiarGuiRegistro()  # limpiar campos de la GUI
            else:
                msbox.setText("Error en registrar")
            msbox.exec()
        else:
            # Mostrar errores acumulados y enfocar el primer campo erróneo
            self.msgError(error)
            match e[0]:
                case '1':
                    self.regWin.cBox_TipoDoc.setFocus()
                case '2':
                    self.regWin.cBox_MotGiro.setFocus()
                case '3':
                    self.regWin.linEdNumDoc.setFocus()
                case '4':
                    self.regWin.linEdMonto.clear()
                    self.regWin.linEdMonto.setFocus()

    def msgError(self, msg):
        # Mostrar cuadro de mensaje con errores
        msbox = QMessageBox()
        msbox.setWindowTitle("Errores en entrada")
        msbox.setText(msg)
        msbox.exec()

    def limpiarGuiRegistro(self):
        # Limpiar todos los campos de la GUI y resetear valores
        self.regWin.cBox_TipoDoc.setCurrentIndex(-1)
        self.regWin.cBox_MotGiro.setCurrentIndex(-1)
        self.regWin.linEdNumDoc.clear()
        self.regWin.linEdMonto.clear()
        self.regWin.chekBoxTransInter.setChecked(False)
        self.regWin.checkBoxDolares.setChecked(False)
        self.regWin.chekBoxDolares.setFocus()
