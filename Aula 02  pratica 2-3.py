def operação(num1, num2, operando):
    if operando == '*':
        resultado = num1 * num2
        print (f'A Multiplicação de {num1} por {num2} é {resultado}')
    elif operando == '/':
        resultado = num1 / num2
        print (f'A Divisão de {num1} por {num2} é {resultado}')
    elif operando == '+':
        resultado = num1 + num2
        print (f'A Soma de {num1} e {num2} é {resultado}')
    elif operando == '-':
        resultado = num1 - num2
        print (f'A Subtração de {num1} e {num2} é {resultado}')
    else:
        print ('Opção Inválida!')

    
num1 = int (input ('Digite o primeiro número: '))
num2 = int (input ('Digite o segundo número: '))
operando = input ('Digite o operando desejado: \n* Multiplicação \n/ Divisão \n+ Soma \n- Subtração \n')
operação(num1, num2 , operando)
