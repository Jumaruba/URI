n = int(input())


def soma_impares(x, y):
    soma = 0
    ultimo = (y * 2) + x
    if x % 2 == 0:
        primeiro = x + 1
    elif x % 2 == 1:
        primeiro = x
    for i in range(primeiro, ultimo, 2):
        soma += i
    print(soma)


for i in range(n):
    x, y = map(int, input().split())
    soma_impares(x, y)
