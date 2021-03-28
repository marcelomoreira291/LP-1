# Marcelo

nome = 'marcelo'

def dicionario(nome, limite):
    dic = {x:[x for x in range(0, limite ) if x % 2 == 0] for x in nome}
    print(dic)
dicionario(nome, 10)