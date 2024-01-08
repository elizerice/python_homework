cat_num = int()
cat_list = list()
for i in range(int(input())):
    phrase = str(input())
    if 'кот' in phrase or 'Кот' in phrase:
        for j in range(len(phrase)):
            if phrase[j] == 'к' or phrase[j] == 'К':
                cat_num = j + 1
        cat_list.append((i + 1, cat_num))
for i in cat_list:
    print(*i)
