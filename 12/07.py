line = input().split(' ')
num_list = list()
for symb in line:
    if symb.isdigit():
        num_list.append(int(symb))
        continue
    if symb == '+':
        result = int(num_list[-2]) + int(num_list[-1])
    if symb == '-':
        result = int(num_list[-2]) - int(num_list[-1])
    if symb == '*':
        result = int(num_list[-2]) * int(num_list[-1])
    num_list.pop()
    num_list.pop()
    num_list.append(result)
print(*num_list)
