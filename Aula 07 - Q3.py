# Eudasio
acesso_usuario = {'login':'adm',
                  'senha': '123'}

login = input("Usuário: ")
senha = input("Senha: ")

def verificar(acesso_usuario, login, senha):
    if login == "adm" and senha == "123":
        print("Acertou miseravi")
    else:
        print("Sai daqui")

verificar(acesso_usuario, login, senha)