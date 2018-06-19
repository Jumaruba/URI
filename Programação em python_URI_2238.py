divisor, n_divisor, multiplo, n_multiplo = list(map(int, input().split()))

b = False
if multiplo % divisor == 0:
    for x in range(divisor, multiplo // 2 + 1, divisor):
        if x % n_divisor != 0 and n_multiplo % x != 0 and multiplo % x == 0:
            print(x)
            b = True
            break

if not b:
    print(-1)
