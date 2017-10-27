import time
from datetime import datetime, date, time


class produto:
    def __init__(self, codigo, descr, valUni):
        self.__codigo = codigo
        self.__descr = descr
        self.__valUni = valUni
        self.__qtd = 0

    def __init__(self, codigo, descr, valUni,qtd):
        self.__codigo = codigo
        self.__descr = descr
        self.__valUni = valUni
        self.__qtd = qtd

    def setCodigo(self,codigo):
        self.__codigo = codigo
    def setDescr(self, descr):
        self.__descr = descr
    def setValUni(self, valUni):
        self.__valUni = valUni
    def setQtd(self, qtd):
        self.__qtd = qtd
    def getCodigo(self):
        return self.__codigo
    def getDescr(self):
        return self.__descr
    def getValUni(self):
        return self.__valUni
    def getQtd(self):
        return self.__qtd

class totalVenda:
    def __init__(self, codprod, qtd):
        self.__codProd = codprod
        self.__qtd = qtd

    def setCodProd(self,codProd):
        self.__codProd = codProd

    def setQtd(self, qtd):
        self.__qtd = qtd

    def getCodProd(self):
        return self.__codProd

    def getQtd(self):
        return self.__qtd
