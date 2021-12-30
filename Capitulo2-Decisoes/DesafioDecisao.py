## solução feita
typeUser = input("Qual seu nivél de acesso: ").upper()
userGender = input("Qual o seu genero?").upper()

print("Olá ")
if typeUser == "ADM":
    if userGender == "FEMININO":
        print("administardora")
    else:
        print("administardor")
elif typeUser == "USR":
    if userGender == "FEMININO":
        print("usuária")
    else:
        print("usuário")
elif typeUser == "GUEST":
    print("visitante")
else:
    print("desconhecido(a)")

##Solução proposta
nivel=input("Digite o nível de acesso: ").upper()
if nivel=="ADM" or nivel=="USR":
    genero=input("Digite o seu gênero: ").upper()
    if nivel=="ADM":
        if genero=="FEMININO":
            print("Olá administradora")
        else:
            print("Olá administrador")
    else:
        if genero=="FEMININO":
            print("Olá usuária")
        else:
            print("Olá usuário")
elif nivel=="GUEST":
    print("Olá visitante")
else:
    print("Olá desconhecido(a)")
