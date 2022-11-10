login = str(input("Digite seu nome de Login: "))
senha = str(input("Digite sua senha: "))

while senha == login:
    print("Sua senha não pode ser igual seu login. Por favor, altere seus dados:")
    login = str(input("Digite seu nome de Login: "))
    senha = str(input("Digite sua senha: "))



