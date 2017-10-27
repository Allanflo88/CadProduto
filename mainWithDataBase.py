# usr/bin/python3
# -*- coding: utf-8 -*-

import MySQLdb
import model


produtos = []
con = MySQLdb.connect(host="localhost",user="root",passwd="Andreia16")

cursor = con.cursor()

x = int(input("deseja (re)criar Banco de dados? 1 - sim ou 2 - não "))
if x == 1:
    cursor.execute("drop database if exists Testes")
    cursor.execute("create database Testes")
    cursor.execute("use Testes")

    cursor.execute("drop table if exists produto")

    sql = """create table produto(cod int auto_increment primary key,descr varchar(20) not null,valUni float(5) not null,qtd int);"""

    cursor.execute(sql)

    cursor.execute("drop table if exists erros")

    sql = """create table erros(id int auto_increment primary key,erro varchar(20) not null);;"""

    cursor.execute(sql)

descr = ""
valUni = 0.00
qtd = 0


totProd = int(input("Quantos produtos deseja inserir? "))

for i in range(totProd):
    descr = raw_input("Descrição: ")
    valUni = float(input("Valor Unitário: "))
    qtd = int(input("Quantidade: "))
    try:
        sql = """insert into produto(descr, valUni, qtd) values('{0}', '{1}', '{2}')""".format(descr, valUni, qtd)
        cursor.execute(sql)
        con.commit()
    except:
        sql_erro = """insert into erros(erro) values('Erro na inserção')"""
        cursor.execute(sql_erro)
        con.commit()

sql_select = "select * from produto"

try:
    cursor.execute(sql_select)
    results = cursor.fetchall()
    print("{0} {1:10} {2} {3}".format('Codigo', 'Descricao', 'Valor', 'Quantidade'))

    for row in results:
        cod = row[0]
        descricao = row[1]
        valor = row[2]
        qtde = row[3]
        produtos.append(model.produto(cod, descricao, valor, qtde))
    c = 0
    for c in range(len(produtos)):
        print("{0:5} {1:10} {2:5} {3:5}".format(produtos[c].getCodigo(), produtos[c].getDescr(), produtos[c].getValUni(), produtos[c].getQtd()))
except:
    sql_erro = """insert into erros(erro) values('Erro na leitura')"""
    cursor.execute(sql_erro)
    con.commit()

con.close()
