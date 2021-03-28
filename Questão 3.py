#Questão 3
#Tempo perdido fumando em segundos
def tempo_Vida(quantidade, anos):
    dias = anos * 365 
    minutos_perdidos = ((quantidade * 10) / 1440)
    total_perdido = minutos_perdidos * dias
    return total_perdido
    
quantidade = int (input("Digite a quantidade de cigarros fumados por dia: "))
anos = int (input("Digite a quantidade de anos você já fumou: "))
segundos_perdidos = tempo_Vida(quantidade, anos) * 24 * 60 * 60

print(f'Seu tempo de vida perdido foi: {segundos_perdidos} segundos')
