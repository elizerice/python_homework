def who_are_you_and_hello():
    name = input()
    while True:
        if name[0].isupper() and " " not in name and name.isalpha():
            print('Привет, ', name)
            break
        else:
            name = input()
who_are_you_and_hello()
