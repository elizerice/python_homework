_list = []
yes_no = bool()
for i in range(int(input())):
    number = input()
    _list.append(number)
num = int(input())
for i in _list:
    for j in _list:
        if int(i) * int(j) == num:
            yes_no = True
if yes_no == True:
    print('да')
else:
    print('нет')
