def dividir(a,b):
    if a and b != 0:
        return a/b
    else:
        return "não divide por 0"

num= int(input("digite um numerador:"))
den= int(input("digite um denominador:"))

final = dividir(num,den)

print(f"a divisão final desses dois numeros foi {final:.1f}")

        