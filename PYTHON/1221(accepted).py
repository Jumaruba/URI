def prime(n):
    if n == 2:
        return "Prime"
    elif n % 2 == 0 or n < 2:
        return "Not Prime"
    start = 3
    m = n ** (1 / 2)
    while start <= m:
        if n % start == 0:
            return "Not Prime"
        start += 2

    return "Prime"


x = int(input())

for j in range(x):
    print(prime(int(input())))
