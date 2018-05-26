estacoes = int(input())
sequencia = []
escolhido = []

for i in range(1, estacoes + 1):
    sequencia.append(i)

original = sequencia
passo = 1

for j in range(1, estacoes - 1):
    contador = 0
    passo = passo + 1
    index = passo - 1
    sequencia = original
    if passo > len(sequencia):
        index = (passo % len(sequencia) - 1)
    while 13 in sequencia:
        sequencia.pop(index)
        if index <= 0:
            index += 1
        index += (passo - 1)
        if index >= len(sequencia):
            index = index % len(sequencia)
        contador += 1
    escolhido.append(contador)

print(escolhido.index(min(escolhido))+2)
print(escolhido)