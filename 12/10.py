line = str(input())
line = line.split()
sum_symb = 0
for i in line:
    sum_symb += len(i)
print(sum_symb)
