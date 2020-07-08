# Escreva um progarama que pergunte a quantidade de KM percoirridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.Calcule o preço a pagar, sabendo que o carro custa R$60.00 por dia e R$0.15 por Km rodado.

km_inicial = float(input('Quantos Km o carro tinha?'))
km_final = float(input('Quantos Km o carro têm?'))
km_total = (km_final-km_inicial)
dias_usados = float(input('Quantos dias o carro foi usado?'))

km = (km_total*0.15)
dias = (dias_usados*60)

print(f'O total de dias usados é de {dias_usados :.0f} percorendo o total de {km_final-km_inicial :.2f}KM')
print(f'O valor total é de {km+dias :.2f}')
