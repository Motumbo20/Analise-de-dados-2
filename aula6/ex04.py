i = 1
while i <= 3:
    print ("digite o nome do aluno:")
    nome = input("nome:")
    notas = []
    for j in range (1,4):
        nota = float(input(f"digite a sua {j}° nota:"))
        notas.append(nota)
    media = (notas[0] + notas[1] + notas[2])/3
    if media >=7:
        situação = "aprovado"
    elif media >= 5:
        situação = "recuperação"
    else:
        situação = "reprovado"
    print(f"aluno {nome}")
    print(f"notas {notas}")
    print(f"média {media:.2f}")
    print (f"situação {situação}")
    i+=1