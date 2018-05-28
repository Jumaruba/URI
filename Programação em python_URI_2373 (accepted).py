quantidade = int(input())
broken = 0

for i in range(quantidade):
    l, c = map(int, input().split())
    if l > c:
        broken += c

print(broken)