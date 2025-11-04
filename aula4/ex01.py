n1 = int(input("digite um numero:"))
match n1:
    case _ if n1 % 2 == 0:
        print(f"o numero {n1} é par")
    case _:    
        print(f"o numero {n1} é impar")