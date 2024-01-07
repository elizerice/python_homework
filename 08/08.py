line = str(input())
count = 0
max_count = 0
for i in range(len(line)):
    if 'о' in line:
        count += 1
        if 'р' in line[i]:
            count = 0
    if count > max_count:
        max_count = count
print(max_count)
