sum = int(input('Введите количество товаров: '))
print('Введите покупки')
list_ = []
for _ in range(sum):
    list_.append(input())
for x in range(len(list)):
    print(list_[x])
