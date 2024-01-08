line_list = list()
search_list = list()
for _ in range(int(input())):
    line_list.append(input())
for _ in range(int(input())):
    search_list.append(input())
for i in line_list:
    count = 0
    for j in search_list:
        if j in i:
            count +=1
    if count == len(search_list):
        print(i)
