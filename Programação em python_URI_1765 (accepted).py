t = int(input())
while t != 0:
    for i in range(0, t):
        quantidade, b1, b2 = map(float, input().split())
        print('Size #%i:' % (i + 1))
        area = ((b1 + b2) * 5 / 2)*quantidade
        print('Ice Cream Used: %.2f cm2' % area)
    print('')
    t = int(input())
