def fatorial(num):
    if num <= 2:
        return num
    else:
        return num * fatorial(num - 1)


x = input()
while x != '0':
    k = set(x)
    calculo = fatorial(len(x)) % 100000007
    for i in k:
        calculo /= fatorial(x.count(i)) % 100000007

    print(int(calculo))
    x = input()
