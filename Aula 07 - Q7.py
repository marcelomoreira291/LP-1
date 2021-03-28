lista1 = []
lista2 = []

lista1 = [int(input("Digite o cod dos itens: ")) for i in range(4)]
set1= set(lista1)
print(set1)

lista2 = [int(input("Digite o cod dos itens: ")) for i in range(4)]
set2= set(lista2)

print(set2)

print("D = diferença, U = União ou I = Intersecção\n")

op = input("Operação: ")
def opcao(set1, set2, op):
    if op == "D":
        print(set1 - set2)
    elif op == "U":
        print(set1 | set2)
    elif op == "I":
        print(set1.intersection(set2))
       
    else:
        print("Não existe essa opção")
x = opcao(set1, set2, op)
print(x)
