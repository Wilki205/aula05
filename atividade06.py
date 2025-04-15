pin = 1234
tentativas = 1
senha = int(input("Digite sua senha: "))
while senha != pin and tentativas < 3:
        senha = int(input("tente novamente: "))
        tentativas += 1
if senha ==pin:
        print ("Acesso liberado!")
else:
    print ("Acesso bloqueado!")