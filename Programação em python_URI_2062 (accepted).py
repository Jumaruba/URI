n = int(input())
p = input().split()
l = []
for j in p:
    if len(j) == 3 and j[0] == 'U' and j[1] == 'R':
        l.append('URI')
    elif len(j) == 3 and j[0] == 'O' and j[1] == "B":
        l.append('OBI')
    else:
        l.append(j)

for k in range(n - 1):
    print(l[k], end=' ')

print(l[n-1])
