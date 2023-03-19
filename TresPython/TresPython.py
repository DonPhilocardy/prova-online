# Elabore um programa de computador que realize o cálculo de notas.
# Este programa deverá solicitar o nome do aluno e quatro notas, todo este
#  conjunto deverá estar contido em um laço que confirme se deseja encerrar o
#  programa ou continuar solicitando outros nomes e notas.
# Ao final da solicitação do nome e das notas deverá ser impresso o nome do aluno
# e a sua média, se a nota for  menor que 6 imprimir Reprovado, senão, se a nota
# for igual ou maior que 6, imprimir Aprovado.

while True:
    nome = input("\nDigite o nome do aluno: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    nota4 = float(input("Digite a quarta nota: "))

    media = (nota1 + nota2 + nota3 + nota4) / 4

    if media < 6:
        print("\n", nome, "\nSua média: ", media, "\nReprovado")
    else:
        print("\n", nome, "\nSua média: ", media, "\nAprovado")

    opcao = input("\nDeseja encerrar o programa? (S/N) ")
    if opcao.upper() == "S":
        break
