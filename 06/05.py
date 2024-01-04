lang_1 = int(input())
lang_2 = int(input())
lang_3 = int(input())
people = set()
two_lang = set()
for i in range(lang_1 + lang_2 + lang_3):
    sec_name = str(input())
    if sec_name not in people:
        people.add(sec_name)
    else:
        if sec_name not in two_lang:
            two_lang.add(sec_name)
        else:
            two_lang.remove(sec_name)
if len(two_lang) == 0:
    print('NO')
else:
    print(*two_lang)
