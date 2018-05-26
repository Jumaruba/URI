maior = int(input())
menor = int(input())
soma=0

for i in range(menor+1, maior):
    if i%2==1:
        soma+=i
print(soma)