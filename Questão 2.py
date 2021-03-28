#Questão 2

num1 = int (input ('Digite o primeiro número: '))
num2 = int (input ('Digite o segundo número: '))

def produto (num1, num2):
    resultado = (num1 **4) / (num2 **2)
    return resultado


print (f'O resultado é: {produto(num1, num2)}')