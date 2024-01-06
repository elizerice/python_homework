for i in range(int(input())):
    phrase = input()
    if 'не ' in phrase[0:3] or 'Не ' in phrase[0:3]:
        print(phrase[3:])
    else:
        print(phrase)
