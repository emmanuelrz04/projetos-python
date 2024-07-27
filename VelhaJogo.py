# Espaços em branco a serem preenchidos com X ou O
pos1_in_1 = ' '
pos1_in_2 = ' '
pos1_in_3 = ' '
pos2_in_1 = ' '
pos2_in_2 = ' '
pos2_in_3 = ' '
pos3_in_1 = ' '
pos3_in_2 = ' '
pos3_in_3 = ' '
jogador_atual = 'X'

# Função para printar o tabuleiro, e as marcações para o X e O
def imprimir_tabuleiro():
    print(f"{pos1_in_1} | {pos1_in_2} | {pos1_in_3}")
    print("--+---+--")
    print(f"{pos2_in_1} | {pos2_in_2} | {pos2_in_3}")
    print("--+---+--")
    print(f"{pos3_in_1} | {pos3_in_2} | {pos3_in_3}")


def verificar_vitoria(jogador):
    # Verifica todas as vitórias possíveis de X ou O
    return ((pos1_in_1 == pos1_in_2 == pos1_in_3 == jogador) or
            (pos2_in_1 == pos2_in_2 == pos2_in_3 == jogador) or
            (pos3_in_1 == pos3_in_2 == pos3_in_3 == jogador) or
            (pos1_in_1 == pos2_in_1 == pos3_in_1 == jogador) or
            (pos1_in_2 == pos2_in_2 == pos3_in_2 == jogador) or
            (pos1_in_3 == pos2_in_3 == pos3_in_3 == jogador) or
            (pos1_in_1 == pos2_in_2 == pos3_in_3 == jogador) or
            (pos1_in_3 == pos2_in_2 == pos3_in_1 == jogador))

#É um while constante que só termina com um break, ele serve para ser preenchido todos os espaços com X ou O
while True:
    imprimir_tabuleiro()
    posicao = int(input(f"Jogador {jogador_atual}, digite a posição (ex: 11 para linha 1, coluna 1): "))

#Faz os comandos para colocar X ou O nos espaços em branco

    if posicao == 11 and pos1_in_1 == ' ':
        pos1_in_1 = jogador_atual #X OU O
    elif posicao == 12 and pos1_in_2 == ' ':
        pos1_in_2 = jogador_atual #X OU O
    elif posicao == 13 and pos1_in_3 == ' ':
        pos1_in_3 = jogador_atual #X OU O
    elif posicao == 21 and pos2_in_1 == ' ':
        pos2_in_1 = jogador_atual #X OU O
    elif posicao == 22 and pos2_in_2 == ' ':
        pos2_in_2 = jogador_atual #X OU O
    elif posicao == 23 and pos2_in_3 == ' ':
        pos2_in_3 = jogador_atual #X OU O
    elif posicao == 31 and pos3_in_1 == ' ':
        pos3_in_1 = jogador_atual #X OU O
    elif posicao == 32 and pos3_in_2 == ' ':
        pos3_in_2 = jogador_atual #X OU O
    elif posicao == 33 and pos3_in_3 == ' ':
        pos3_in_3 = jogador_atual #X OU O
    else:
        print("Esta posição já está preenchida ou é inválida. Tente novamente.")

#Ele pega o verificar vitória se ele é true ou false, e compara com o jogador atual no momento (X ou O)
    if verificar_vitoria(jogador_atual):
        imprimir_tabuleiro()
        print(f"Jogador {jogador_atual} venceu o jogo!")
        break

#Verifica todas as colunas! Se todas elas não estiverem vazias, significa que deu VELHA!
    if (pos1_in_1 != ' ' and pos1_in_2 != ' ' and pos1_in_3 != ' ' and
            pos2_in_1 != ' ' and pos2_in_2 != ' ' and pos2_in_3 != ' ' and
            pos3_in_1 != ' ' and pos3_in_2 != ' ' and pos3_in_3 != ' '):
        imprimir_tabuleiro()
        print("Velha")

#Faz a alternância do jogador X para o O
    if jogador_atual == "X":
        jogador_atual = "O"
    else:
        jogador_atual = "X"
