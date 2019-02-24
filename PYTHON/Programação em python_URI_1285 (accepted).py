while True:
    try:
        n, m = map(str, input().split())
        number = 0
        for i in range(int(n), int(m) + 1):
            if len(str(i)) == len(set(str(i))):
                number += 1

        print(number)

    except EOFError:
        break
