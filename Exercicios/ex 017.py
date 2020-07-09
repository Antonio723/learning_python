#
from math import hypot
ca = float(input('Digite o tamanho do cateto adjacente:'))
co = float(input('Digite o tamanho do cateto oposto:'))

resultado = hypot(co, ca)
print(f'A hipotenusa vale {resultado :.2f}')
