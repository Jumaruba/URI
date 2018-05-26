testes = int(input())
contador = 0
for i in range(0, testes):
    contador = 0
    pa, pb, ga, gb = input().split()
    while pa < pb:
        pa = int(pa) + round(int(pa) * float(ga) / 100)
        pb = int(pb) + round(int(pb) * float(gb) / 100)
        print(pa)
        print(pb)
        contador += 1
    print(contador)
