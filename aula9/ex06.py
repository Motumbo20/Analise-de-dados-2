def conta():

    print("1-adição")
    print("2-subtração")
    print("3-divisão")
    opc = int(input("escolha:"))
    con = "sim"
    match opc:
            case 1:
                try:
                    n1 = int(input("digite um numero: "))
                    n2 = int(input("digite outro numero: "))
                    resultado = n1+n2
                except ValueError:
                    print("valores invalidos para a operacao")
                else:
                    print(f"o resultado da sua operação é {resultado}")
                finally:
                    print("acabou sua operação")
            case 2:
                try:
                    n1 = int(input("digite um numero: "))
                    n2 = int(input("digite outro numero: "))
                    resultado = n1-n2
                except ValueError:
                    print("valores invalidos para a operacao")
                else:
                    print(f"o resultado da sua operação é {resultado}")
                finally:
                    print("acabou sua operação")
            case 3:
                try:
                    n1 = int(input("digite um numero: "))
                    n2 = int(input("digite outro numero: "))
                    resultado = n1/n2
                except ValueError:
                    print("valores invalidos para a operacao")
                except ZeroDivisionError:
                    print("não pode ter zero para divisao")
                else:
                    print(f"o resultado da sua operação é {resultado}")
                finally:
                    print("acabou sua operação")
conta()
    