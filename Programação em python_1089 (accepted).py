x = int(input())

while x != 0:
    l = list(map(int, input().split()))
    index = l.index(min(l))
    p_1, p_2 = l[0:index], l[index:]
    l = p_2 + p_1
    l.append(l[0])
    signal_before = (l[1] - l[0]) // abs(l[1] - l[0])
    total = 1
    for i in range(1, len(l) - 1):
        signal = (l[i + 1] - l[i]) // abs(l[i + 1] - l[i])
        if signal != signal_before:
            total += 1
            signal_before = signal

    print(total)

    x = int(input())
