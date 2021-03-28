'''
Escreva uma função que receba o total de vendas de um funcionário no período de 1 mês e seu nome. 
Se o valor total de suas vendas for maior que a metade do salário, o funcionário 
deve receber um adicional de 50%, caso não seja, ele recebe apenas o salário bruto. 
Retorne quanto o funcionário irá receber no mês. O valor do salário deve estar 
armazenado em uma variável global e o nome do funcionário deve ser um parâmetro opcional.
'''


def verificaVendas (total_vendas, nome_vendedor = 'Rómulo'):
    if total_vendas > 550.00:
        global salario
        salario += 550
        print (f'\nParabéns {nome_vendedor}! Você atingil a meta. Seu salário este mês é R${salario}\n')
    else:
        print (f'\nQue pena {nome_vendedor}! Você não atingil a meta. Seu salário este mês é R${salario}\n')

#Programa Principal
salario = float (1100.00)
total_vendas = float (input('\nDigite o valor em vendas: '))
verificaVendas(total_vendas)