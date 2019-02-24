estacoes = int(input())
sequencia = []
escolhido = []


def ordem():  # colocando estacoes nas posicoes
    global sequencia, estacoes
    for i in range(1, estacoes + 1):
        sequencia.append(i)
    return sequencia


def ultimo():
    global sequencia, escolhido, passo
    contador = 0
    passo = passo+1
    index = passo - 1
    if passo > len(sequencia):
        index = (passo % len(sequencia) - 1)
    while 13 in sequencia:
        sequencia.pop(index)
        if index<=0:
            index+=1
        index+=(passo-1)
        if index >= len(pessoas):
            index= index%len(pessoas)
        contador+=1
    escolhido.append(contador)
    return escolhido, passo

passo =2

def main ():
    ordem()
    for j in range(0,16):
        ultimo()
        passo+=1
    print(escolhido.index(min(escolhido)))

main()
