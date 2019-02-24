cartas = list(map(int, input().split()))


def crescente():
    global cartas
    a = True
    for i in range(0, 4):
        if cartas[i] > cartas[i + 1]:
            a = False
            print(cartas [i])
            break


def decrescente():
    global cartas
    a = True
    for i in range(0, 4):
        if cartas[i] < cartas[i + 1]:
            a = False
            break


c = crescente()
d = decrescente()
if c == True and d == False:
    print('C')
elif c == False and d == True:
    print('D')
else:
    print('N')
