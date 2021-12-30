numero = int(input("Você quer saber a tabuada do número:"))
print("\n Tabuada número " + str(numero) + "\n")
for valor in range(0, 10+1, 1):
    print("\t "+str(valor) + " X " + str(numero) + " = " + str(numero*valor))

