import model

produtos = []
c = 0
while(1):
    c += 1
    print("Escreva exit para sair")
    descr = input("Descricao: ")
    if descr == "exit":
        break
    price = input("Preco:")
    produtos.append(model.produto(c,descr, price))


print("Descricao" + "   " + "Valor Unitario")
for c in range(len(produtos)):
    print(str(produtos[c].getDescr()) + '   ' + str(produtos[c].getValUni()))
    c += 1
