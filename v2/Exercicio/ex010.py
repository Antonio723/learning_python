# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
# Considere US$ 1.00 == R$ 3.27

money = float(input('Digite quanto você tem na carteira: '))
print(f'Com {money} você poderá comprar {money/3.27} dólares')
