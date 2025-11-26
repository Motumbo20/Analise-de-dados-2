def mediaa(a):
    return (a)/3
def situacao(situacao):
    if media >= 7:
        situacao = "aprovado"
    elif media >= 5:
        situacao = "recuperacao"
    else:
        situacao = "reprovado"
    return situacao

nome = input("digite seu nome: ")
notas=()
for i in range (1,4):
    nota = float(input(f"digite sua nota{i}°"))
    notas = notas + (nota,)
media= mediaa(sum(notas))
situacaoo = situacao(media)

print(f"sua média é {media} e sua situação é {situacaoo}")

