primeiro, segundo = map(int, input().split())

if 97 <= segundo <= 100:
    print('cheia')
elif 0 <= segundo <= 2:
    print('nova')
if 3 <= segundo <= 96:
    if primeiro < segundo:
        print('crescente')
    else:
        print('minguante')
