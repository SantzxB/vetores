import os 

os.system("cls||clear")
vetor_notas = []
quantidade_notas = 3

for i in range(quantidade_notas):
    nota =  float(input(f"Digite a {i +1}ª nota: "))
    vetor_notas.append(nota)

print("\n Exibindo Informações \n")
for uma_nota in vetor_notas:
    print(f"Notas: {uma_nota}")

