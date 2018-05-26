r = 0
x = int(input())
l = []
for i in range(0, x):
    y = str(input())
    l.append(y)
if len(set(l)) != len(l):
       r = 1

print(r)
