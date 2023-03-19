#  Solicitar a inserção de 5 números, ao final, imprimir os números pares,
#  números ímpares e a média geral desses números.

num1 = int(input("\nDigite o primeiro número:"))
num2 = int(input("Digite o primeiro número:"))
num3 = int(input("Digite o primeiro número:"))
num4 = int(input("Digite o primeiro número:"))
num5 = int(input("Digite o primeiro número:"))

numPares = ""
numImpares = ""

if num1 % 2 == 0:
    numPares += str(num1) + "  "
else:
    numImpares += str(num1) + "  "

if num2 % 2 == 0:
    numPares += str(num2) + "  "
else:
    numImpares += str(num2) + "  "

if num3 % 2 == 0:
    numPares += str(num3) + "  "
else:
    numImpares += str(num3) + "  "

if num4 % 2 == 0:
    numPares += str(num4) + "  "
else:
    numImpares += str(num4) + "  "

if num5 % 2 == 0:
    numPares += str(num5) + "  "
else:
    numImpares += str(num5) + "  "

print("\nOs números pares: " + numPares)
print("Os números impares: " + numImpares)

media = (num1 + num2 + num3 + num4 + num5) / 5
print("\nA média geral desses números: " + str(media))
