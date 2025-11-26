def dividir(a,b):
    try:
        resultado = a/b
    except ZeroDivisionError:
        print("Erro: dividido por zero")
    else:
        print(f"resultado {resultado}")
    finally:
        print("operacao foi finalizada")

print("prgrama principal")
num1 = float(input("digite um numerador: "))
num2 = float(input("digite um denominador: "))
dividir(num1,num2)
