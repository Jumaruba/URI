times = int(input())
count = 0
while times != 0:
    a = 0
    b = 0
    count += 1

    for i in range(times):
        x, y = map(int, input().split())
        a += x
        b += y
        
    print('Teste {}'.format(count))
    if a > b:
        print('Aldo')
    elif b > a:
        print('Beto')
    else:
        print(0)

    print('')
    times = int(input())

