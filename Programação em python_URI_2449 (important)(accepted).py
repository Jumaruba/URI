def soma_dois(numero1, numero2, ideal):
    aumenta = ideal - numero1
    numero1 += aumenta
    numero2 += aumenta
    return numero1, numero2, abs(aumenta)


numeros, ideal = map(int, input().split())

x = list(map(int, input().split()))
aumenta_total = 0
for i in range(numeros - 1):
    if x[i] != ideal:
        x[i], x[i + 1], aumenta_agora = soma_dois(x[i], x[i + 1], ideal)
        aumenta_total += aumenta_agora

print(aumenta_total)
