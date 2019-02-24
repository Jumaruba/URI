def mdc(num1, num2):
    if num1 % num2 == 0:
        return num2
    else:
        return mdc(num2, num1 % num2)


times = int(input())

for i in range(times):
    a, b = map(int, input().split())
    if b > a:
        c = a
        a = b
        b = c
    print(mdc(a, b))
