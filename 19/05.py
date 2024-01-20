def ask_password(login, password, success, failure):
    vowels ="aeuiioy"
    vowels_count = 0
    password_copy = list(password)
    login_copy = list(login)
    for i in password:
        if i in vowels:
            vowels_count += 1
            password_copy.remove(i)
    [login_copy.remove(i) for i in login if i in vowels]
    if vowels_count != 3 and password_copy != login_copy:
        failure(login, "Everything is wrong")
    elif password_copy != login_copy:
        failure(login,"Wrong consonants")
    elif vowels_count != 3:
        failure(login,"Wrong number of vowels")
    else:
        success(login)


def failure(login, error):
    print(f"Кто - то пытался притвориться пользователем {login}, но в пароле допустил ошибку: {error.upper()}.")



def success(login):
    print(f"Привет, {login}")


def main(login, password):
    ask_password(login, password, success, failure)
