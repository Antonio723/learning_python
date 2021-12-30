import datetime
import sysconfig

responsavel = input("Digite o responsável: ")
funcionario = input("Digite o nome do funcionário: ")
evento = input("digite o nome do evevnto: ")
valor = float(input("Digite o valor a ser ressarcido: "))

print("Declar para o senhor " + responsavel + " que o senhor " + funcionario + " esteve presente no evento " + evento + " e gastou o valor de R$" + str(valor) + " com a entrada")
