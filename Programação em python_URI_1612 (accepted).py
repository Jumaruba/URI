testes = int(input())

for i in range(0, testes):
    x = int(input())
    if x % 2 == 0:
        print(x // 2)
    else:
        x += 1
        print(x // 2)
