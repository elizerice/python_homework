words = dict()
line = str(input()).split()
word_repeat = list()
for i in range(len(line)):
    if line[i] not in words:
        words[line[i]] = 1
    else:
        words[line[i]] += 1
    word_repeat.append(words[line[i]])
print(*word_repeat)
