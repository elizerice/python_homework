word_1 = input('введите слово')
word_2 = input('введите следующее слово')
while True:
    word_1 = word_2
    word_2 = input('введите следующее слово')
    if word_1[-1] != word_2[0]:
        break;
print(word_2)
