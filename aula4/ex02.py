n1= int(input("diga um numero, meu nobre: "))
n2= int(input("diga outro numero, meu nobre: "))
match n1:
    case _ if n1 > n2:
        print(f"o {n1} é maior que o {n2}")
    case _ if n1 < n2:
        print(f"o {n2} é maior que o {n1}")
    case _ if n1 == n2:
        print(f"o {n1} é igual o {n2}")