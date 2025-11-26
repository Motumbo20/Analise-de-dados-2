def calcular_media():
    try:
        n1 = float(input("1° nota: "))
        n2 = float(input("2° nota: "))
        media = (n1+n2)/2
    except ValueError:
        print("digite numeros validos")
    else:
        print(f"media: {media}")
    finally:
        print("fim do programa")
calcular_media()
