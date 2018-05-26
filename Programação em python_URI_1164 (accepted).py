n = int(input())


def soma_divisores():
    global x
    soma = 1
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            soma += i
    return soma


for i in range(n):
    x = int(input())
    soma = soma_divisores()
    if soma == x:
        print(x, 'eh perfeito')
    else:
        print(x, 'nao eh perfeito')
