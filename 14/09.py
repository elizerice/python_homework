def ask_password():
    password = 'password'
    for _ in range(3):
        if str(input()) != password:
            print('В доступе отказано')
        else:
            print('Пароль принят')
