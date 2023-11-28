word = str(input())
num = int(input())
if num > len(word) or num <= 0:
    print('ошибка')
else:
    print(word[num-1])
