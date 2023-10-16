login = input('введите логин')
mail = input('введите почту')
if '@' in login:
    print('некорректный логин')
elif '@' not in mail:
    print('некорректный адрес')
else:
    print('OK')
