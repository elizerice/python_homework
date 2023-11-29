line = input()
line = line.split(' ')
_list = []
count = 0
print(line)
for i in range(len(line)):
    count += 1
    if count % 3 == 0:
        _list.append(line[i])
print(*_list)
