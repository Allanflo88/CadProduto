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
    print("Digite a quantidade do item: " + str(produtos[c - 1].getDescr()))
    produtos[c - 1].setQtd(input())


print("Descricao" + "   " + "Valor Unitario" + "    " + "Quantidade")
for c in range(len(produtos)):
    print(str(produtos[c].getDescr()) + "           " + str(produtos[c].getValUni()) + "            " + str(produtos[c].getQtd()))
    c += 1

totalItens = 0.0
for c in range(len(produtos)):
    totalItens += float(produtos[c].getValUni()) * float(produtos[c].getQtd())

print("Valor total dos itens: " + str(totalItens))
