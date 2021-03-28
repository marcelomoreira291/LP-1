nome = "marcelo"
def estrutura(nome):
    dic = dic = {x : [x for x in range(7) ] for x in nome}
    #print(dic)
estrutura(nome)

lista_vogais = ['A', 'E', 'I', 'O', 'U']
def vogais(nome, lista_vogais):
    for i in nome:
        if i.upper() in lista_vogais:
            print(i, end = ", ")
vogais(nome, lista_vogais)

print("\n")

def numeros(nome):
    dic = {x : [x for x in range(7) ] for x in nome} 
    for v in dic.values():
        for i in v:
            if i % 2 == 0:
                print(1, end = ", ")

numeros(nome)