num = int(input())
list = []
for i in range(num):
    list.append(input())
for i in range(num):
    for j in range(i + 1, num):
        if list[i] > list[j]:
            list[i], list[j] = list[j], list[i]
for i in range(num):
    print(list[i])
