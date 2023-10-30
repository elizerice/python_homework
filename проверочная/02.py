line_1 = input().split(' ')
line_2 = input().split(' ')
line_3 = input().split(' ')
uniques = set()
uniq = list()
sum = 0
for i in line_1:
    if i not in line_2 and i not in line_3:
        uniques.add(i)
for i in line_2:
    if i not in line_1 and i not in line_3:
        uniques.add(i)
for i in line_3:
    if i not in line_2 and i not in line_1:
        uniques.add(i)
for i in uniques:
    uniq.append(i)
    sum += len(i)
print('#'.join(uniq))
print(sum)
