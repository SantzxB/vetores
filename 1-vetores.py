import os

os.system("cls")

list = []
soma = 0
media = 0
for i in  range(3):
 nota = float(input(f"Digite {1 + i}ª nota: "))
 list.append(nota)
 soma += nota
 media = soma / 3

print(f"Nota: {list}")
print(f"Soma: {soma}")  
print(f"Média: {media:.2f}")
