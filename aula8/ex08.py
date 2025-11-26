def conceitonota(x):
    if x >= 9:
        conceito = "A"
    elif x >= 7:
        conceito = "B"
    elif x >= 5:
        conceito = "C"
    else:
        conceito = "D"
    return conceito
nota = int(input("digite sua nota: "))
final = conceitonota(nota)
print(f"sua nota foi {nota} e seu conceito final foi {final}") 