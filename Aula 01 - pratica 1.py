'''
def nome_inserido(nome):
    return nome


def idade_inserida(idade):
    return idade 


def estado_civil_inserido(estado_civil):
    return estado_civil


def genero_inserido(genero):
    return genero

#Programa Principal
nome = input ('Qual seu nome?: ')
idade = int (input('Qual sua idade?: '))
estado_civil = input ('Qual seu Estado Civil?: ')
genero = input ('Qual seu Gênero?: ')
print ('\n')
print ('Seu nome é: ', nome_inserido(nome))
print ('Sua idade é: ', idade_inserida(idade))
print ('Seu estado civil é: ', estado_civil_inserido(estado_civil))
print ('Seu gênero é: ', genero_inserido(genero))
'''

from  time import sleep 
import os
x = 9
while x > 0:
    for contagem in range(1):
        sleep(2)
        print(x)
        x = x-2    
os.system('clear')  
print('Lançar!')