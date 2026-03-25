import os

os.system("cls")

list = []

for i in  range(3):
 nota = float(input(f"Digite {1 + i}ª nota: "))
#Adiciona nota no vetor.
 list.append(nota)

 media = sum(list) / 3
#ForEach = percorre o vetor sem informar a quantidade.
#enumerate = atráves da variavél i, numera a quantidade de repetições.
for i, uma_nota in enumerate(list, start=1):
    print(f"{i}ª nota {uma_nota}")
print(f"Média: {media:.2f}")
