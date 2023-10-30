num = int(input())
line = []
words = []
line = input()
line = line.split('; ')
for i in range(len(line)):
    if (len(line[i]) % num == 0):
        words.append(line[i])
print(' -  '.join(words))
