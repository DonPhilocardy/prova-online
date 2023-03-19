#  Criar um vetor de cinco posições, solicitar  cinco números e ao fim,
#  imprimir o valor apresentado na posição três.

vetor = []

num1 = int(input("Digite o primeiro número: "))
vetor.append(num1)
num2 = int(input("Digite o segundo número: "))
vetor.append(num2)
num3 = int(input("Digite o terceiro número: "))
vetor.append(num3)
num4 = int(input("Digite o quarto número: "))
vetor.append(num4)
num5 = int(input("Digite o quinto número: "))
vetor.append(num5)

print("\nO valor apresentado na posição três é:", vetor[2])
