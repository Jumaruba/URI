notas = {'W': 1, 'H': 1 / 2, 'Q': 1 / 4, 'E': 1 / 8, 'S': 1 / 16, 'T': 1 / 32, 'X': 1 / 64}

composicao = input()


def compaco(composicao_pos):
    global notas
    soma = 0
    for i in composicao_pos:
        soma += notas[i]
    if soma != 1:
        return False
    else:
        return True


while composicao != '*':
    composicao = list((composicao.strip('/')).split('/'))
    quantidade = 0
    for i in range(len(composicao)):
        boleana = compaco(composicao[i])
        if boleana:
            quantidade += 1

    print(quantidade)

    composicao = input()
