soma = 0
for x in range(2):
    nota = float(input(f"digite a nota {x+1}: "))
    soma = soma + nota
media = soma/2
if media < 4:
    print("reprovado")
elif media > 4 and media < 7:
    print("recuperação")
elif media >= 7:
    print("aprovado")
print(media)

