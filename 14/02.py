text = input()
def space_game(text):
    count = 0
    for i in text:
        if i == ' ':
            count += 1
    if count % 2 == 0:
        print('Вы выиграли')
    else:
        print('Вы проиграли')
space_game(text)
