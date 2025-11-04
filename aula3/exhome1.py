nome = input('digite seu nome:')
salario = float(input("digite seu salario:").replace (",","."))
if salario >= 3000:
    desconto = (salario*0.11)
elif salario >= 2000:
    desconto = (salario*0.09)
elif salario <= 2000:
    desconto = (salario*0.08)


if salario >= 2000:
    trans = (salario*0.08)
else:
    trans = (salario*0.05)


if salario >= 3000:
    bonus = 300
else:
    bonus  = 200


if salario >= 3000:
    cargo = ("Acionista")
elif salario >= 2000:
    cargo = ("Gerente")
elif salario <= 2000:
    cargo = ("Vendedor")

salarioliq = salario - (desconto + trans) + bonus

print("================================================================================================")
print (f"{nome}, seu salario bruto informado foi de {salario:.2f} e seu salario liquido é de {salarioliq:.2f}".replace(".",","))
print("=================================================================================================")
print(f"os descontos aplicados foram de  {desconto:.2f} referente ao INSS, {trans:.2f} referente ao VT".replace(".",","))
print("=================================================================================================")
print(f"também recebeu um bonus de {bonus}, e seu cargo atual é de {cargo}".replace(".",","))
print("=================================================================================================")