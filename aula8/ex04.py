def parimpar(x):
    if num1 % 2 == 0:
        tipo = "par"
    else:
        tipo = "impar"
    return tipo
num1 = int(input("digite um numero: "))
tipoo = parimpar(num1)
print(f"o {num1} é {tipoo}")