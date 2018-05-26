def matriz():
    vetor = []
    for i in range(0, 12):
        vetor.append([])
        for j in range(0, 12):
            vetor[i].append(float(input()))
    return vetor


soma = 0
operacao = str(input())
vetor = matriz()
contador = 0
for i in range(0, 12):
    for j in range(i+1, 12):
        soma += vetor[i][j]
        contador +=1
if operacao == 'S':
    print('%.1f' % soma)
else:
    print('%.1f' % (soma/contador))