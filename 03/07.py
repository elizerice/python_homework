print("Загадайте целое число от 1 до 1000")
min_num = 1
max_num = 1000
chance = 1
while chance <= 10:
    guess = (min_num + max_num) // 2
    print("Попытка", chance, "- предполагаю вы загадали число:", guess)
    feedback = input("Ваше число больше, меньше или равно загаданному числу? ")

    if feedback == ">":
        min_num = guess + 1
    elif feedback == "<":
        max_num = guess - 1
    elif feedback == "=":
        print("Я угадал ваше число")
        win = True
        break
    else:
        print("Введите >, < или =.")
        continue

    chance += 1
if win != True:
    print("Я не смог угадать ваше число")

