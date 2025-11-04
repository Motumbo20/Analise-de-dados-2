diasemana = int(input("digite um numero e 1 a 7: "))
match diasemana:
    case 1:
        print(f"Domingo é correspondente ao numero {diasemana}")
    case 2:
        print(f"Segunda é correspondente ao numero {diasemana}")
    case 3:
        print(f"Terça é correspondente ao numero {diasemana}")
    case 4:
        print(f"Quarta é correspondente ao numero {diasemana}")
    case 5:
        print(f"Quinta é correspondente ao numero {diasemana}")
    case 6:
        print(f"Sexta é correspondente ao numero {diasemana}")
    case 7:
        print(f"Sábado é correspondente ao numero {diasemana}")
    case _:
        print("ta errado")
