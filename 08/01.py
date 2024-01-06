word = input()
max_word = ''
min_word = word
while word != 'стоп':
    word = input()
    if len(max_word) < len(word):
        max_word = word
    if len(min_word) > len(word):
        min_word = word
if set(min_word) < set(max_word):
    print('yes')
else:
    print('no')
