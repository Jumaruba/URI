
total = []
s = str(input())

while s != 'EOF':
    n = int(input())
    total.append(n)
    s = str(input())

k = sum(total) / 3
k = round(k, 3)
print(k)