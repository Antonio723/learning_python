# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade
# de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa por dia
# R$ 60.00 e R$ 0.15 por Km rodado.

dias = int(input('Quantos dias o carro foi alugado: '))
distanciaInicial = float(input('Quantos Km o veiculo possuia antes de ser alugado: '))
distanciaFinal = float(input('Quantos Km o veiculo possui na devolução: '))

valorDistancia = (distanciaFinal-distanciaInicial)*0.15
valorDias = dias*60
print(f'O valor a ser pago é de R$ {valorDias+valorDistancia:.2f},'
      f' referentes a {dias} dia(s) e {distanciaFinal-distanciaInicial}Km(s)')
