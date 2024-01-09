num = int(input())
list_ = []
for i in range(num):
    list_.append(input())
for i in range(num):
    for j in range(i + 1, num):
        if list_[i] > list_[j]:
            list_[i], list_[j] = list_[j], list_[i]
for i in range(num):
    print(list_[i])
