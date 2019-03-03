x = int(input())

if x % 2 == 0:
    print('S')
else:
    b = False
    i = 1
    while i * i <= x:
        i += 2
        if x % i == 0:
            print('S')
            b = True
            break
    if not b:
        print('N')
