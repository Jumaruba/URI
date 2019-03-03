testes = int(input())

for i in range(testes):
    x = int(input())
    alturas = list(map(int, input().split()))
    alturas.sort()
    print(alturas)