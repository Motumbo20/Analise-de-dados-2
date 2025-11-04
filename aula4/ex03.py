print("escolha uma das seguintes opções de trabalho")
print("="*30)
print("="*10,"OPÇÕES","="*10)
print("1 - descobrir par ou impar")
print("2 - descobrir maior valor")
print("3 - descobrir o dobro")
print("="*30)
opc= int(input("escolha uma opção: "))
match opc:
    case 1:
        n1 = int(input("digite um numero:"))
        if n1 % 2 == 0:
            print(f"o numero {n1} é par")
        else:
            print(f"o numero {n1} é impar")
    case 2:
        n1= int(input("diga um numero, meu nobre: "))
        n2= int(input("diga outro numero, meu nobre: "))
        if n1 > n2:
            print(f"o {n1} é maior que o {n2}")
        elif n1 < n2:
            print(f"o {n2} é maior que o {n1}")
        elif n1 == n2:
                print(f"o {n1} é igual o {n2}")        
    case 3:
        n1 = int(input("digite um numero: "))
        dobro = n1 * 2
        print(f"o dobro de {n1} é {dobro}")
    case _:
        print("="*20)
        print("opção inválida!!!!")
        print("="*20)