m = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
auxiliar = []
k = 8


def aux():
    x, y = map(int, input().split())
    if x > y:
        auxiliar.append(m[2 * i])
    else:
        auxiliar.append(m[2 * i + 1])
    return auxiliar


while k >= 1:
    for i in range(k):
        auxiliar = aux()

    m = auxiliar[:]
    auxiliar = []

    k = k // 2

print(m[0].upper())
