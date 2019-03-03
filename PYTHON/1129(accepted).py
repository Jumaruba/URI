x = int(input())
dict = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E'}


def contando(lista):
    contador = 0
    for j in range(5):
        if lista[j] <= 127:
            contador += 1
            pos = j
    if contador == 1:
        print(dict[pos])
    else:
        print('*')


while x != 0:
    for i in range(x):
        l = list(map(int, input().split()))
        contando(l)
    x = int(input())