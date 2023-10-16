password_1 = input('введите пароль')
if len(password_1) < 8:
    print('короткий')
else:
    password_2 = input('повторите пароль')
    if password_1 != password_2:
        print('Различаются')
    else:
        print('OK')
