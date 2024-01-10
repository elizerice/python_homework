line = str(input())
line = sorted(list(line.lower()))
max_symb = ''
max_count = 0
count = 1
for i in range(1, len(line)):
    if i == line[i-1]:
        count += 1
    else:
        if count > max_count and line[i-1] != ' ':
            max_count = count
            max_symb = line[i - 1]
        else:
            break
print(max_symb)
