resposta = "s"
while resposta == "s" or "S":
    n = int(input("digite um numero: "))
    if n <0:
        print(f"{n} é um número negativo")
    elif n >0:
        print(f"{n} é um número positivo")
    else:
        print(f"{n} é um número neutro")
    resposta = input("deseja continuar?")

