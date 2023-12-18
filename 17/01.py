phrase_list = list()
def parrot(phrase):
    if phrase in phrase_list:
        print(phrase)
    else:
        phrase_list.append(phrase)


parrot("Привет")
parrot("Как тебя зовут?")
parrot("Привет")
