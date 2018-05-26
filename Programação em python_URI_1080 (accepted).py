maior = 0
n=[]
p=0
for i in range (0,100):
    x = int(input())
    n.append(x)


print(max(n))
print(n.index(max(n))+1)
