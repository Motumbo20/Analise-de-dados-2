def imc(nome,altura,peso,idade):
    print("vou ver seu nome:")
    print("vou ver sua altura: ")
    print("vou ver seu peso: ")
    print("vou ver sua idade: ")
    imcc = peso / (altura*altura)
    if imcc < 18.5:
        sit = "parabéns, se ventar vc voa"
    elif imcc >=18.5 and imcc < 24.9:
        sit = "no peso ideal"
    elif imcc >= 25 and imcc < 29.99:
        sit = "gordin"
    else:
        sit = "obeso porra"
    print(f"o imc é {imcc} e vc ta {sit}")
imc("joe",1.8,800,22)