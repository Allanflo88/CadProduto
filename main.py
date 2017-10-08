import model

produtos = []
c = 0
while(1):
    c += 1
    print("Escreva exit para sair"))
    descr = input("Descricao: ")
    if descr == "exit":
        break
    price = input("Preco:")
    produtos.append(model.produto(c,descr, price))


c -= 1
while(c >= 0):
    print(produtos[c].getDescr())
    c -= 1
