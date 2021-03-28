def login (nome='José', senha = 'admin'):
    usuario = nome

    if nome == '':
        print ('nome inválido')
    elif usuario == nome and senha == senha:
        print ('Acesso concedido')
    else:
        print ('acesso negado')


login ('José', 'admin')