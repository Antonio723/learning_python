# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

metro = float(input('Digite o valor em metros: '))
print(f'{metro:.2f} metro(s) convertido em:')
print(f'Centimetro: {metro*100:}  \nMilimetros: {metro*1000}')
