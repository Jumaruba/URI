x, y = map(str, input().split())

while x != 0 and y != 0:
    y = list(y)
    if x in y:
        z = y.count(x)
        for i in range(z):
            y.remove(x)
    y = ''.join(y)
    if y == '':
        print(0)
    else:
        print(int(y))
    x, y = map(str, input().split())
