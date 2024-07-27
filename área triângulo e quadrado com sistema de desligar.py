pergunta = 1
while pergunta != 3:
    pergunta = int(input("digite 1 para triângulo ou 2 para quadrado e 3 para desligar"))
    if pergunta == 1:
        b = int(input("digite a base do triângulo"))  # base
        a = int(input("digite a altura do triângulo"))  # altura
        areat = (b * a) / 2  # base vezes altura
        print(areat)
    elif pergunta == 2:
        la = int(input("quais os lados do quadrado"))
        areaq = la * 4
        print(f"a área do quadrado é {areaq}: ")
    elif pergunta == 3:
        print("acabou")
    else:
        print("número inválido")
