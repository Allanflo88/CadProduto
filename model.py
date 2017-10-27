class produto:
    def __init__(self, codigo, descr, valUni):
        self.__codigo = codigo
        self.__descr = descr
        self.__valUni = valUni
        self.__qtd = 0

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
