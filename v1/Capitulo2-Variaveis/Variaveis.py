
## Version 1
# nome = "Antonio Ailton Goncalves"
# empresa = 'FIAP'
# qtde_funcionarios = 500
# mediaMensalidade = 856.50

##Version 2
nome = input("Digite o nome de um funcionario: ")
empresa = input("Digite a intituição: ")
qtde_funcionarios = int(input("Digite a quantidade de funcionários: "))
mediaMensalidade = float(input("Digite a média da mensalidade: "))

# # print mensagens version1
# print(nome + " trabalha na empresa " + empresa)
# print("Possui: ", qtde_funcionarios, " funcionarios.")
# print("A média da mensalidade é de: " + str(mediaMensalidade))

# print mensagens version2
print(nome + " trabalha na empresa " + empresa)
print("Possui: ", qtde_funcionarios, " funcionarios.")
print("A média da mensalidade é de: " + str(mediaMensalidade))
print("==============Verifique os tipos de dados abaixo:==============")
print("O tipo de dado da variavel [nome] é: ",type(nome))
print("O tipo de dado da variavel [empresa] é: ",type(empresa))
print("O tipo de dado da variavel [qtde_funcionarios] é: ",type(qtde_funcionarios))
print("O tipo de dado da variavel [mediaMensalidade] é: ",type(mediaMensalidade))

