line = str(input())
line = sorted(list(line.lower()))
max_count = 0
count = 1
for i in range(1, len(line)):
    if line[i] == line[i-1]:
        count += 1
    else:
        if count > max_count:
            max_count = count
        count = 1
print(max_count)
