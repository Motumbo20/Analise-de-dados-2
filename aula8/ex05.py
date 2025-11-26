def etariaclass(x):
    if x >= 60:
        etaria = "melhor idade"
    elif x >18:
        etaria = "adulto"
    elif x > 13:
        etaria = "adolescente"
    elif x < 13:
        etaria = "crianca"
    return etaria
anos = int(input("digite sua idade: "))
etariaa = etariaclass(anos)
print(f"na sua idade sua faixa etaria é {etariaa}")