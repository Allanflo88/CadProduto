# usr/bin/python3
# -*- coding: utf-8 -*-

import MySQLdb
import model

con = MySQLdb.connect(host="localhost",user="root",passwd="Andreia16",db="Testes")
cursor = con.cursor()
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
        con.commit

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
        print("{0:5} {1:10} {2:5} {3:5}".format(cod, descricao, valor, qtde))
except:
    sql_erro = """insert into erros(erro) values('Erro na leitura')"""
    cursor.execute(sql_erro)
    con.commit

con.close()
