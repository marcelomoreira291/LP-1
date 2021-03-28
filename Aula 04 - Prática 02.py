#11- Escreva um programa que receba as medidas dos lados de um triângulo e calcule sua área e perímetro.


def calcula_Area (base, altura):
    area = base * altura / 2
    return area


def calcula_Perimetro (base, altura, comprimento):
    perimetro = base + altura + comprimento
    return perimetro


print ('Digite as medisas solicitadas')
base = int (input('Medida da base: '))
altura = int (input ('Medida da altura: '))
comprimento = int (input ('Medida do comprimento: '))
print ('\nA Área do triângulo é: ', calcula_Area(base, altura))
print ('O perímetro do triângulo é: ', calcula_Perimetro(base, altura, comprimento))