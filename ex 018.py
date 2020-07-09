# Faça um programa que leia um ângulo qualqer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

import math
angulo = float(input('Digite o ângulo:'))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print(f'O ângulo de {angulo}° equivale ao seno {sen :.2f}')
print(f'O ângulo de {angulo}° equivale ao cosseno  {cos :.2f}')
print(f'O ângulo de {angulo}° equivale a tangente {tan :.2f}')
