list_1 = set()
list_2 = set()
num = input()
while num != '':
    list_1.add(str(num))
    num = input()
num = input()
while num != '':
    list_2.add(str(num))
    num = input()
if len(list_1 & list_2) != 0:
    print(list_1 & list_2)
else:
    print('EMPTY')
