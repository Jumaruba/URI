s = str(input())
total = 0
n = 0
while True:
    try:
        n = int(input())
        total += n
        s = str(input())
        n += 1
    except EOFError:
        print(round(total / n, 3))
        break
