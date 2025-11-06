final = 0
cont = 0
for i in range (1,6):
    nota= int(input(f"digite a sua {i}° nota:"))
    final += nota
    cont +=1
media = final / cont
if media >=7:
    situacao = "Aprovado"
    print(f"a sua média final é de {media} voce está {situacao}")
elif media >= 5:
    situacao = "Recuperação"
    print(f"a sua média final é de {media} voce foi para {situacao}")
else:
    situacao = "Reprovado"
    print(f"a sua média final é de {media} voce foi {situacao}")