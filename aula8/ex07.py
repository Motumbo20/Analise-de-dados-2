valores = []
def maiordos(a,b,c):
    if a > b and a> c:
        maioral = a
    elif b > a and b> c:
        maioral = b
    else:
        maioral = c
    return maioral
for i in range (1,4):
    num = int(input("digite um numero: "))
    valores.append(num)

a = valores[0]
b = valores [1]
c = valores [2]
maior = maiordos(a,b,c)
print(f"o maior valor é {maior}")
