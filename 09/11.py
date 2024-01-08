white_list = list()
analys_list = list()
for _ in range(int(input())):
    white_list.append(input())
for _ in range(int(input())):
    analys_list.append(input())
for i in analys_list:
    if i in white_list:
        print(i)
