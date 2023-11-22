lang_1 = int(input())
lang_2 = int(input())
lang_1_list = set()
lang_2_list = set()
for i in range(lang_1):
    student = str(input())
    lang_1_list.add(student)
for i in range(lang_2):
    student = str(input())
    lang_2_list.add(student)
if not lang_1_list ^ lang_2_list:
    print('no')
else:
    print(len(lang_1_list ^ lang_2_list))
