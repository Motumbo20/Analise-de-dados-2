print("calculo de imc")
print("siga com suas informações:")
print("="*30)
def alt():
    try:
        altura = float(input("digite sua altura:"))
        return altura
    except ValueError:
        print("digite um numero valido")
    except ZeroDivisionError:
        print("zero não vale")

def pes():
    try:
        peso = float(input("digite seu peso:"))
        return peso
    except ValueError:
        print("digite um numero valido")

altura = alt()
peso = pes()
imc = (peso/(altura*altura))

print(f"peso {peso}. altura {altura} e seu imc é {imc}")