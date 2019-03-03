'''tamanho = int(input())

vetor = list(map(int, input().split()))

menor = min(vetor)
print('Menor valor:', menor )
index = vetor.index(menor)
print('Posicao:', index)'''  # usando artifícios de python

# caso nao tivessemos o artificio de min

tamanho = int(input())
vetor = list(map(int, input().split()))


def menor(vetor):
    valor = vetor[0]
    index = 0
    for i in range(1, len(vetor)):
        if vetor[i] < valor:
            valor = vetor[i]
            index = i
    return valor, index

valor,index = menor(vetor)
print('Menor valor:', valor )
print('Posicao:', index)