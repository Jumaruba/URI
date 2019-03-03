alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
conversao = str(input())
palavra = str(input())
frase = []
for i in range(len(palavra)):
      index = conversao.index(palavra[i])
      frase.append(alfabeto[index])

for j in range(len(frase)-1):
    print(frase[j], end='')

print(frase[len(frase)-1])
