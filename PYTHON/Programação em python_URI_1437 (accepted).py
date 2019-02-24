x = int(input())
while x != 0:
    t = 0
    for i in str(input()):
        if i == 'D':
            t += 1
        else:
            t -= 1
    if t % 4 == 0:
        print('N')
    elif t % 4 == 1:
        print('L')
    elif t % 4 == 2:
        print('S')
    else:
        print('O')

    x = int(input())