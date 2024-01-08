num_list = list()
new_num_list = list()
for _ in range(int(input())):
    num = int(input())
    num_list.append(num)
for i in range(len(num_list) - 1):
    new_num_list.append(num_list[i] + num_list[i + 1])
for num in new_num_list:
    print(num)
