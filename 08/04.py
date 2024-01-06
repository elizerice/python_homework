num = int(input())
symbols = 'ABCDEFGHI'
for i in range(num, 0, -1):
    for j in symbols[0:num]:
        print(j, i, sep ='', end =' ')
        if j == symbols[num - 1]:
            print('')
