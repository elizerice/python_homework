sum = int(input('Введите количество строк: '))
print('Введите строки')
list_ = []
for _ in range(sum):
    list_.append(input())
search = input('введите запрос')
for x in range(len(list_)):
    if search in list_[x]:
        print(list_[x])
