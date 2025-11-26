nome = input("digite seu nome:")
def calculo_idade():
    try:
        anos = int(input("digite sua idade: "))
    except ValueError:
        print("ta maluco rapá?")
    else:
        print(f"seu nome é {nome}, e sua idade é {anos}")
    finally:
        print("programa encerrado")
calculo_idade()