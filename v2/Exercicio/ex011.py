# faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
# de tinta neessária para pinta-la, sabendo que cada litro de tinta pinta uma área de 2m²

larg = float(input('Digite a largura da parede: '))
altu = float(input('Digite a altura da parede: '))
quadrado = larg * altu
tinta = quadrado / 2
print(f'Será necessário {tinta} de litros de tinta para pintar a parede que tem {quadrado} m²')
