# Código ERRADO!

total = float(input("quantos foram os eleitores de Recife?"))
validos = float(input("quantos foram os validos"))
nulos = float(input("quantos foram os votos nulos"))
branco = float(input("quantos foram os eleitores em branco"))

pvalidos = (validos/total)*100
pnulos = (nulos/total)*100
pbrancos = (branco/total)*100

print (f"{pvalidos}% {pnulos}% {pbrancos}%")

# Código CORRETO!

validos = 0
branco = 0
nulo = 0
eleitores = int(input("digite a quantidade de eleitores: "))
for x in range(eleitores):
    voto = int(input("em quem você quer votar?\n[1] para carlos\n[2] para marcelo\n[3] para maicon\n[4] para nulo\nVOTE AQUI: "))
    if voto == 1:
        validos += 1
    elif voto == 2:
        validos += 1
    elif voto == 3:
        validos += 1
    elif voto == 4:
        nulo += 1
    else:
        branco += 1
pvalidos = (validos/eleitores)*100
pnulos = (nulo/eleitores)*100
pbranco = (branco/eleitores)*100
print(f"{pvalidos}% dos votos válidos\n {pnulos}% dos votos nulos\n {pbranco}% dos votos brancos")


