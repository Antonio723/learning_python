#Faça um algoritimo que leia o salario de um funcionario e mostre seu novo salario,
# com 15% de aumento
salario1=float(input('Qual o valor do salario a ser reajustado?'))
salario_reaustado=salario1*1.15
print(f'O valor do salario inicial é de {salario1} e com reajuste ele irá receber ', round(salario_reaustado,2))
