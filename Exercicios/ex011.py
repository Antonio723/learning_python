 # Elabre um programa que leia a largura e a altra de uma parede em metros,
 # calcule a sua área e a quantidade de
 # tinte necessaria para pinta-la, sabendo que cada litro de tinta pinta uma area de 2m²

altura=float(input('Qual a altura da parede:'))
largura=float(input('Qual a largura da parede:'))

print(f'As dimensoes dessa parde são de {altura} X {largura} e têm {altura*largura}m²')
print(f'A quantidade de tinta necessaria para pintala é de {( altura * largura) / 2 } litros de tinta')