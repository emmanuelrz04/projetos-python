inicio = int(input("quantas horas começou a partida de xadrez?"))
fim = int(input("quantas horas acabou a partida de xadrez?"))
resultado = fim - inicio
if resultado > 24:
    print("erro")
elif resultado <0:
    print(inicio - fim)
else:
    print(resultado)