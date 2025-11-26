def intt(inteiro):
    try:
        resul = int(float(inteiro))
    except ValueError:
        print("errouuuu")
    else:
        print(f"seu numero inteiro é ",resul)
    finally:
        print("operacao finalizada")

num1 = input("digite um numero:")
intt (num1)
