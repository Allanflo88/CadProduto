class produto:
    def __init__(self, codigo, descr, valUni):
        self.codigo = codigo
        self.descr = descr
        self.valUni = valUni
        self.qtd = 0

    def setCodigo(self,codigo):
        self.codigo = codigo
    def setDescr(self, descr):
        self.descr = descr
    def setValUni(self, valUni):
        self.valUni = valUni
    def setQtd(self, qtd):
        self.qtd = qtd
    def getCodigo(self):
        return self.codigo
    def getDescr(self):
        return self.descr
    def getValUni(self):
        return self.valUni
    def getQtd(self):
        return self.qtd
