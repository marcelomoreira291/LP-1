lista_teste = ["Marcelo", 29, 85, 1.7, "Mombaça"]
'''
def recebe_lista (lista_teste, troca, i):
    lista_teste [i] = troca
    return lista_teste

def pinicar(lista_teste, n1, n2, n3):
    n1 = lista_teste range[ : 2]
    n2 = lista_teste range [2:3]
    n3 = lista_teste range [ : -4] 

recebe_lista(lista_teste, 81, 3)
print (lista_teste)


pinicar(lista_teste, n1, n2, n3)
print (n1, n2, n3)
'''
'''
codigo Edinara
biografia = ["Edinara", 21, "Mombaça", 50.60, 1.67]

def modifica(lista):
    return(lista)

def recorte(modifica, n1, n2, n3):
    print(f'''
       # {modifica[n1:n2]}
        #{modifica[n3:]}
        #{modifica[:n2]}
'''

recorte(modifica(biografia), 2, 4, 1)
'''
'''
lista2 = [0, 1, 2, 3, 4, 5]

nova_lista = [x - 1 for x in lista2]
print (nova_lista)
'''
nome = "Marcelo"
tupla = tuple (nome)
lista_tupla = list (tupla)
lista_tupla.append("M")
tupla_nova = tuple (lista_tupla)
print (tupla_nova)