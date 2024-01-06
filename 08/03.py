name = input()
for i in name:
    if i not in 'qwertyuiopasdfghjklzxcvbnm_1234567890':
        print('неверный символ ', i)
        break
else:
    print('OK')
