stud_list = []
for i in range(int(input())):
    class_list = [input().split()[-1] for j in range(int(input()))]
    stud_list.append(class_list)

if all(any(x == '5' for x in i) for i in stud_list):
    print('ДА')
else:
    print('НЕТ')
print(stud_list)
