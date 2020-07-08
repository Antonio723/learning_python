#Faça um programa que leia opreço de um roduto e mostre seu novo
#preço com 5% de desconto
produto = float(input('Qual o preçodo produto:R$'))
resultado = produto*0.95
print(f'O preçodo produto que custava {produto} com desconto de 5% vai custar R$',round(resultado,2))