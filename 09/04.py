phrase_list = list()
num_list = list()
for i in range(int(input())):
    line = str(input())
    phrase_list.append(line)
sum_num = int(input())
for _ in range(sum_num):
    num = int(input())
    num_list.append(num)
for num in num_list:
    print(phrase_list[int(num) - 1])
