money_list = list()
for _ in range(int(input())):
    money = int(input())
    money_list.append(money)
for i in money_list:
    print(i)
print('')
for i in money_list:
    print(i * 2 + i)
