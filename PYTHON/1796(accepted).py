x = int(input())
people = input()

n_n = people.count('1')

if n_n >= x-n_n:
    print('N')
else:
    print('Y')