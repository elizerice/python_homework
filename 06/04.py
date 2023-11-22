lang_1 = int(input())
lang_2 = int(input())
lang_list = set()
count = int() 

for i in range(lang_1 + lang_2):
    student = str(input())
    if student in lang_list:
        lang_list.remove(student)
    else:
        lang_list.add(student)
        count += 1
if (lang_1 + lang_2) // 2 ==  count:
    print('NO')
else:
    print(len(lang_list))
