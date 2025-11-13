nome = input("nome: ")
notas = ()
for i in range (1,4):
    nota = float(input(f"nota{i}: "))
    notas = notas + (nota,)
media = sum(notas)/3
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