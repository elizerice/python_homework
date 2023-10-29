num = int(input())
situation = False
for i in range(num):
    phrase = str(input())
    if 'кот' in phrase:
        print('мяу')
        situation = True
        break
if situation == False:
    print('нет')
