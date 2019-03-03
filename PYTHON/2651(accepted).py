string_vet = []
x = input()
want = False
for z in ['z', 'Z']:
    for e in ['e', 'E']:
        for l in ['l', 'L']:
            for d in ['d', 'D']:
                for a in ['a', 'A']:
                    string = z + e + l + d + a
                    if string in x:
                        want = True


if want:
    print('Link Bolado')
else:
    print('Link Tranquilo')