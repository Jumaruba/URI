x = list(map(int,input().split()))

'''print(max(x))'''

maior = 0
for i in range(len(x)):
    if x[i]>maior:
        maior= x[i]

print(maior)