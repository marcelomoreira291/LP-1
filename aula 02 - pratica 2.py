def idade_em_minutos(idade):
    minutos = idade * 525600
    print ('Sua idade em minutos é {} min' .format (minutos))

idade = int (input ('Qual sua idade?: '))
idade_em_minutos(idade)
