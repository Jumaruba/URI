def leds(k):
    global i, soma
    if k[i] == '0':
        soma += 6
    elif k[i] == '1':
        soma += 2
    elif k[i] == '2':
        soma += 5
    elif k[i] == '3':
        soma += 5
    elif k[i] == '7':
        soma += 3
    elif k[i] == '8':
        soma += 7
    elif k[i] == '9':
        soma += 6
    elif k[i] == '4':
        soma += 4
    elif k[i] == '5':
        soma += 5
    elif k[i] == '6':
        soma += 6
    return soma


x = int(input())

for i in range(0, x):
    k = str(input())
    soma = 0
    for i in range(0, len(k)):
        soma = leds(k)

    print('%i leds' % soma)
