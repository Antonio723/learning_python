#faça um programa que leia quanto uma pessoa tem na carteir e mostre quantos dolares ela pode comprar
# considere us$1.00=R$3.27
r = float(input('Quantos reais você têm na carteira? R$'))
conversao_dolar = r/5.23
print(f'Você pode comprar ', round(conversao_dolar,2),'dolar')
conversao_euro = (r/5.88)
print(f'O valor em euro é:',round(conversao_euro,2))
