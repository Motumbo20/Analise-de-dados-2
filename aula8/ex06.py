def descontofinal(x):
    if x >= 500:
        desconto = x * 0.09
    elif x >= 200:
        desconto = x * 0.08
    else:
        desconto = x *0.07
    return desconto
def descontocolocado(x):
    precof = preco - (preco*(desconto/preco))
    return precof
preco = int(input("digite o preco do seu produto: "))
desconto = descontofinal(preco)
final = descontocolocado(preco)
print(f"o seu produto teve desconto de {desconto} e no final ficou no total de {final}")

