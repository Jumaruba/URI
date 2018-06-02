numero, total = map(int, input().split())

while numero != 0 and total != 0:
    repetidos = 0
    x = list(map(int, input().split()))
    for i in range(1, numero + 1):
        n = x.count(i)
        if n > 1:
            repetidos += 1
    print(repetidos)

    numero, total = map(int, input().split())
