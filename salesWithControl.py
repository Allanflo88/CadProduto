# usr/bin/python3
# -*- coding: utf-8 -*-

import MySQLdb
import model
import time
from datetime import datetime, date, time, timedelta

vendas = []
produtos = []

bd = control.BD("localhost","root","Andreia16")

x = int(input("Deseja criar tabela vendas? 1 - sim ou 2 - não "))
if x == 1:
    bd.criaTBVendas()

produtos = bd.selectTBProduto()

while(1):
    x = int(input("Nova venda? 1-sim 2-não:"))
    if(x == 2):
        break
    c = 0
    print("{0} {1:10} {2} {3}".format('Codigo', 'Descricao', 'Valor', 'Quantidade'))
    for c in range(len(produtos)):
        print("{0:5} {1:10} {2:5} {3:5}".format(produtos[c].getCodigo(), produtos[c].getDescr(), produtos[c].getValUni(), produtos[c].getQtd()))

    now = datetime.now()
    item = int(input("Código Item:"))
    quantidade = int(input("Quantidade: "))
    print("Total compra: R$ {0}".format(float(produtos[item - 1].getValUni()) * quantidade))
    bd.insereTBVendas(now, item, quantidade);
    
bd.EncerrarDia()
con.close()
