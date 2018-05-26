def kadane(vetor):
    max_ate_agora = 0
    max_temp = 0
    inicio_temp = 0
    inicio = 0
    fim = 0
    for i in range(0, len(vetor)):
        max_temp += vetor[i]
        if max_temp > max_ate_agora:
            max_ate_agora = max_temp
            inicio = inicio_temp
            fim = i
        elif max_temp < 0:
            max_temp = 0
            inicio_temp = i + 1
        elif max_temp == max_ate_agora and fim - inicio < i - inicio_temp:
            inicio = inicio_temp
            fim = i
    return inicio, fim


quantidade = int(input())
teste = 1
while quantidade != 0:
    vetor = []
    boleana = False
    for i in range(quantidade):
        x, y = map(int, input().split())
        soma = x - y
        if x != 0 and x > y:
            boleana = True
        vetor.append(soma)
    if boleana:
        inicio, fim = kadane(vetor)
        print('Teste', teste)
        print(inicio + 1, fim + 1)
        print('')
    else:
        print('Teste', teste)
        print('nenhum')
        print('')
    quantidade = int(input())
    teste += 1
