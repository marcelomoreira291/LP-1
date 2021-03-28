'''
almoço = ["Cuscuz", "Baião", "Macarrão"]
sobremesa = ("Rapadura", "Doce de Liete", "Chouriço com sangue das inimigas")


def engorda(almoço, sobremesa):
    fartura = set()
    fartura.update(almoço, sobremesa)
    print(fartura)

engorda(almoço, sobremesa)
'''
lista = {"jaca", "uva"}
tupla = {"pera", "maça", "uva", "jaca"}
def conjunto (lista, tupla):
    op = tupla.difference(lista)
    print(op)

conjunto(lista, tupla)