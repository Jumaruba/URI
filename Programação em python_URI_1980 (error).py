def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)


produto = 1
palavra = list(input())
while palavra != ['0']:
    if len(set(palavra)) == len(palavra):
        resposta = fatorial(len(palavra))
    else:
        for i in set(palavra):
            frequencia = palavra.count(i)
            produto *= fatorial(frequencia)
        resposta = fatorial(len(palavra)) // produto
    print(resposta)
    palavra = list(input())
