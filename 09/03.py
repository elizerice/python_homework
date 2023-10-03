sum = int(input('Введите количество строк: '))
print('Введите строки')
list = []
for _ in range(sum):
    list.append(input())
num = int(input('введите номер буквы: '))
for i in range(len(list)):
   print(list[i][num-1], end="") 
