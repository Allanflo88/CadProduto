# usr/bin/python3
# -*- coding: utf-8 -*-

import MySQLdb
import model
import time
from datetime import datetime, date, time, timedelta

vendas = []
produtos = []

con = MySQLdb.connect(host="localhost",user="root",passwd="Andreia16",db="Testes")
cursor = con.cursor()

x = int(input("Deseja criar tabela vendas? 1 - sim ou 2 - não "))
if x == 1:
    cursor.execute("drop table if exists vendas")

    sql = """create table vendas(cod int auto_increment primary key,data datetime not null,codprod int not null,qtd int not null);"""

    cursor.execute(sql)

    sql = """alter table add constraint fk_vendas foreign key(codprod);"""

sql_select = "select * from produto"
try:
    cursor.execute(sql_select)
    results = cursor.fetchall()


    for row in results:
        cod = row[0]
        descricao = row[1]
        valor = row[2]
        qtde = row[3]
        produtos.append(model.produto(cod, descricao, valor, qtde))

except:
    sql_erro = """insert into erros(erro) values('Erro na leitura')"""
    cursor.execute(sql_erro)
    con.commit()

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
    try:
        sql = """insert into vendas(data, codprod, qtd) values('{0}', '{1}', '{2}')""".format(now.strftime('%Y-%m-%d %H:%M:%S'), item, quantidade)
        cursor.execute(sql)
        con.commit()
    except:
        sql_erro = """insert into erros(erro) values('Erro na inserção do item {}')""".format(item)
        cursor.execute(sql_erro)
        con.commit()

sql_select = "select codprod, sum(qtd) from vendas where data between '{0}' and '{1}' group by codprod;".format(now.strftime('%Y-%m-%d'),(now + timedelta(days=1)).strftime('%Y-%m-%d'))
try:
    cursor.execute(sql_select)
    results_total = cursor.fetchall()

    for row in results_total:
        cod = row[0]
        total = row[1]
        vendas.append(model.totalVenda(cod, total))

except:
    sql_erro = """insert into erros(erro) values('Erro na leitura')"""
    cursor.execute(sql_erro)
    con.commit()
for c in range(len(vendas)):
    try:
        sql = """update produto set qtd = qtd - '{0}' where cod = '{1}';""".format(vendas[c].getQtd(), vendas[c].getCodProd())
        cursor.execute(sql)
        con.commit()
    except:
        sql_erro = """insert into erros(erro) values('Erro no update')"""
        cursor.execute(sql_erro)
        con.commit()


con.close()
