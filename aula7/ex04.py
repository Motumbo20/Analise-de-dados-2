def soma(a,b):
    return a + b
def sub(a,b):
    return a - b
def mult(a,b):
    return a * b
def div(a,b):
    if a and b != 0:
        return a / b
    else:
        return "não divide por zero"

num1 = int(input("digite o 1° valor: "))
num2 = int(input("digite o 2° valor: "))
sum = soma(num1,num2)
subt = sub(num1,num2)
multi = mult(num1,num2)
divi = div(num1,num2)
print(f"soma {sum}, subtração {subt}, multiplicação {multi}, divisão {divi}")