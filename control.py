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

    def criaTb(self):
        self.__cursor.execute("use Testes")
        self.__cursor.execute("drop table if exists produto")
        self.__cursor.execute("""create table produto(cod int auto_increment primary key,descr varchar(20) not null,valUni float(5) not null,qtd int);""")
        self.__cursor.execute("drop table if exists erros")
        self.__cursor.execute("""create table erros(id int auto_increment primary key,erro varchar(20) not null);""")

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
