sum = int(input('Введите количество строк: '))
print('Введите строки')
list = []
for _ in range(sum):
    list.append(input())
search = input('введите запрос')
for x in range(len(list)):
    if search in list[x]:
        print(list[x])
