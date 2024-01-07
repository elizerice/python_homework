cat_num = int()
for i in range(int(input())):
    phrase = str(input())
    if 'кот' in phrase or 'Кот' in phrase:
        for j in range(len(phrase)):
            if phrase[j] == 'к' or phrase[j] == 'К':
                cat_num = j + 1
        print(i + 1, cat_num)
