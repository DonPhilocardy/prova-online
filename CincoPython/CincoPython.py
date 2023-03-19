#  Crie uma matriz bidimensional. Deverá ser solicitado três nomes de alunos
#  e quatro notas, após solicitação dos nomes e das notas deverá ser impresso os
#  nomes acompanhados da média geral de cada aluno, deverá ser impresso também o
#  nome do aluno que obteve a maior média e o nome do aluno que obteve a menor
#  média.

matriz = []

alunos = []
notas = []
media_geral = 0
medias = 0
maior_media = 0
menor_media = 10
nome_aluno_maior_media = ""
nome_aluno_menor_media = ""
for aluno in range(3):
    nota_aluno = []
    nome_aluno = input(f"digitar o nome do aluno {aluno + 1}: ")
    adicionar_nota = 0

    for i in range(4):
        nota = int(input(f"digitar a nota {i+1} do {nome_aluno}: "))
        nota_aluno.append(nota)
        adicionar_nota += nota
    media = adicionar_nota / 4
    if media > maior_media:
        maior_media = media
        nome_aluno_maior_media = nome_aluno

    if media < menor_media:
        menor_media = media
        nome_aluno_menor_media = nome_aluno

    print(f"{nome_aluno} \n media: {media}")
    medias += media
    alunos.append(nome_aluno)
    notas.append(nota_aluno)
matriz.append(alunos)
matriz.append(notas)

media_geral = "%.2f" % (medias / 3)
print(f"o aluno que obtive a maior média é {nome_aluno_maior_media}")
print(f"o aluno que obtive a menor média é {nome_aluno_menor_media}")

