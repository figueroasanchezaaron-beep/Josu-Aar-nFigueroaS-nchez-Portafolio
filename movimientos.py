"""Josue Aaron Figueroa Sanchez
    No. Control: 23420335"""

class Transferencia():

    #Registro de los datos de la transferencia realizada
    def __init__(self, tipo: str, documento:str, motivo:str, monto: int, transfIntern: bool, monedaDolares: bool):
        self.tipo = tipo
        self.documento = documento
        self.motivo = motivo
        self.monto = monto
        self.transfIntern = transfIntern
        self.monedaDolares = monedaDolares