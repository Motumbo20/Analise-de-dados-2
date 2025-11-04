num1 = int(input("digite um numero: "))
num2 = int(input("digite outro numero: "))
sinal = input("agora digite um dos sinais matematicos ( + , - , * ou / ): ")
match sinal:
    case "+":
        print(f"{num1} + {num2} é igual a {num1+num2}")
    case "-":
        print(f"{num1} - {num2} é igual a {num1-num2}")
    case "*":
        print(f"{num1} * {num2} é igual a {num1*num2}")
    case "/":
        print(f"{num1} / {num2} é igual a {num1/num2}")