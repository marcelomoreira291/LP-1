#Programa Principal
print ('-'*50)
print ('        SISTEMA PARA CONSULTA DE DESCONTO              ')
print ('-'*50)
print ('\n')
print ('O Desconto do Produto será de acordo com a Categoria')
preço = float (input('Digite o preço do produto: '))


def consulta_desconto (preço):
    if preço <= 20.00:
        desconto = preço * (20/100)
        categoria = 5
        print ('Categoria:{categoria}\nParabéns! Seu desconto é de 20%')
        print (f'De R${preço} por apenas R${desconto}')
    elif preço > 20.00 <= 50.00:
        desconto = preço * (15/100)
        categoria = 4
        print ('Categoria:{categoria}\nParabéns! Seu desconto é de 20%')
        print (f'De R${preço} por apenas R${desconto}')
    elif preço > 50.00 <= 100.00:
        desconto = preço * (10/100)
        categoria = 3
        print ('Categoria:{categoria}\nParabéns! Seu desconto é de 20%')
        print (f'De R${preço} por apenas R${desconto}')

        