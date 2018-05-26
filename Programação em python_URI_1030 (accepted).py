cases = int(input())

for i in range(0, cases):
    quant, passo = map(int, input().split())
    pessoas = []
    for j in range(1, quant + 1):
        pessoas.append(j)

    index = passo - 1
    if index > len(pessoas):
        index = (passo % len(pessoas)) - 1

    while len(pessoas) != 1:
        pessoas.pop(index)
        if index < 0:
            index += 1
        index += (passo - 1)

        if index > len(pessoas):
            index = index % len(pessoas)
        if index == len(pessoas):
            index = 0

    print('Case %i: %i' % (i + 1, pessoas[0]))