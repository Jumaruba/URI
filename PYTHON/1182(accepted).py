def matriz():
    vetor = []
    for i in range(0, 12):
        vetor.append([])
        for j in range(0, 12):
            vetor[i].append(float(input()))
    return vetor


coluna = int(input())
soma = 0
operacao = str(input())
vetor = matriz()

for i in range(0, 12):
    soma += vetor[i][coluna]

if operacao == 'S':
    print('%.1f' % soma)
else:
    print('%.1f' % (soma/12))