
##Version 01

# nome = input("Digite o seu nome: ")
# idade = int(input("Digite a sua idade"))

# if idade >= 65:
#     print("O paciente " + nome + " POSSUI atendimento prioritário!")
# else:
#     print("O paciente " + nome + " NÃO POSSUI atendimento prioritário!")


## Version 02

# nome=input("Digite o nome: ")
# idade=int(input("Digite a idade: "))
# doenca_infectocontagiosa=input("Suspeita de doença infecto-contagiosa?").upper()

# if idade>=65:
#     print("O paciente " + nome + " POSSUI atendimento prioritário!")
# elif doenca_infectocontagiosa=="SIM":
#     print("O paciente " + nome + " deve ser direcionado para sala de espera reservada.")
# else:
#     print("O paciente " + nome + " NÃO possui atendimento prioritário e pode aguardar na sala comum!")


## Version 03
nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
doenca_infectocontagiosa=input("Suspeita de doença infecto-contagiosa?").upper()
if idade>=65 and doenca_infectocontagiosa=="SIM":
    print("O paciente será direcionado para sala AMARELA - COM prioridade")
elif idade < 65 and doenca_infectocontagiosa == "SIM":
    print("O paciente será direcionado para sala AMARELA - SEM prioridade")
elif idade >= 65 and doenca_infectocontagiosa == "NAO":
    print("O paciente será direcionado para sala BRANCA - COM prioridade")
elif idade < 65 and doenca_infectocontagiosa == "NAO":
    print("O paciente será direcionado para sala BRANCA - SEM prioridade")
else:
    print("Responda a suspeita de doença infectocontagiosa com SIM ou NAO")


