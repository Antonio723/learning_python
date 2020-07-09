# Crie um programa que leia um número Real qualquer pelo teclado e mostre a sua porção inteira
# Ex: 6.127
# o número 6.127 têm a parte inteira 6

from math import floor

p = float(input('Digite um número'))
print(f'O número digitado foi {p} e o sua porção inteira foi ', floor(p))
