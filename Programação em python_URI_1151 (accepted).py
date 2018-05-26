def fibonacci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input())

for i in range(1, n):
    print(fibonacci(i), end=' ')
print(fibonacci(n))
