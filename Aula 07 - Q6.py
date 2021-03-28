lista1 = [1, 2, 3, 4, 5]
tupla1 = (6, 7, 8, 9, 10)

def fusao(lista1, tupla1):
    set1 = set(lista1)
    set2 = set(tupla1)

    print(set1 | set2)
fusao(lista1, tupla1)