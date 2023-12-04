phone_book = {}
for i in range(int(input())):
    number, name = input().split(" ")
    if name not in phone_book:
        phone_book[name] = number
    else:
        phone_book[name] += " " + str(number)
for i in range(int(input())):
    print(phone_book.get(input(), "Нет в телефонной книге"))
