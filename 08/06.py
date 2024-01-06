max_lenght = int(input())
for i in range(int(input())):
    phrase = str(input())
    if len(phrase) > max_lenght-3:
        phrase = phrase[0:max_lenght-3] + '...'
    print(phrase)
