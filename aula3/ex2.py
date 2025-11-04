fruta = input("digite sua fruta: ")
match fruta:
    case "maça":
        print("é uma maça")
    case "banana":
        print("é uma banana")
    case _:
        print("escolha errada - é outra fruta")