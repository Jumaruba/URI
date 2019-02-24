number = int(input())
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(number):
    letter = input()
    move = int(input())
    n_letter = ''
    for j in range(len(letter)):
        n_letter += alpha[alpha.index(letter[j]) - move]
    print(n_letter)
