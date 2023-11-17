num = 0
cat = 0
word = str()
cat_line = int()
count = int()
while word != 'стоп':
    word = input()
    num += 1
    if cat == 0:
        cat_line = num
    if 'кот' in word:
        cat = 1
        count += 1
    if word == 'стоп':
        break
if cat == 0:
    print(-1)
else:
    print(count, cat_line)
