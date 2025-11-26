def ler_inteiro():
    try:
        numero = int(float(input("digite um numero: ")))
    except ValueError:
        print("digitar somente numero inteiro")
    else:
        print(f"numero digitado pelo usuario {numero}")
    finally:
        print("fim do programa")

ler_inteiro()