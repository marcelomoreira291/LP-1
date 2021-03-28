"""
Escreva uma função que faça a verificação de existência 
de uma chave dentro de um dicionário. Caso a chave exista 
a função deve retornar o valor da chave, caso ela não 
exista, a função deve adicioná-la e retornar o dicionário.
"""

# Marcelo A

dados_pessoais={'nome':"Marcelo",
                "idade": 27,
                "cidade":'Mombaça',
                "estado_civil":'casado'
                }

chave = input("Chave: ")

def verifica_chave(dados_pessoais, chave):
    if chave in dados
    print(dados_pessoais[chave])
    else:
        dados_pessoais[chave] = "chave adicionada"
        print(dados_pessoais)
        
verifica_chave(dados_pessoais, chave)