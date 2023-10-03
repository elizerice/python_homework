sum = int(input('Введите количество товаров: '))
print('Введите покупки')
list = []
for _ in range(sum):
    list.append(input())
for x in range(len(list)):
    print(list[x])
