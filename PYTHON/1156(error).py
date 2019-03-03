contador =0
for i in range (1, 40, 2):
    contador+=1

soma=0
for j in range(0,contador):
    k = (2**j+1)/2**j
    soma+=j

print('%.2f' %soma)