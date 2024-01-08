sum = int(input('Введите количество строк: '))
print('Введите строки')
list_ = []
for _ in range(sum):
    list_.append(input())
num = int(input('введите номер буквы: '))
for i in range(len(list_)):
   print(list_[i][num-1], end="")
