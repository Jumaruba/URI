def kadane(lista, tamanho):
    max_real = 0
    soma = 0
    max_ate_agora = 0
    for i in range(tamanho):
        soma += lista[i]
        if soma > max_ate_agora:
            max_ate_agora = soma
        if soma < 0:
            if max_ate_agora > max_real:
                max_real = max_ate_agora
            soma = 0
            max_ate_agora = 0
    if max_ate_agora > max_real:
        max_real = max_ate_agora
    return max_real


tamanho = int(input())
lista = list(map(int, input().split()))

maior = kadane(lista, tamanho)

print(maior)
