# usr/bin/python3
# -*- coding: utf-8 -*-

import MySQLdb
import model

class BD:
    def __init__(self, Host, usuario, senha):
        self.__con = MySQLdb.connect(host=Host,user=usuario,passwd=senha)
        self.__cursor = self.__con.cursor()

    def closeBD(self):
        self.__con.close()

    def criaBD(self):
        self.__cursor.execute("drop database if exists Testes")
        self.__cursor.execute("create database Testes")
        self.__cursor.execute("use Testes")

    def criaTbProdutos(self):
        self.__cursor.execute("use Testes")
        self.__cursor.execute("drop table if exists produto")
        self.__cursor.execute("""create table produto(cod int auto_increment primary key,descr varchar(20) not null,valUni float(5) not null,qtd int);""")
        self.__cursor.execute("drop table if exists erros")
        self.__cursor.execute("""create table erros(id int auto_increment primary key,erro varchar(20) not null);""")

    def criaTBVendas(self):
        self.__cursor.execute("use Testes")
        self.__cursor.execute("drop table if exists vendas")
        self.__cursor.execute(create table vendas("cod int auto_increment primary key,data datetime not null,codprod int not null,qtd int not null);")
        self.__cusor.execute("alter table add constraint fk_vendas foreign key(codprod);")

    def insereTBProduto(self, descr, valUni, qtd):
        try:
            sql = """insert into produto(descr, valUni, qtd) values('{0}', '{1}', '{2}')""".format(descr, valUni, qtd)
            self.__cursor.execute(sql)
            self.__con.commit()

            return 1
        except:
            sql_erro = """insert into erros(erro) values('Erro na inserção')"""
            self.__cursor.execute(sql_erro)
            self.__con.commit()

            return -1

    def selectTBProduto(self):
        sql_select = "select * from produto"
        produtos = []

        try:
            self.__cursor.execute(sql_select)
            results = self.__cursor.fetchall()
            for row in results:
                cod = row[0]
                descricao = row[1]
                valor = row[2]
                qtde = row[3]
                produtos.append(model.produto(cod, descricao, valor, qtde))

            return produtos
        except:
            sql_erro = """insert into erros(erro) values('Erro na leitura')"""
            self.__cursor.execute(sql_erro)
            self.__con.commit()

    def insereTBVendas(self, now, item, quantidade):
        try:
            sql = """insert into vendas(data, codprod, qtd) values('{0}', '{1}', '{2}')""".format(now.strftime('%Y-%m-%d %H:%M:%S'), item, quantidade)
            self.__cursor.execute(sql)
            self.__con.commit()
        except:
            sql_erro = """insert into erros(erro) values('Erro na inserção do item {}')""".format(item)
            self.__cursor.execute(sql_erro)
            self.__con.commit()

    def EncerrarDia(self):
        vendas = []
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
