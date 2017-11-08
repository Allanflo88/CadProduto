# usr/bin/python3
# -*- coding: utf-8 -*-

import MySQLdb
import model
import control

bd = control.BD("localhost","root","Andreia16")

x = input("Deseja (re)criar Banco de dados? 1-Sim 2-Não")
if x == 1:
    bd.criaBD()
    bd.criaTbProdutos()
else:
    x = input("Deseja (re)criar Tabelas? 1-Sim 2-Não")
    if x == 1:
        bd.criaTbProdutos()

totProd = int(input("Quantos produtos deseja inserir? "))

for i in range(totProd):
    descr = raw_input("Descrição: ")
    valUni = float(input("Valor Unitário: "))
    qtd = int(input("Quantidade: "))
    if bd.insereTBProduto(descr, valUni, qtd) == -1:
        print("Erro na inserção")

produtos = bd.selectTBProduto()
for c in range(len(produtos)):
    print("{0:5} {1:10} {2:5} {3:5}".format(produtos[c].getCodigo(), produtos[c].getDescr(), produtos[c].getValUni(), produtos[c].getQtd()))

bd.closeBD()
