num = int(input())
for i in range(num):
    word = str(input())
    if 'Кот' in word or 'кот' in word:
        availability = True
    if 'Пес' in word or 'пес' in word:
        availability = False
if availability == True:
    print('МЯУ')
