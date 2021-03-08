def tinder(pessoa1, pessoa2):
    if ((pessoa1 == 'c' or 'C') and (pessoa2 == 'c' or 'C')):
        print ('\n')
        print ('Deixa quieto!')
        print ('\n')
    elif ((pessoa1 == 's' or 'S') and (pessoa2 == 's' or 'S')):
        print ('\n')
        print ('Bora!')
        print ('\n')
    else:
        print ('Opção Inváilida!')


#Programa Principal
print ('-'*50)
print ('                TINDER DO PYTHON             ')
print ('-'*50)
print ('\n')
print ('Escolha S para Solteiro ou C para Casado')
pessoa1 = input ('Você: ')
pessoa2 = input ('O crush: ')
tinder(pessoa1, pessoa2)
