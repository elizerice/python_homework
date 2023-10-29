while True:
    password_1 = input()
    password_2 = input()
    if len(password_1) >= 8:
        if '123' not in password_1:
            if password_1 == password_2:
                print('OK!')
                break
            else:
                print('различаются')
        else:
            print('простой')
    else:
        print('короткий')
