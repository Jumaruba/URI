testes = int(input())

for i in range(testes):
    actions = int(input())
    shots = list(map(int, input().split()))
    command = input()
    total = 0
    for m in range(actions):
        if (shots[m] == 1 or shots[m] == 2) and command[m] == 'S':
            total += 1
        elif (shots[m] > 2) and command[m] == 'J':
            total += 1
    print(total)
