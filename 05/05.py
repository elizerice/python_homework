num = 0
cat = 0
word = str()
while word != 'стоп':
    word = input()
    num += 1
    if cat == 0:
        if 'кот' in word:
            cat = 1
            cat_line = num
            break
if cat == 0:
    print(-1)
else:
    print(cat_line)
