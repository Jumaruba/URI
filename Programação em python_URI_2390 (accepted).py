quantidade = int(input())
segundos = 0
segundo_agora = int(input())
for i in range(quantidade - 1):
    segundo_depois = int(input())
    tempo = segundo_depois - segundo_agora
    if tempo >= 10:
        segundos += 10
    else:
        segundos += tempo
    segundo_agora = segundo_depois

segundos += 10
print(segundos)
