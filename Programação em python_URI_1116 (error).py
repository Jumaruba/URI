n = int(input())


def divisao(x, y):
    if abs(x) >= abs(y) and y != 0 and x != 0:
        k = x // y
        if x % y != 0:
            k = x / y
            k = '%.1f' % k
        print(k)
    elif x == 0:
        print(0.0)
    else:
        print('divisao impossivel')


for i in range(0, n):
    x, y = map(float, input().split())
    divisao(x, y)
