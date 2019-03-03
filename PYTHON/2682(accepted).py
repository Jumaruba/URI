numero = 0
erro = False
while True:
    try:
        x = int(input())
        if x > numero and erro == False:
            numero = x
        elif x < numero:
            erro = True
    except EOFError:
        break

print(numero + 1)
