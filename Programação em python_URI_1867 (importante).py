x, y = map(str, input().split())


def soma(x):
    while int(x) >= 10:
        x = sum([int(i) for i in x])
        x = str(x)
    return int(x)


while int(x) != 0 or int(y) != 0:
    x = soma(x)
    y = soma(y)

    if x > y:
        print(1)
    elif y > x:
        print(2)
    else:
        print(0)

    x, y = map(str, input().split())
