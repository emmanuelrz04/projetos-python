pergunta = "sim"
while pergunta == "sim" or pergunta == "s":
    n = int(input("digite um número"))
    if n % 2 ==0:
        print("é par")
    else:
        print("é impar")
    pergunta = input("quer voltar?")

