def buscar_nomes():
    alunos= {
        "Ana":8.5,
        "Bruno":7.0,
        "Carlos":9.2
    }
    try:
        nome = input("digite nome: ").capitalize()
        nota= alunos[nome]
    except KeyError:
        print("nome não encontrado")
    else:
        print("o nome encontrado foi: ",nome)
        print("a nota é", nota)
    finally:
        print("FIM")
buscar_nomes()
