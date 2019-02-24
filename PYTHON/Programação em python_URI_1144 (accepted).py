x = int(input())


def sequencia(x):
    for i in range(1, x + 1):
        print(i, end=' ')
        print(i ** 2, end=' ')
        print(i ** 3)
        print(i, end=' ')
        print((i ** 2) + 1, end=' ')
        print(i ** 3 + 1)

sequencia (x)