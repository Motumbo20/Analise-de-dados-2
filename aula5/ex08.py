n2 = "sim"
while n2 == "sim":
    n1 = int (input("digite um numero: "))
    if n1 % 2 == 0:
        print("seu numero é par")
    else:
        print("seu numero é impar")
    n2 = input("quer continuar? sim ou não?").lower()
    if n2 != "sim":
        print("encerrado o programa.")
        break