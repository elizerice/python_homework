num = 0
cat = 0
word = str()
nums = str()
while word != 'стоп':
    word = input()
    num += 1
    if 'кот' in word:
        cat = 1
        nums += str(num)
    
    if word == 'стоп':
        break
if cat == 0:
    print(-1)
else:
    print(nums)
