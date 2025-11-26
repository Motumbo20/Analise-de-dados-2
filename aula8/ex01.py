def calcularInss(inss):
    if salariobruto >=1800:
        inss = salariobruto*0.11
    else:
        inss = salariobruto*0.09

    return inss
def calcularVale(vale):
    if salariobruto >=1500:
        vale = salariobruto*0.06
    else:
        vale = salariobruto*0.05

    return vale
def calcularBonus(bonus):
    if salariobruto >=1240:
        bonus = 700
    else:
        bonus = 500

    return bonus
def classificacao(cargo):
    if salariobruto >= 3000:
        cargo= "acionista"
    elif salariobruto >=2000:
        cargo = "Gerente"
    else:
        cargo = "vendedor"
    return cargo
def salarioliquidoo(salarioliquido):
    salarioliquido = salariobruto - (calcularInss(inss) + calcularVale(vale)) + calcularBonus(bonus)
    return salarioliquido
nome = input("digite seu nome:")
salariobruto = float(input("digite seu salario bruto: "))

inss = calcularInss(salariobruto)
vale = calcularVale(salariobruto)
bonus = calcularBonus(salariobruto)
cargo = classificacao(salariobruto)
salarioliquido = salarioliquidoo(salariobruto)

print(f"nome: {nome}")
print(f"cargo: {cargo}")
print(f"salario bruto: {salariobruto}")
print(f"inss: {inss}")
print(f"vale: {vale}")
print(f"bonus: {bonus}")
print(f"salario liquido: {salarioliquido}")