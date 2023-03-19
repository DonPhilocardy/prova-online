
num1 = int(input("\nDigite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))
num3 = int(input("Digite o terceiro número:"))
num4 = int(input("Digite o quarto número:"))
num5 = int(input("Digite o quinto número:"))

maior = num1
menor = num1

if num2 > maior:
    maior = num2
elif num2 < menor:
    menor = num2

if num3 > maior:
    maior = num3
elif num3 < menor:
    menor = num3

if num4 > maior:
    maior = num4
elif num4 < menor:
    menor = num4

if num5 > maior:
    maior = num5
elif num5 < menor:
    menor = num5

print("\nO maior número é:", str(maior))
print("O menor número é:", str(menor))
