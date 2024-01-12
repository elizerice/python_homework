words_dict = dict()
for _ in range(int(input())):
    phrase = str(input())
    word = phrase.split()[0]
    description = ' '.join(phrase.split()[1:])
    words_dict[word] = description
for _ in range(int(input())):
    mom_check = str(input())
    if mom_check in words_dict:
        print(words_dict[mom_check])
    else:
        print('Нет в словаре')
