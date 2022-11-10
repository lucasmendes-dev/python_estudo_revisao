alunos = ["José", "Joana", "Maria", "Carla", "Mauricio", "Andre", "Tiago", "Enzo", "Amanda", "Alessandra"]
notas = [
    [10, 9, 8, 8],
    [9, 7, 6, 4],
    [10, 10, 10, 10],
    [5, 3, 10, 9],
    [7, 6, 6, 6],
    [7, 7, 8, 7],
    [7, 7, 7, 9],
    [8, 5, 6, 7],
    [10, 9, 7, 4],
    [10, 1, 3, 3],
]

lista_medias = []

for media in notas:
    media_aluno = sum(media) / len(media)
    lista_medias.append(media_aluno)

for i in range(len(alunos)):
    print(f"O aluno {alunos[i]} tirou a média de {lista_medias[i]}")

contador = 0
for nota in lista_medias:
    if nota >= 7:
        contador += 1;

print(f"Houveram {contador} alunos com média acima de 7.")