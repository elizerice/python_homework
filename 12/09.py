symb = str(input())
line = str(input())
line = (line.lower()).split()
list_with_symb = list()
for i in line:
    if symb in i:
        list_with_symb.append(i)
for i in list_with_symb:
    print(i)
